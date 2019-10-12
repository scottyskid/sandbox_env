import os
import sys
import logging

import pandas as pd
import requests

def split_names(data):
    clean = []
    for index, row in data.iterrows():
        names = row['Best & Fairest'].split(',')
        for i in names:
            clean.append([row['Timestamp'], i.strip()])

    clean = pd.DataFrame(clean, columns=['date', 'name'])
    clean = clean.replace('Sophie Drysddale', 'Sophie Drysdale')
    return clean
    


if __name__ == "__main__":

    # Need to check names
    # Compare to total points scored

    data = pd.read_csv(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'data_in', 'hockey_bnf.csv'))
    data = split_names(data)
    data['value'] = 1
    data= data.groupby(['date', 'name'])['value'].count()
    data = data.reset_index()
    data['rank'] = data.groupby('date')['value'].rank(method='dense', ascending=False)
    data = data[data['rank'] <= 3]
    data['rank'] = abs(data['rank'] - 4)
    data = data.groupby('name')['rank'].sum().sort_values(ascending=False)
    # data['rank'] = data['value'].rank(method='dense', ascending=False)
    
    
    print(data)


    