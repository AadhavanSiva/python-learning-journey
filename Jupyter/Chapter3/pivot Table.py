import pandas as pd
import numpy as np

df = pd.read_csv('cwurData.csv')
print(df.head())

def create_category(ranking):
    if (ranking >= 1) & (ranking <= 100):
        return "First Tier Top Unversity"
    elif (ranking >= 101) & (ranking <= 200):
        return "Second Tier Top Unversity"
    elif (ranking >= 201) & (ranking <= 300):
        return "Third Tier Top Unversity"
    return "Other Top Unversity"

df['Rank_Level'] = df['world_rank'].apply(lambda x: create_category(x))
print(df.head())

print(df.pivot_table(values='score', index='country', columns='Rank_Level', aggfunc=[np.mean]).head())

print(df.pivot_table(values='score', index='country', columns='Rank_Level', aggfunc=[np.mean, np.max]).head())

print(df.pivot_table(values='score', index='country', columns='Rank_Level', aggfunc=[np.mean, np.max],
               margins=True).head())

new_df=df.pivot_table(values='score', index='country', columns='Rank_Level', aggfunc=[np.mean, np.max],
               margins=True)
print(new_df.index)
print(new_df.columns)

print(new_df['mean']['First Tier Top Unversity'].head())

print(type(new_df['mean']['First Tier Top Unversity']))

print(new_df['mean']['First Tier Top Unversity'].idxmax())

print(new_df.unstack().unstack().head())