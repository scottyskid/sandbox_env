import os
import logging

import pandas as pd

def read_data():
    """
    reads in all the neccessary data and returns it in a pandas DataFrame
    """

    # Path that incoming data sits 


    data_in_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'data_in')
    print(data_in_path)
    #Import vff data
    vff_ad_data = pd.read_csv(os.path.join(data_in_path, 'vff_ad_data.csv'))

    return vff_ad_data


def data_transformation(data):
    # print("Show the dataset")
    # print(data)
    # print("\n")


    # print("Show the datatypes of the dataset")
    # print(data.dtypes)
    # print("\n")


    # print(data['ad_group'])
    #There is something wrong with doing it this way
    data['viewable_impressions_v2'] = data['viewable_impressions'].fillna(0)
    print(data[['viewable_impressions','viewable_impressions_v2']])

    # print("Show the filled na values")
    # print(data['viewable_impressions'])
    # print("\n")


    data['impressions'] = data['impressions'].fillna(0)
    data['ctr_1'] = data['clicks'] / data['impressions']
    # # data['ctr_2'] = data.apply(lambda x: x['clicks'] / x['impressions'], axis=1)

    print("Show the dataset")
    print(data[['impressions', 'clicks', 'ctr_1']])
    print("\n")
    


def to_csv(data):
    pass


import pandas as pd 


vff_data = pd.read_csv(r'C:\Users\CHESCS\OneDrive\@projects_sjbs\@personal\sandbox_env\data_in\vff_ad_data.csv')

is_date = vff_data['date'] = ['11-11-17', '11-12-17']
limited_date = vff_data[is_date]

dimentions = ['channel', 'platform']
metrics= ['clicks', 'impressions','views']



vff_data_grouped = limited_date.groupby(dimentions)[metrics].sum()
vff_data_grouped['CTR'] = vff_data_grouped['clicks']/vff_data_grouped['impressions']

print(vff_date_grouped)



print()














if __name__ == "__main__":

    pass
    # vff_ad_data = read_data()

    # data_transformation(vff_ad_data)


# Read data
# Export data
