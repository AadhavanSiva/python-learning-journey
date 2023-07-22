import pandas as pd

df=pd.DataFrame(['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D'],
                index=['excellent', 'excellent', 'excellent', 'good', 'good', 'good',
                       'ok', 'ok', 'ok', 'poor', 'poor'],
               columns=["Grades"])
print(df.dtypes)

print(df["Grades"].astype("category").head())

my_categories=pd.CategoricalDtype(categories=['D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+'],
                           ordered=True)
grades=df["Grades"].astype(my_categories)
print(grades.head())

print(df[df["Grades"]>"C"])

import numpy as np

df=pd.read_csv("census.csv")

df=df[df['SUMLEV']==50]

df=df.set_index('STNAME').groupby(level=0)['CENSUS2010POP'].agg(np.average)

print(df.head())

