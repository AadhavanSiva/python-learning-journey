import pandas as pd

df=pd.read_csv ('datasets/grades.csv')
df.head()

print("There are {} rows and {} columns".format(df.shape[0], df.shape[1]))

early_finishers=df[pd.to_datetime(df['assignment1_submission']) < '2016']
early_finishers.head()


late_finishers=df[~df.index.isin(early_finishers.index)]
late_finishers.head()


print(early_finishers['assignment1_grade'].mean())
print(late_finishers['assignment1_grade'].mean())

