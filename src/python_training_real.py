import os 

import pandas as pd 


if __name__ == "__main__":
    file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', "data_in", "241801_Untitled_Report_20181025_090831_841860532.csv")
    print(file_path)
    df = pd.read_csv(file_path, skiprows=16)
    print(df.dtypes)
