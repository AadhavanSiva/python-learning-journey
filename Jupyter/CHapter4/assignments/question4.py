import pandas as pd
import numpy as np
import scipy.stats as stats
import re


def nfl_correlation():
    # YOUR CODE HERE
    # raise NotImplementedError()

    nfl_df = pd.read_csv("assets/nfl.csv")
    cities = pd.read_html("assets/wikipedia_data.html")[1]
    cities = cities.iloc[:-1, [0, 3, 5, 6, 7, 8]]

    nfl_df.drop([0, 5, 10, 15, 20, 25, 30, 35], 0, inplace=True)

    cities.drop([13, 22, 27, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 45, 46, 47, 49, 50], 0,
                inplace=True)

    l1 = []
    for i in nfl_df['team']:
        # i=i.rstrip()
        i = i.split('*')
        l1.append(i[0])
    nfl_df['team'] = l1

    l2 = []
    for i in nfl_df['team']:
        i = i.split('+')
        l2.append(i[0])
    nfl_df['team'] = l2

    nfl_df = nfl_df.head(32)

    nfl_df['team_ville'] = nfl_df['team']
    nfl_df['team_ville'] = nfl_df['team_ville'].map({'New England Patriots': 'Boston',
                                                     'Miami Dolphins': 'Miami–Fort Lauderdale',
                                                     'Buffalo Bills': 'Buffalo',
                                                     'New York Jets': 'New York City',
                                                     'Baltimore Ravens': 'Baltimore',
                                                     'Pittsburgh Steelers': 'Pittsburgh',
                                                     'Cleveland Browns': 'Cleveland',
                                                     'Cincinnati Bengals': 'Cincinnati',
                                                     'Houston Texans': 'Houston',
                                                     'Indianapolis Colts': 'Indianapolis',
                                                     'Tennessee Titans': 'Nashville',
                                                     'Jacksonville Jaguars': 'Jacksonville',
                                                     'Kansas City Chiefs': 'Kansas City',
                                                     'Los Angeles Chargers': 'Los Angeles',
                                                     'Denver Broncos': 'Denver',
                                                     'Oakland Raiders': 'San Francisco Bay Area',
                                                     'Dallas Cowboys': 'Dallas–Fort Worth',
                                                     'Philadelphia Eagles': 'Philadelphia',
                                                     'Washington Redskins': 'Washington, D.C.',
                                                     'New York Giants': 'New York City',
                                                     'Chicago Bears': 'Chicago',
                                                     'Minnesota Vikings': 'Minneapolis–Saint Paul',
                                                     'Green Bay Packers': 'Green Bay',
                                                     'Detroit Lions': 'Detroit',
                                                     'New Orleans Saints': 'New Orleans',
                                                     'Carolina Panthers': 'Charlotte',
                                                     'Atlanta Falcons': 'Atlanta',
                                                     'Tampa Bay Buccaneers': 'Tampa Bay Area',
                                                     'Los Angeles Rams': 'Los Angeles',
                                                     'Seattle Seahawks': 'Seattle',
                                                     'San Francisco 49ers': 'San Francisco Bay Area',
                                                     'Arizona Cardinals': 'Phoenix'})

    df4 = pd.merge(nfl_df, cities, left_on="team_ville", right_on="Metropolitan area")

    df4['W'] = pd.to_numeric(df4['W'])
    df4['L'] = pd.to_numeric(df4['L'])
    df4['Population (2016 est.)[8]'] = pd.to_numeric(df4['Population (2016 est.)[8]'])
    he = ['team', 'W', 'L', 'Metropolitan area', 'Population (2016 est.)[8]']
    df4 = df4[he]
    df4['W/L'] = df4['W'] / (df4['L'] + df4['W'])
    df4 = df4.groupby('Metropolitan area').mean().reset_index()

    population_by_region = df4['Population (2016 est.)[8]']  # pass in metropolitan area population from cities
    win_loss_by_region = df4[
        'W/L']  # pass in win/loss ratio from nfl_df in the same order as cities["Metropolitan area"]

    assert len(population_by_region) == len(win_loss_by_region), "Q4: Your lists must be the same length"
    assert len(population_by_region) == 29, "Q4: There should be 29 teams being analysed for NFL"

    return stats.pearsonr(population_by_region, win_loss_by_region)[0]