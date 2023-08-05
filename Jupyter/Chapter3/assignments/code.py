import pandas as pd
import re
import numpy as np

import warnings
warnings.filterwarnings('ignore')
#Opened xls file in google sheet and removed the header, footer and unncessary columns, then
# downloaded the file as csv format.

df1 = pd.read_csv ('assets/Converted Energy Indicators.csv')

def rename_countries(df):
    country_mapping = {
        "Republic of Korea": "South Korea",
        "United States of America": "United States",
        "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
        "China, Hong Kong Special Administrative Region": "Hong Kong",
    }

    df = df['Country'].replace(country_mapping)
    return df

def clean_country_name(name):
    cleaned_name = re.sub(r'\([^)]*\)|\d', '', name).strip()
    return cleaned_name


def clean_dataframe(df):

    df['Country'] = df['Country'].apply(clean_country_name)
    return df

#print(clean_dataframe(df1).head(26))



df2 = pd.read_csv ('assets/world_bank.csv')

df2.columns = [col if col != 'Data Source' else 'Country' for col in df2.columns]
df2 = df2.drop(df2.index[:4])
# Reset the index to reflect the changes
df2.reset_index(drop=True, inplace=True)



def rename_countries2(df):
    country_mapping = {
        "Korea, Rep.": "South Korea",  "Iran, Islamic Rep.": "Iran", "Hong Kong SAR, China": "Hong Kong"
    }

    df = df.replace(country_mapping)
    return df

df3 = pd.read_csv ('assets/scimagojr-3.csv')


def mergedf(df1,df2):
    return pd.merge(df1, df2, how='right', on='Country')


def answer_one_aadhavan():

    mainDf = mergedf(mergedf(df1,df2),df3)

    print(type(mainDf))
    assert type(mainDf) == pd.DataFrame, "Q1: You should return a DataFrame!"

    mainDf.to_csv('mainDf,csv', index=False)


#print(mergedf(df1,df2).head(15))

#QUESTION 3:


def answer_one():
    import pandas as pd

    df1 = pd.read_excel('assets/Energy Indicators.xls', na_values=["..."], header=None, skiprows=18, skipfooter=38,
                           usecols=[2, 3, 4, 5],
                           names=['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable'])
    df1['Energy Supply'] = df1['Energy Supply'].apply(lambda x: x * 1000000)

    df1['Country'] = df1['Country'].str.replace(r" \(.*\)", "")
    df1['Country'] = df1['Country'].str.replace(r"\d*", "")
    df1['Country'] = df1['Country'].replace({'Republic of Korea': 'South Korea',
                                                   'United Kingdom of Great Britain and Northern Ireland': 'United Kingdom',
                                                    'United States of America': 'United States',
                                                   'China, Hong Kong Special Administrative Region': 'Hong Kong'})

    df2= pd.read_csv('assets/world_bank.csv', skiprows=4)
    df2['Country Name'] = df2['Country Name'].replace({
                                                        'Iran, Islamic Rep.': 'Iran',
                                                        'Korea, Rep.': 'South Korea',
                                                       'Hong Kong SAR, China': 'Hong Kong'})

    df3 = pd.read_excel('assets/scimagojr-3.xlsx')

    mergeRank = pd.merge(df3, df1, how="inner", left_on="Country", right_on="Country")
    mergeRank = mergeRank[mergeRank["Rank"] <= 15]

    df2.rename(columns={"Country Name": "Country"}, inplace=True)
    df2 = df2.loc[:, ['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', "Country"]]
    finalMerge = pd.merge(mergeRank, df2, how="inner", left_on="Country", right_on="Country").set_index("Country")

    finalMerge.to_csv("assets/out.csv")
    return finalMerge


#QUESTION 2:

def answer_two():
    import pandas as pd

    df1 = pd.read_excel('assets/Energy Indicators.xls',na_values=["..."],header = None,skiprows=18,skipfooter= 38,usecols=[2,3,4,5],names=['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable'])
    df1['Energy Supply'] = df1['Energy Supply'].apply(lambda x: x*1000000)

    df1['Country'] = df1['Country'].str.replace(r" \(.*\)","")
    df1['Country'] = df1['Country'].str.replace(r"\d*","")
    df1['Country'] = df1['Country'].replace({'Republic of Korea' : 'South Korea',
                                               'United States of America' : 'United States',
                                               'United Kingdom of Great Britain and Northern Ireland':'United Kingdom',
                                               'China, Hong Kong Special Administrative Region':'Hong Kong'})

    df2 = pd.read_csv('assets/world_bank.csv', skiprows = 4)
    df2['Country Name'] = df2['Country Name'].replace({'Korea, Rep.': 'South Korea',
                                                       'Iran, Islamic Rep.': 'Iran',
                                                       'Hong Kong SAR, China' : 'Hong Kong'})

    df3 = pd.read_excel('assets/scimagojr-3.xlsx')

    innerMerge = pd.merge(df3,df1,how="inner",left_on="Country",right_on="Country")

    df2.rename(columns = {"Country Name":"Country"},inplace=True)
    df2 = df2.loc[:,['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015',"Country"]]
    inner2 = pd.merge(innerMerge,df2,how="inner",left_on="Country",right_on="Country").set_index("Country")

    outerMerge = pd.merge(df3,df1,how="outer",left_on="Country",right_on="Country")
    outer2 = pd.merge(outerMerge,df2,how="outer",left_on="Country",right_on="Country").set_index("Country")

    return len(outer2)-len(inner2)


