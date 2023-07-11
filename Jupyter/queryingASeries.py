import pandas as pd

grades = pd.Series([90, 80, 70, 60])

total = 0
for grade in grades:
    total+=grade
print(total/len(grades))

import numpy as np

# Then we just call np.sum and pass in an iterable item. In this case, our panda series.

total = np.average(grades)
print(total)
numbers = pd.Series(np.random.randint(0,1000,10000))




numbers.head()