import pandas as pd

park_info = pd.read_csv('national_parks_sample.csv')

result = park_info.query("Park == 'Everglades'")[
    ["Park", "Region", "TrailMiles"]
]

print(result.to_string(index=False))
