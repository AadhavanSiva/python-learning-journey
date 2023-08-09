import pandas as pd
import numpy as np
import scipy.stats as stats
import re

cities = pd.read_html("assets/wikipedia_data.html")[1]
cities = cities.iloc[:-1, [0, 3, 5, 6, 7, 8]]
cities.rename(columns={"Population (2016 est.)[8]": "Population"},
              inplace=True)
cities['NFL'] = cities['NFL'].str.replace(r"\[.*\]", "")
cities['MLB'] = cities['MLB'].str.replace(r"\[.*\]", "")
cities['NBA'] = cities['NBA'].str.replace(r"\[.*\]", "")
cities['NHL'] = cities['NHL'].str.replace(r"\[.*\]", "")


def nhl_df():
    dfname = 'NHL'
    team = cities[dfname].str.extract(
        '([A-Z]{0,2}[a-z0-9]*\ [A-Z]{0,2}[a-z0-9]*|[A-Z]{0,2}[a-z0-9]*)([A-Z]{0,2}[a-z0-9]*\ [A-Z]{0,2}[a-z0-9]*|[A-Z]{0,2}[a-z0-9]*)([A-Z]{0,2}[a-z0-9]*\ [A-Z]{0,2}[a-z0-9]*|[A-Z]{0,2}[a-z0-9]*)')
    team['Metropolitan area'] = cities['Metropolitan area']
    team = pd.melt(team, id_vars=['Metropolitan area']).drop(columns=['variable']).replace("", np.nan).replace("—",
                                                                                                               np.nan).dropna().reset_index().rename(
        columns={"value": "team"})
    team = pd.merge(team, cities, how='left', on='Metropolitan area').iloc[:, 1:4]
    team = team.astype({'Metropolitan area': str, 'team': str, 'Population': int})
    team['team'] = team['team'].str.replace('[\w.]*\ ', '')

    df = pd.read_csv("assets/" + str.lower(dfname) + ".csv")
    df = df[df['year'] == 2018]
    df['team'] = df['team'].str.replace(r'\*', "")
    df = df[['team', 'W', 'L']]

    dropList = []
    for i in range(df.shape[0]):
        row = df.iloc[i]
        if row['team'] == row['W'] and row['L'] == row['W']:
            dropList.append(i)
    df = df.drop(dropList)

    df['team'] = df['team'].str.replace('[\w.]* ', '')
    df = df.astype({'team': str, 'W': int, 'L': int})
    df['W/L%'] = df['W'] / (df['W'] + df['L'])

    teamdf = pd.merge(team, df, 'inner', on='team')
    teamdf = teamdf.groupby('Metropolitan area').agg({'W/L%': np.nanmean, 'Population': np.nanmean})

    return teamdf[['W/L%']]


def nba_df():
    dfname = 'NBA'
    team = cities[dfname].str.extract(
        '([A-Z]{0,2}[a-z0-9]*\ [A-Z]{0,2}[a-z0-9]*|[A-Z]{0,2}[a-z0-9]*)([A-Z]{0,2}[a-z0-9]*\ [A-Z]{0,2}[a-z0-9]*|[A-Z]{0,2}[a-z0-9]*)([A-Z]{0,2}[a-z0-9]*\ [A-Z]{0,2}[a-z0-9]*|[A-Z]{0,2}[a-z0-9]*)')
    team['Metropolitan area'] = cities['Metropolitan area']
    team = pd.melt(team, id_vars=['Metropolitan area']).drop(columns=['variable']).replace("", np.nan).replace("—",
                                                                                                               np.nan).dropna().reset_index().rename(
        columns={"value": "team"})
    team = pd.merge(team, cities, how='left', on='Metropolitan area').iloc[:, 1:4]
    team = team.astype({'Metropolitan area': str, 'team': str, 'Population': int})
    team['team'] = team['team'].str.replace('[\w.]*\ ', '')

    df = pd.read_csv("assets/" + str.lower(dfname) + ".csv")
    df = df[df['year'] == 2018]
    df['team'] = df['team'].str.replace(r'[\*]', "")
    df['team'] = df['team'].str.replace(r'\(\d*\)', "")
    df['team'] = df['team'].str.replace(r'[\xa0]', "")
    df = df[['team', 'W/L%']]
    df['team'] = df['team'].str.replace('[\w.]* ', '')
    df = df.astype({'team': str, 'W/L%': float})

    teamdf = pd.merge(team, df, 'outer', on='team')
    teamdf = teamdf.groupby('Metropolitan area').agg({'W/L%': np.nanmean, 'Population': np.nanmean})
    return teamdf[['W/L%']]


