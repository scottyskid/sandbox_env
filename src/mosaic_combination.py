import os
import sys
import logging

import pandas as pd
import requests


if __name__ == "__main__":
    path = "C:\\Users\\CHESCS\\OneDrive\\@projects_sjbs\\CHE Proximity\\insights_desk_ref_code\\data_out"
    data = pd.read_csv(os.path.join(path, "data.csv"))
    metadata = pd.read_csv(os.path.join(path, "metadata.csv"), encoding="latin_1")
    segements = pd.read_csv(os.path.join(path, "segments.csv"))

    full_data = pd.merge(data, metadata, on="profile_id", how="inner")
    full_data = pd.merge(full_data, segements, on="segment", how="inner")
    
    full_data.to_csv(os.path.join(path, 'full_data.csv'), index=False)


    print(full_data)
    
