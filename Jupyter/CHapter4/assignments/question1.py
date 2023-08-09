import pandas as pd
import numpy as np
import scipy.stats as stats
import re


def nhl_correlation():
    # YOUR CODE HERE
    # raise NotImplementedError()

    nhl_df = pd.read_csv("assets/nhl.csv")
    cities = pd.read_html("assets/wikipedia_data.html")[1]
    cities = cities.iloc[:-1, [0, 3, 5, 6, 7, 8]]

    nhl_df.drop([0, 9, 18, 26], 0, inplace=True)
    cities.drop([14, 15, 18, 19, 20, 21, 23, 24, 25, 27, 28, 32, 33, 38, 40, 41, 42, 44, 45, 46, 48, 49, 50], 0,
                inplace=True)

    l = []
    for i in cities['NHL']:
        i = i.split('[')
        l.append(i[0])
    cities['NHL'] = l

    li = []
    for i in nhl_df['team']:
        i = re.findall("[^*]+", i)
        li.append(i[0])
    nhl_df['team'] = li

    nhl_df = nhl_df.head(31)

    nhl_df['team_ville'] = nhl_df['team']
    nhl_df['team_ville'] = nhl_df['team_ville'].map({'Tampa Bay Lightning': 'Tampa Bay Area',
                                                     'Boston Bruins': 'Boston',
                                                     'Toronto Maple Leafs': 'Toronto',
                                                     'Florida Panthers': 'Miami–Fort Lauderdale',
                                                     'Detroit Red Wings': 'Detroit',
                                                     'Montreal Canadiens': 'Montreal',
                                                     'Ottawa Senators': 'Ottawa',
                                                     'Buffalo Sabres': 'Buffalo',
                                                     'Washington Capitals': 'Washington, D.C.',
                                                     'Pittsburgh Penguins': 'Pittsburgh',
                                                     'Philadelphia Flyers': 'Philadelphia',
                                                     'Columbus Blue Jackets': 'Columbus',
                                                     'New Jersey Devils': 'New York City',
                                                     'Carolina Hurricanes': 'Raleigh',
                                                     'New York Islanders': 'New York City',
                                                     'New York Rangers': 'New York City',
                                                     'Nashville Predators': 'Nashville',
                                                     'Winnipeg Jets': 'Winnipeg',
                                                     'Minnesota Wild': 'Minneapolis–Saint Paul',
                                                     'Colorado Avalanche': 'Denver',
                                                     'St. Louis Blues': 'St. Louis',
                                                     'Dallas Stars': 'Dallas–Fort Worth',
                                                     'Chicago Blackhawks': 'Chicago',
                                                     'Vegas Golden Knights': 'Las Vegas',
                                                     'Anaheim Ducks': 'Los Angeles',
                                                     'San Jose Sharks': 'San Francisco Bay Area',
                                                     'Los Angeles Kings': 'Los Angeles',
                                                     'Calgary Flames': 'Calgary',
                                                     'Edmonton Oilers': 'Edmonton',
                                                     'Vancouver Canucks': 'Vancouver',
                                                     'Arizona Coyotes': 'Phoenix'})

    df = pd.merge(nhl_df, cities, left_on="team_ville", right_on="Metropolitan area")

    df['W'] = pd.to_numeric(df['W'])
    df['L'] = pd.to_numeric(df['L'])
    df['Population (2016 est.)[8]'] = pd.to_numeric(df['Population (2016 est.)[8]'])

    he = ['team', 'W', 'L', 'Metropolitan area', 'Population (2016 est.)[8]']

    df = df[he]

    df['W/L'] = df['W'] / (df['L'] + df['W'])

    df = df.groupby('Metropolitan area').mean().reset_index()

    population_by_region = df['Population (2016 est.)[8]']  # pass in metropolitan area population from cities
    win_loss_by_region = df[
        'W/L']  # pass in win/loss ratio from nhl_df in the same order as cities["Metropolitan area"]

    assert len(population_by_region) == len(win_loss_by_region), "Q1: Your lists must be the same length"
    assert len(population_by_region) == 28, "Q1: There should be 28 teams being analysed for NHL"

    return stats.pearsonr(population_by_region, win_loss_by_region)[0]