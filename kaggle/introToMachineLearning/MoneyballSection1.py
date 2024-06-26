#@title Run this to download data and prepare our environment!
import numpy as np
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

# Get Sean Lahman teams dataset, which contains data on team performance all the way back to 1871
teams = pd.read_csv("https://drive.google.com/uc?id=1kbfBhzHNqfg4Af81mdGRTyMKPt1kCGUu")

# Focus on most recent 50 years of data, and ignore seasons shortened by strikes and the pandemic
#Credit: John Basbagill; thanks for poining these years out!
teams = teams.loc[(teams["yearID"] > 1972)  &
                  (teams["yearID"] != 1981) &
                  (teams["yearID"] != 1994) &
                  (teams["yearID"] != 2020)]

# Remove irrelevant columns
columns_to_drop =  [
                    # team IDs in other datasets
                    'teamIDBR', 'teamIDlahman45', 'teamIDretro',

                    # IDs for franchise, division, league
                    'franchID', 'divID', 'lgID',

                    # other success metrics
                    'DivWin', 'WCWin', 'LgWin', 'WSWin', 'Rank',

                    # Batting/Pitching Park Factor and related features
                    'BPF', 'PPF', 'Ghome', 'park', 'attendance',

                    # more batting stats
                    'SB', 'CS', 'SO',

                    # misc defense/pitching stats
                    'ER', 'E', 'CG', 'SHO', 'SV', 'IPouts', 'DP', 'FP',
                    'ERA', 'RA', 'HA', 'HRA', 'BBA', 'SOA'
                    ]
teams = teams.drop(columns=columns_to_drop)

# Rename columns to be more descriptive
abbrev_map = {
    "R" : "Runs",

    "AB" : "AtBats",

    "H" : "Hits",
    "2B" : "Doubles",
    "3B" : "Triples",
    "HR" : "HomeRuns",

    "BB" : "Walks",
    "HBP" : "HitsByPitch",
    "SF" : "SacrificeFlies",

    "W" : "Wins",
    "L" : "Losses",
    "G" : "Games",
}
teams = teams.rename(columns=abbrev_map)

# Move team name column
teams.insert(teams.columns.get_loc('teamID') + 1, 'Name',
              teams.pop("name"))

teams.reset_index(inplace=True, drop=True)


teams["BattingAverage"] = teams["Hits"]/teams["AtBats"]

teams['Singles'] = teams['Hits'] - teams['Doubles'] - teams['Triples'] - teams['HomeRuns']
teams['TotalBases'] = (teams['Singles'] + (2 * teams['Doubles']) + (3 * teams['Triples']) + (4 * teams['HomeRuns']))

teams['SluggingPercentage'] = teams['TotalBases'] / teams['AtBats']

teams['OnBasePercentage'] = (teams['Hits'] + teams['Walks'] + teams['HitsByPitch']) / (teams['AtBats'] + teams['Walks'] + teams['HitsByPitch'] + teams['SacrificeFlies'])

teams['WinPercentage'] = teams['Wins'] / teams['Games']

import pandas as pd
import matplotlib.pyplot as plt
import ipywidgets as widgets
from ipywidgets import interact

# Function to plot team progression over time by a given feature
def plot_team_progression(team, feature):
    plt.figure(figsize=(12, 8))
    team_data = teams[teams['teamID'] == team]
    plt.plot(team_data['yearID'], team_data[feature], marker='o', label=team_data['Name'].iloc[0])

    plt.title(f'{team_data["Name"].iloc[0]} Progression Over Time by {feature}')
    plt.xlabel('Year')
    plt.ylabel(feature)
    plt.legend()
    plt.grid(True)

# Interactive widgets
team_selector = widgets.Dropdown(
    options=teams['teamID'].unique(),
    description='Team:'
)

feature_selector = widgets.Dropdown(
    options=['Games', 'Wins', 'Losses', 'Runs', 'AtBats', 'Hits', 'Doubles', 'Triples', 'HomeRuns', 'Walks', 'HitsByPitch', 'SacrificeFlies', 'BattingAverage', 'Singles', 'SluggingPercentage', 'OnBasePercentage'],
    description='Feature:'
)

# Display interactive plot
interact(plot_team_progression, team=team_selector, feature=feature_selector)

plt.subplots(1, 3, figsize=(15, 5), sharey=True)

plt.subplot(1,3,1)
sns.scatterplot(x="BattingAverage", y = "WinPercentage", data=teams)

plt.subplot(1,3,2)
sns.scatterplot(x="SluggingPercentage", y = "WinPercentage", data=teams)

plt.subplot(1,3,3)
sns.scatterplot(x="OnBasePercentage", y = "WinPercentage", data=teams)

correlationMatrix = teams.corr(numeric_only=True)

plt.figure(figsize=(10, 8))
sns.heatmap(correlationMatrix, annot=True, cmap='coolwarm', linewidths=.5, annot_kws={"size": 6})
plt.title('Correlation Matrix Heatmap')

correlationMatrix["WinPercentage"].sort_values()

for column_name in ['BattingAverage', 'SluggingPercentage', 'OnBasePercentage']:
  sns.histplot(x=column_name, data=teams, label=column_name)

plt.xlabel('')
plt.legend(fontsize='small')
plt.show()