def answer_three():

    import numpy as np
    mainDf = answer_one()
    return mainDf[["2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015"]]\
        .apply(np.mean, axis=1).sort_values(ascending=False)



#QUESTION 4:

def answer_four():
    import pandas as pd
    import re
    import numpy as np


    mainDf =answer_one()
    mainDf['avgGDP']=mainDf[["2006","2007","2008","2009","2010","2011","2012","2013","2014","2015"]].apply(np.mean,axis = 1)
    mainDf.sort_values(['avgGDP'],ascending = False,inplace=True)
    return mainDf.iloc[5]['2015']-mainDf.iloc[5]['2006']



#QUESTION 5:

def answer_five():

    mainDf = answer_one()
    return mainDf['Energy Supply per Capita'].mean()


#QUESTION 6:

def answer_six():
    mainDf = answer_one()
    result = mainDf.sort_values(by='% Renewable', ascending=False).iloc[0]
    return (result.name, result['% Renewable'])



df = pd.read_csv('mainDf.csv')




#QUESTION 7:

def answer_seven():
    mainDf = answer_one()
    mainDf['Citation ratio'] = mainDf['Self-citations'] / mainDf['Citations']
    result = mainDf.sort_values(by='Citation ratio', ascending=False).iloc[0]
    return (result.name, result['Citation ratio'])




#QUESTION 8

def answer_eight():
    mainDf = answer_one()
    return (mainDf['Energy Supply']/mainDf['Energy Supply per Capita']).sort_values(ascending=False).index[2]


def answer_nine():
    # YOUR CODE HERE
    # raise NotImplementedError()
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['Citable docs per Capita'] = Top15['Citable documents'] / Top15['PopEst']
    return Top15['Citable docs per Capita'].corr(Top15['Energy Supply per Capita'])


def plot9():
    import matplotlib as plt
 #   %matplotlib inline

    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['Citable docs per Capita'] = Top15['Citable documents'] / Top15['PopEst']
    Top15.plot(x='Citable docs per Capita', y='Energy Supply per Capita', kind='scatter', xlim=[0, 0.0006])



def answer_ten():
    # YOUR CODE HERE
    # raise NotImplementedError()
    Top15 = answer_one()
    df=Top15["% Renewable"].median()
    Top15["HighRenew"]= Top15["% Renewable"].apply(lambda x:0 if x<df else 1 )
    return Top15["HighRenew"]

def answer_eleven():
    # YOUR CODE HERE
    # raise NotImplementedError()
    ContinentDict  = {'China':'Asia',
                  'United States':'North America',
                  'Japan':'Asia',
                  'United Kingdom':'Europe',
                  'Russian Federation':'Europe',
                  'Canada':'North America',
                  'Germany':'Europe',
                  'India':'Asia',
                  'France':'Europe',
                  'South Korea':'Asia',
                  'Italy':'Europe',
                  'Spain':'Europe',
                  'Iran':'Asia',
                  'Australia':'Australia',
                  'Brazil':'South America'}

    df = answer_one()
    df['PopEst'] = df['Energy Supply'] / df['Energy Supply per Capita']
    df['Continent'] = pd.Series(ContinentDict)

    return df.groupby('Continent')['PopEst'].agg([np.size,np.sum, np.mean, np.std])

def answer_twelve():
    # YOUR CODE HERE
    # raise NotImplementedError()
    ContinentDict  = {'China':'Asia',
                  'United States':'North America',
                  'Japan':'Asia',
                  'United Kingdom':'Europe',
                  'Russian Federation':'Europe',
                  'Canada':'North America',
                  'Germany':'Europe',
                  'India':'Asia',
                  'France':'Europe',
                  'South Korea':'Asia',
                  'Italy':'Europe',
                  'Spain':'Europe',
                  'Iran':'Asia',
                  'Australia':'Australia',
                  'Brazil':'South America'}

    df = answer_one()

    print(df)
    print("**** length ****")

    print(len(df))
    print("**** columns ****")

    #print(df['Country'].unique())
    df['Continent'] = pd.Series(ContinentDict)
    df['% Renewable']=pd.cut(df['% Renewable'],5)

    return df.groupby(['Continent','% Renewable'])['Continent'].agg(np.size).dropna()


print(len(answer_twelve()))


def answer_thirteen():
    # YOUR CODE HERE
    # raise NotImplementedError()
    df = answer_one()
    df['PopEst'] = df['Energy Supply'] / df['Energy Supply per Capita']
    return df['PopEst'].apply('{:,}'.format)

print(type(answer_twelve()))