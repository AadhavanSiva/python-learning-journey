import pandas as pd
import numpy as np

df = pd.read_csv('census.csv')
df = df[df['SUMLEV']==50]
df.head()



for state in df['STNAME'].unique():
    avg = np.average(df.where(df['STNAME']==state).dropna()['CENSUS2010POP'])
    print('Counties in state ' + state +
          ' have an average population of ' + str(avg))


for group, frame in df.groupby('STNAME'):

    avg = np.average(frame['CENSUS2010POP'])
    print('Counties in state ' + group +
          ' have an average population of ' + str(avg))

for group, frame in df.groupby('STNAME'):
    avg = np.average(frame['CENSUS2010POP'])
    print('Counties in state ' + group +
          ' have an average population of ' + str(avg))

df = df.set_index('STNAME')

def set_batch_number(item):
    if item[0]<'M':
        return 0
    if item[0]<'Q':
        return 1
    return 2


for group, frame in df.groupby(set_batch_number):
    print('There are ' + str(len(frame)) + ' records in group ' + str(group) + ' for processing.')

df=pd.read_csv("listings.csv")
print(df.head())

df=df.set_index(["cancellation_policy","review_scores_value"])

for group, frame in df.groupby(level=(0,1)):
    print(group)

def grouping_fun(item):

    if item[1] == 10.0:
        return (item[0],"10.0")
    else:
        return (item[0],"not 10.0")

for group, frame in df.groupby(by=grouping_fun):
    print(group)

df=df.reset_index()

df.groupby("cancellation_policy").agg({"review_scores_value":np.average})

df.groupby("cancellation_policy").agg({"review_scores_value":np.nanmean})