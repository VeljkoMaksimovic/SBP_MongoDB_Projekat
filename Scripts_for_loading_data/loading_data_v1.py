# Loading data so that we have list of gameweeks, each gameweek document will have a list of player statistics for
# that gameweek

import os
import pandas as pd
import pymongo


data_dir = '../Fantasy-Premier-League-master/data/'
seasons = ['2016-17', '2017-18', '2018-19', '2019-20']

client = pymongo.MongoClient()
db = client['FPL_Database_v1']
for season in seasons:
    print(season)
    season_collection = db[season]
    gameweek_to_players = {}
    for i in range(1, 39):
        gameweek_to_players[i] = []
    # In our gameweek .csv that we are going to use we have all of the information that we need except for the player
    # position. We are going to get that info by parsing 'players_raw.csv', and store it in a player to position dict
    player_to_position_dict = {}
    data = pd.read_csv(data_dir + season + '/players_raw.csv', usecols=['element_type', 'first_name', 'second_name'])
    for _, row in data.iterrows():
        player_to_position_dict[row['first_name'] + ' ' + row['second_name']] = row['element_type']
    # Going through each player in 'players' subfolder and and creating a object that represents their performance for
    # each gameweek
    players_dir = data_dir + season + '/players/'
    player_subfolders = os.listdir(players_dir)
    test = 5
    for player in player_subfolders:
        player_data = pd.read_csv(players_dir + player + '/gw.csv',
                                  usecols=['assists',  'goals_conceded', 'goals_scored', 'ict_index', 'creativity',
                                           'threat', 'influence', 'minutes', 'red_cards', 'yellow_cards', 'round',
                                           'selected', 'total_points', 'was_home', 'value', 'transfers_in',
                                           'transfers_out'])
        # Our data source is not uniform for all 4 seasons. Some player folders have id number at the end of their
        # name, and some dont, so we need to do a bit of preprocessing
        name = ''.join(i for i in player if not i.isdigit()).replace('_', ' ').strip()
        try:
            position = player_to_position_dict[name]
        except KeyError:
            print('Name ' + name + ' does not exist in players_raw.csv')
            continue

        for _, row in player_data.iterrows():
            gameweek_to_players[row['round']].append({
                'complex_stats': {
                    'creativity': row['creativity'],
                    'influence': row['influence'],
                    'threat': row['threat'],
                    'ict_index': row['ict_index']
                },
                'transfers': {
                    'in': row['transfers_in'],
                    'out': row['transfers_out']
                },
                'name': name,
                'position': position,
                'value': row['value'],
                'assists': row['assists'],
                'minutes': row['minutes'],
                'selected': row['selected'],
                'goals_scored': row['goals_scored'],
                'goals_conceded': row['goals_conceded'],
                'red_cards': row['red_cards'],
                'yellow_cards': row['yellow_cards'],
                'was_home': row['was_home'],
                'total_points': row['total_points']
            })

    all_gameweeks = [{'gw': gw, 'players': gameweek_to_players[gw]} for gw in gameweek_to_players]
    season_collection.insert_many(all_gameweeks)
    # We have to delete the list because pymongo uses object_id as document_id in its database, so inserting the
    # same list more than once will cause BulkWriteError
    # del all_player_jsons

