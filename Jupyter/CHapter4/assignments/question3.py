

import pandas as pd
import scipy.stats as stats


def mlb_correlation():
    mlb_df = pd.read_csv("assets/mlb.csv")
    cities = pd.read_html("assets/wikipedia_data.html")[1]
    cities = cities.iloc[:-1, [0, 3, 5, 6, 7, 8]]
    cities.drop([24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50], 0,
                inplace=True)
    mlb_df = mlb_df.head(30)
    mlb_df['team_ville'] = mlb_df['team']
    mlb_df['team_ville'] = mlb_df['team_ville'].map({'Boston Red Sox': 'Boston',
                                                     'New York Yankees': 'New York City',
                                                     'Tampa Bay Rays': 'Tampa Bay Area',
                                                     'Toronto Blue Jays': 'Toronto',
                                                     'Baltimore Orioles': 'Baltimore',
                                                     'Cleveland Indians': 'Cleveland',
                                                     'Minnesota Twins': 'Minneapolis–Saint Paul',
                                                     'Detroit Tigers': 'Detroit',
                                                     'Chicago White Sox': 'Chicago',
                                                     'Kansas City Royals': 'Kansas City',
                                                     'Houston Astros': 'Houston',
                                                     'Oakland Athletics': 'San Francisco Bay Area',
                                                     'Seattle Mariners': 'Seattle',
                                                     'Los Angeles Angels': 'Los Angeles',
                                                     'Texas Rangers': 'Dallas–Fort Worth',
                                                     'Atlanta Braves': 'Atlanta',
                                                     'Washington Nationals': 'Washington, D.C.',
                                                     'Philadelphia Phillies': 'Philadelphia',
                                                     'New York Mets': 'New York City',
                                                     'Miami Marlins': 'Miami–Fort Lauderdale',
                                                     'Milwaukee Brewers': 'Milwaukee',
                                                     'Chicago Cubs': 'Chicago',
                                                     'St. Louis Cardinals': 'St. Louis',
                                                     'Pittsburgh Pirates': 'Pittsburgh',
                                                     'Cincinnati Reds': 'Cincinnati',
                                                     'Los Angeles Dodgers': 'Los Angeles',
                                                     'Colorado Rockies': 'Denver',
                                                     'Arizona Diamondbacks': 'Phoenix',
                                                     'San Francisco Giants': 'San Francisco Bay Area',
                                                     'San Diego Padres': 'San Diego'})

    df3 = pd.merge(mlb_df, cities, left_on="team_ville", right_on="Metropolitan area")
    df3['W'] = pd.to_numeric(df3['W'])
    df3['L'] = pd.to_numeric(df3['L'])
    df3['Population (2016 est.)[8]'] = pd.to_numeric(df3['Population (2016 est.)[8]'])
    he = ['team', 'W', 'L', 'Metropolitan area', 'Population (2016 est.)[8]']
    df3 = df3[he]
    df3['W/L'] = df3['W'] / (df3['L'] + df3['W'])
    df3 = df3.groupby('Metropolitan area').mean().reset_index()
    population_by_region = df3['Population (2016 est.)[8]']  # pass in metropolitan area population from cities
    win_loss_by_region = df3[
        'W/L']  # pass in win/loss ratio from mlb_df in the same order as cities["Metropolitan area"]
    assert len(population_by_region) == len(win_loss_by_region), "Q3: Your lists must be the same length"
    assert len(population_by_region) == 26, "Q3: There should be 26 teams being analysed for MLB"

    return stats.pearsonr(population_by_region, win_loss_by_region)[0]