import pandas as pd
import numpy as np


pd.Timestamp('9/1/2019 10:05AM')

pd.Timestamp(2019, 12, 20, 0, 0)

pd.Timestamp(2019, 12, 20, 0, 0).isoweekday()

pd.Timestamp(2019, 12, 20, 5, 2,23).second

pd.Period('1/2016')

pd.Period('3/5/2016')

pd.Period('1/2016') + 5

pd.Period('3/5/2016') - 2



t1 = pd.Series(list('abc'), [pd.Timestamp('2016-09-01'), pd.Timestamp('2016-09-02'),
                             pd.Timestamp('2016-09-03')])
print(t1)

t2 = pd.Series(list('def'), [pd.Period('2016-09'), pd.Period('2016-10'),
                             pd.Period('2016-11')])
print(t2)

type(t2.index)

d1 = ['2 June 2013', 'Aug 29, 2014', '2015-06-26', '7/12/16']



print(pd.to_datetime('4.7.12', dayfirst=True))


print(pd.Timestamp('9/3/2016')-pd.Timestamp('9/1/2016'))

print(pd.Timestamp('9/2/2016 8:10AM') + pd.Timedelta('12D 3H'))

print(pd.Timestamp('9/4/2016').weekday())

print(pd.Timestamp('9/4/2016') + pd.offsets.Week())

print(pd.Timestamp('9/4/2016') + pd.offsets.MonthEnd())

