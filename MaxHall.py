import pandas as pd

student_info = {
    "name": "Zendaya" , 
    "year": "Freshman" , 
    "age": 30,
    "graduated": False,
    "fav_class": "Accounting 310"
}

print(student_info)

df = pd.DataFrame([student_info])

print(df)