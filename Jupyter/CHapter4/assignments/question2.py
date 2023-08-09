import pandas as pd
import scipy.stats as stats



def nba_correlation():


    nba_df = pd.read_csv("assets/nba.csv")
    cities = pd.read_html("assets/wikipedia_data.html")[1]
    cities = cities.iloc[:-1, [0, 3, 5, 6, 7, 8]]

    cities.drop([16, 17, 19, 20, 21, 22, 23, 26, 29, 30, 31, 34, 35, 36, 37, 39, 40, 43, 44, 47, 48, 49, 50], 0,
                inplace=True)

    l1 = []
    for i in nba_df['team']:
        # i=i.rstrip()
        i = i.split('*')
        l1.append(i[0])
    nba_df['team'] = l1

    l2 = []
    for i in nba_df['team']:
        i = i.split('(')
        l2.append(i[0])
    nba_df['team'] = l2

    l3 = []
    for i in nba_df['team']:
        i = i.rstrip()
        l3.append(i)
    nba_df['team'] = l3

    nba_df = nba_df.head(30)

    nba_df['team_ville'] = nba_df['team']
    nba_df['team_ville'] = nba_df['team_ville'].map({'Toronto Raptors': 'Toronto',
                                                     'Boston Celtics': 'Boston',
                                                     'Philadelphia 76ers': 'Philadelphia',
                                                     'Cleveland Cavaliers': 'Cleveland',
                                                     'Indiana Pacers': 'Indianapolis',
                                                     'Miami Heat': 'Miami–Fort Lauderdale',
                                                     'Milwaukee Bucks': 'Milwaukee',
                                                     'Washington Wizards': 'Washington, D.C.',
                                                     'Detroit Pistons': 'Detroit',
                                                     'Charlotte Hornets': 'Charlotte',
                                                     'New York Knicks': 'New York City',
                                                     'Brooklyn Nets': 'New York City',
                                                     'Chicago Bulls': 'Chicago',
                                                     'Orlando Magic': 'Orlando',
                                                     'Atlanta Hawks': 'Atlanta',
                                                     'Houston Rockets': 'Houston',
                                                     'Golden State Warriors': 'San Francisco Bay Area',
                                                     'Portland Trail Blazers': 'Portland',
                                                     'Oklahoma City Thunder': 'Oklahoma City',
                                                     'Utah Jazz': 'Salt Lake City',
                                                     'New Orleans Pelicans': 'New Orleans',
                                                     'San Antonio Spurs': 'San Antonio',
                                                     'Minnesota Timberwolves': 'Minneapolis–Saint Paul',
                                                     'Denver Nuggets': 'Denver',
                                                     'Los Angeles Clippers': 'Los Angeles',
                                                     'Los Angeles Lakers': 'Los Angeles',
                                                     'Sacramento Kings': 'Sacramento',
                                                     'Dallas Mavericks': 'Dallas–Fort Worth',
                                                     'Memphis Grizzlies': 'Memphis',
                                                     'Phoenix Suns': 'Phoenix'})

    df2 = pd.merge(nba_df, cities, left_on="team_ville", right_on="Metropolitan area")

    df2['W/L%'] = pd.to_numeric(df2['W/L%'])
    df2['W'] = pd.to_numeric(df2['W'])
    df2['L'] = pd.to_numeric(df2['L'])
    df2['Population (2016 est.)[8]'] = pd.to_numeric(df2['Population (2016 est.)[8]'])
    he = ['team', 'W', 'L', 'W/L%', 'Metropolitan area', 'Population (2016 est.)[8]']
    df2 = df2[he]
    df2['W/L'] = df2['W'] / (df2['L'] + df2['W'])
    df2 = df2.groupby('Metropolitan area').mean().reset_index()

    population_by_region = df2['Population (2016 est.)[8]']
    win_loss_by_region = df2[
        'W/L']

    assert len(population_by_region) == len(win_loss_by_region), "Q2: Your lists must be the same length"
    assert len(population_by_region) == 28, "Q2: There should be 28 teams being analysed for NBA"

    return stats.pearsonr(population_by_region, win_loss_by_region)[0]