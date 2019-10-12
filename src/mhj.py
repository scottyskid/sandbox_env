import os
import sys
import logging

import pandas as pd
import requests

# if importing local packages insure src file is marked as source directory

if __name__ == '__main__':
    foot_traffic = pd.read_csv("A:\CHEPdata\@chep\che1699__michael_hill_jeweller__hackathon\csv\hackathon__foot_traffic_by_store.csv")
    stores = pd.read_csv(
        "A:\CHEPdata\@chep\che1699__michael_hill_jeweller__hackathon\csv\hackathon__store_by_tv_region.csv")

    foot_traffic()