def mlb_df():
    dfname = 'MLB'
    team = cities[dfname].str.extract(
        '([A-Z]{0,2}[a-z0-9]*\ [A-Z]{0,2}[a-z0-9]*|[A-Z]{0,2}[a-z0-9]*)([A-Z]{0,2}[a-z0-9]*\ [A-Z]{0,2}[a-z0-9]*|[A-Z]{0,2}[a-z0-9]*)([A-Z]{0,2}[a-z0-9]*\ [A-Z]{0,2}[a-z0-9]*|[A-Z]{0,2}[a-z0-9]*)')
    team['Metropolitan area'] = cities['Metropolitan area']
    team = pd.melt(team, id_vars=['Metropolitan area']).drop(columns=['variable']).replace("", np.nan).replace("—",
                                                                                                               np.nan).dropna().reset_index().rename(
        columns={"value": "team"})
    team = pd.merge(team, cities, how='left', on='Metropolitan area').iloc[:, 1:4]
    team = team.astype({'Metropolitan area': str, 'team': str, 'Population': int})
    team['team'] = team['team'].str.replace('\ Sox', 'Sox')
    team['team'] = team['team'].str.replace('[\w.]*\ ', '')

    df = pd.read_csv("assets/" + str.lower(dfname) + ".csv")
    df = df[df['year'] == 2018]
    df['team'] = df['team'].str.replace(r'[\*]', "")
    df['team'] = df['team'].str.replace(r'\(\d*\)', "")
    df['team'] = df['team'].str.replace(r'[\xa0]', "")
    df = df[['team', 'W-L%']]
    df.rename(columns={"W-L%": "W/L%"}, inplace=True)
    df['team'] = df['team'].str.replace('\ Sox', 'Sox')
    df['team'] = df['team'].str.replace('[\w.]* ', '')
    df = df.astype({'team': str, 'W/L%': float})

    teamdf = pd.merge(team, df, 'outer', on='team')
    teamdf = teamdf.groupby('Metropolitan area').agg({'W/L%': np.nanmean, 'Population': np.nanmean})

    return teamdf[['W/L%']]


def nfl_df():
    dfname = 'NFL'
    team = cities[dfname].str.extract(
        '([A-Z]{0,2}[a-z0-9]*\ [A-Z]{0,2}[a-z0-9]*|[A-Z]{0,2}[a-z0-9]*)([A-Z]{0,2}[a-z0-9]*\ [A-Z]{0,2}[a-z0-9]*|[A-Z]{0,2}[a-z0-9]*)([A-Z]{0,2}[a-z0-9]*\ [A-Z]{0,2}[a-z0-9]*|[A-Z]{0,2}[a-z0-9]*)')
    team['Metropolitan area'] = cities['Metropolitan area']
    team = pd.melt(team, id_vars=['Metropolitan area']).drop(columns=['variable']).replace("", np.nan).replace("—",
                                                                                                               np.nan).dropna().reset_index().rename(
        columns={"value": "team"})
    team = pd.merge(team, cities, how='left', on='Metropolitan area').iloc[:, 1:4]
    team = team.astype({'Metropolitan area': str, 'team': str, 'Population': int})
    team['team'] = team['team'].str.replace('[\w.]*\ ', '')

    df = pd.read_csv("assets/" + str.lower(dfname) + ".csv")
    df = df[df['year'] == 2018]
    df['team'] = df['team'].str.replace(r'[\*]', "")
    df['team'] = df['team'].str.replace(r'\(\d*\)', "")
    df['team'] = df['team'].str.replace(r'[\xa0]', "")
    df = df[['team', 'W-L%']]
    df.rename(columns={"W-L%": "W/L%"}, inplace=True)
    dropList = []
    for i in range(df.shape[0]):
        row = df.iloc[i]
        if row['team'] == row['W/L%']:
            dropList.append(i)
    df = df.drop(dropList)

    df['team'] = df['team'].str.replace('[\w.]* ', '')
    df['team'] = df['team'].str.replace('+', '')
    df = df.astype({'team': str, 'W/L%': float})

    teamdf = pd.merge(team, df, 'outer', on='team')
    teamdf = teamdf.groupby('Metropolitan area').agg({'W/L%': np.nanmean, 'Population': np.nanmean})

    return teamdf[['W/L%']]


def create_df(sport):
    if sport == 'NFL':
        return nfl_df()
    elif sport == 'NBA':
        return nba_df()
    elif sport == 'NHL':
        return nhl_df()
    elif sport == 'MLB':
        return mlb_df()
    else:
        print("ERROR with intput!")


def sports_team_performance():
    # Note: p_values is a full dataframe, so df.loc["NFL","NBA"] should be the same as df.loc["NBA","NFL"] and
    # df.loc["NFL","NFL"] should return np.nan
    leagues = ['NFL', 'NBA', 'NHL', 'MLB']
    p_values = pd.DataFrame({k: np.nan for k in leagues}, index=leagues)

    for i in leagues:
        for j in leagues:
            if i != j:
                merge = pd.merge(create_df(i), create_df(j), 'inner', on=['Metropolitan area'])
                p_values.loc[i, j] = stats.ttest_rel(merge['W/L%_x'], merge['W/L%_y'])[1]

    assert abs(p_values.loc["NBA", "NHL"] - 0.02) <= 1e-2, "The NBA-NHL p-value should be around 0.02"
    assert abs(p_values.loc["MLB", "NFL"] - 0.80) <= 1e-2, "The MLB-NFL p-value should be around 0.80"
    return p_values