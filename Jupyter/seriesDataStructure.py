import pandas as pd
import numpy as np

students = ['Alice', 'Jack', 'Molly']

print(pd.Series(students))

students = ['Alice', 'Jack', None]

print(pd.Series(students))

print(np.nan == None)

students_scores = {'Alice': 'Physics',
                   'Jack': 'Chemistry',
                   'Molly': 'English'}
s = pd.Series(students_scores)
print(s)

print(s.index)

students = [("Alice","Brown"), ("Jack", "White"), ("Molly", "Green")]
print(pd.Series(students))

s = pd.Series(['Physics', 'Chemistry', 'English'], index=['Alice', 'Jack', 'Molly'])
print(s)