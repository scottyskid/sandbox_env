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
__created__ = "2019-05-22"
__copyright__ = "Copyright 2019, CHE Proximity"
__credits__ = ["Scotty Skidmore"]

__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Scotty Skidmore"
__email__ = "scotty.skidmore@cheproximity.com.au"
__status__ = "Development" # "Development", "Prototype", or "Production"


def setup_logging(default_path, default_level=logging.INFO, env_key='LOG_CFG'):
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



if __name__ == "__main__":
    script_start = time.time()
    try:
        BASE_DIR = Path(__file__).resolve().parent.parent
        DATA_EXTRACT_PATH =  BASE_DIR / 'data_extract'
        DATA_LOAD_PATH = BASE_DIR / 'data_load'
        DATA_TRANSFORM_PATH = BASE_DIR / 'data_transform'
        LOGS_PATH = BASE_DIR / 'logs'

        setup_logging(LOGS_PATH / 'logging.yaml')
        logging.info("__main__ start")



        logging.info("__main__ end successfully")
    except Exception as e:
        logging.error("__main__ end with error")
        raise
    finally:
        print(f"the script took {time.time() - script_start}s to complete")