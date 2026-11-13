import pandas as pd

park_info = pd.read_csv('national_parks_sample.csv')

for row, col in park_info.iterrows():
    print(row, col)
    print()