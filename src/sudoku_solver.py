#!/usr/bin/env python

"""Doc string short description

Docstring long description
"""

import logging, logging.config
import os
import sys
import time
from pathlib import Path

import pandas as pd
import numpy as np
import requests
import yaml
from pprint import pprint

# if importing local packages insure src file is marked as source directory

__author__ = "Scotty Skidmore"
__created__ = "2019-06-27"
__copyright__ = "Copyright 2019, CHE Proximity"
__credits__ = ["Scotty Skidmore"]

__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Scotty Skidmore"
__email__ = "scotty.skidmore@cheproximity.com.au"
__status__ = "Development" # "Development", "Prototype", or "Production"

def setup_logging(default_path, default_level=logging.DEBUG, env_key='LOG_CFG'):
    """Setup logging configuration

    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if path.exists():
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)
        logging.warning('logging.yaml not imported')

class Tile():
    def __init__(self, row, col, solved_value=0):
        self.is_solved = solved_value != 0
        self.solved_value = solved_value
        self.possible_values = list(range(1, 10))
        self.row = row
        self.col = col
        self.box = self.get_box(row, col)

    def __repr__(self):
        return repr(self.solved_value)

    def __str__(self):
        return str(self.solved_value)

    def get_box(self, row, col):
        boxes = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
        return boxes[(row - 1) // 3][(col - 1) // 3]

    def check_solved(self):
        if self.is_solved:
            pass
        elif len(self.possible_values) == 1:
            self.solved_value = self.possible_values[0]
            self.is_solved = True
        return self.is_solved


class Board():
    def __init__(self, starting_board):
        self.board_state = [] # look to change board state to just one long array rather than nested
        self.num_cols = 9
        self.num_rows = 9
        for row_num, row in enumerate(starting_board):
            for col_num, value in enumerate(row):
                tile = Tile(row_num + 1, col_num + 1, value)
                self.board_state.append(tile)


    def __repr__(self):
        return repr(self.board_state)

    def __str__(self):
        out_str = "  -----------------\n"
        for idx, tile in enumerate(self.board_state):
            if idx % self.num_cols == 0:
                out_str += "| "
            if tile.solved_value != 0:
                out_str += str(tile.solved_value) + ' '
            else:
                out_str += '  '
            if idx % self.num_cols == self.num_cols - 1:
                out_str += "|\n"
        out_str += "  -----------------\n"
        return out_str


    def _convert_to_board_state_index(self, row, col):
        return (row - 1) * self.num_cols + (col - 1)


    def get_tile(self, row, col): # todo
        if row not in range (1, self.num_rows + 1) or col not in range(1, self.num_cols + 1):
            raise ValueError(f"Value out of bounds: ({row}, {col})")

        idx = self._convert_to_board_state_index(row, col)
        return self.board_state[idx]


    def get_dimension(self, row=None, col=None, box=None):
        # todo can optimise this

        tiles = []
        for i, tile in enumerate(self.board_state):
            if tile.row == row or tile.col == col or tile.box == box:
                tiles.append(tile)

        return tiles


    def get_solved_tiles(self):
        solved_tiles = []
        for tile in self.board_state:
            if tile.is_solved:
                solved_tiles.append(tile)

        return solved_tiles


    def get_unsolved_tiles(self):
        unsolved_tiles = []
        for tiles in self.board_state:
            if not tiles.is_solved:
                unsolved_tiles.append(tiles)

        return unsolved_tiles


class Solver():
    def __init__(self, starting_board):
        self.board = Board(starting_board)
        self.solved_tiles = self.board.get_solved_tiles()
        self.unsolved_tiles = self.board.get_unsolved_tiles()
        self.useless_tiles = []

    def __str__(self):
        return str(self.board)

    def begin(self):
        print(self.board)
        while len(self.solved_tiles) > 0:
            tile = self.solved_tiles.pop()
            self.update_surrounding_tiles(tile)
            self.useless_tiles.append(tile)

        print(self.board)

    def update_surrounding_tiles(self, tile):
        surrounding_tiles = self.board.get_dimension(row=tile.row, col=tile.col, box=tile.box)
        for sur_tile in surrounding_tiles:
            if not sur_tile.is_solved:
                try:
                    sur_tile.possible_values.remove(tile.solved_value)
                    sur_tile.check_solved()
                    if sur_tile.is_solved:
                        self.solved_tiles.append(sur_tile)
                        self.unsolved_tiles.remove(sur_tile)

                except ValueError:
                    pass



if __name__ == "__main__":
    script_start = time.time()
    try:
        BASE_DIR = Path(__file__).resolve().parent
        DATA_EXTRACT_PATH =  BASE_DIR / 'data_extract'
        DATA_LOAD_PATH = BASE_DIR / 'data_load'
        DATA_TRANSFORM_PATH = BASE_DIR / 'data_transform'
        LOGS_PATH = BASE_DIR / 'logs'

        setup_logging(LOGS_PATH / 'logging.yaml')
        logging.info("__main__ start")

        starting_board = [
            [4, 9, 0, 8, 5, 1, 0, 0, 0],
            [7, 0, 6, 0, 0, 0, 1, 8, 5],
            [0, 0, 8, 0, 7, 6, 0, 4, 2],
            [0, 4, 0, 0, 9, 2, 7, 0, 1],
            [2, 0, 5, 0, 6, 0, 3, 0, 4],
            [6, 1, 0, 7, 0, 4, 0, 0, 8],
            [0, 0, 7, 9, 0, 3, 8, 1, 0],
            [9, 6, 1, 2, 0, 0, 0, 7, 0],
            [0, 8, 0, 6, 1, 0, 2, 5, 0],
        ]

        solver = Solver(starting_board)
        print(solver.begin())

        logging.info("__main__ end successfully")
    except Exception as e:
        logging.error("__main__ end with error")
        raise
    finally:
        print(f"the script took {time.time() - script_start}s to complete")

