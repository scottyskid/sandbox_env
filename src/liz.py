import pandas as pd
import os


pd.set_option('display.width', 200)
file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'data_in', 'csf11bp64.csv')
print(file_path)
abs_data = pd.read_csv(file_path)
print(abs_data.dtypes)
print(abs_data[["Age of persons", "Occupation"]])

