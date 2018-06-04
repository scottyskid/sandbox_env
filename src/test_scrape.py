import os
import sys
import logging

import pandas as pd
import requests

# if importing local packages insure src file is marked as source directory

url = "https://preview.danmurphys.com.au/product/DM_9067/johnnie-walker-black-label-scotch-whisky-700ml"

proxies = {
        'http': "http://bc-cls03.ccla.com.au:3128",
        'https': "http://bc-cls03.ccla.com.au:3128",
    }
session = requests.Session()
session.proxies = proxies
conn = session.get(url)
print(conn.text)
