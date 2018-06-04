import logging
import time

import numpy as np
import pandas as pd
from sqlalchemy import create_engine, event


def sqlalchemy_conn_string(dsn="test_scotty", uid="chepdata", pwd="chep2016DATA"):
    conn_str = f"mssql+pyodbc://{uid}:{pwd}@{dsn}"
    logging.debug(f"createed conn_string of {conn_str}")
    return conn_str


def get_sqlalchemy_engine(conn_string, echo=False):
    engine = create_engine(conn_string, echo=echo)

    # This implements the execute many function when pd.to_sql is called to speed up exports
    @event.listens_for(engine, 'before_cursor_execute')
    def receive_before_cursor_execute(conn, cursor, statement, params, context, executemany):
        if executemany:
            cursor.fast_executemany = True

    return engine


def df_to_db(df, table, engine, if_exists='fail', chunksize=100000, dtype=None):
    s = time.time()
    df.to_sql(table, engine, if_exists=if_exists, index=False, chunksize=chunksize, dtype=dtype)
    logging.info(f"{time.time() - s}s to run df.to_sql with a df length of {len(df)}")


if __name__ == '__main__':
    log_format = '%(asctime)s %(levelname)s:%(filename)s:%(funcName)s:%(lineno)d: %(message)s'
    logging.basicConfig(format=log_format, filename='..\\logs\\records_test.log', level=logging.DEBUG)

    df = pd.DataFrame(np.random.random(((10 ** 1) * 1, 100)))
    table = 'fast_executemany_test'
    conn_string = sqlalchemy_conn_string()
    engine = get_sqlalchemy_engine(conn_string, True)

    df_to_db(df, table, engine, if_exists='replace', chunksize=100000)