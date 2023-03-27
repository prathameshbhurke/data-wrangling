"""
The data set is imported from Kaggle.
https://www.kaggle.com/datasets/devinanzelmo/dota-2-matches
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


matches_df=pd.read_csv('/Users/reshmabanaganapalli/Documents/Python_projects/dota/match.csv')
#print(matches_df)

#Define Meta Data:
'''
match_id: A unique identifier for the match.
start_time: The start time of the match in Unix time format.
duration: The duration of the match in seconds.
tower_status_radiant: A binary code representing the status of Radiant team's towers at the end of the match.
tower_status_dire: A binary code representing the status of Dire team's towers at the end of the match.
barracks_status_dire: A binary code representing the status of Dire team's barracks at the end of the match.
barracks_status_radiant: A binary code representing the status of Radiant team's barracks at the end of the match.
first_blood_time: The time in seconds when the first blood occurred in the match.
game_mode: An integer code representing the game mode of the match.
radiant_win: A boolean value representing whether the Radiant team won the match or not.
negative_votes: The number of negative votes the match received from players.
positive_votes: The number of positive votes the match received from players.
cluster: An integer code representing the cluster or region where the match was played.
'''

#check row count and columns
#print(matches_df.shape)

#print(matches_df.info())

matches_df[['duration','first_blood_time']] =  matches_df[['duration','first_blood_time']].apply(lambda x:round(x/60,2))


matches_df.drop(['start_time','tower_status_radiant','tower_status_dire','game_mode','barracks_status_dire'],axis=1,inplace=True)


players_df = pd.read_csv('/Users/reshmabanaganapalli/Documents/Python_projects/dota/players.csv')


#players_df.info()

players_df=players_df.drop(["item_0", "item_1", "item_2", "item_3","item_4", "item_5", "level", "leaver_status", "xp_hero", "xp_creep","xp_roshan", "xp_other", "gold_other", "gold_death", "gold_buyback",       "gold_abandon", "gold_sell", "gold_destroying_structure",       "gold_killing_heros", "gold_killing_creeps", "gold_killing_roshan",
       "gold_killing_couriers", "unit_order_none","unit_order_move_to_position", "unit_order_move_to_target","unit_order_attack_move", "unit_order_attack_target",
       "unit_order_cast_position", "unit_order_cast_target","unit_order_cast_target_tree", "unit_order_cast_no_target",
       "unit_order_cast_toggle", "unit_order_hold_position","unit_order_train_ability","unit_order_drop_item","unit_order_give_item", "unit_order_pickup_item",
       "unit_order_pickup_rune", "unit_order_purchase_item","unit_order_sell_item", "unit_order_disassemble_item","unit_order_move_item", "unit_order_cast_toggle_auto",
       "unit_order_stop", "unit_order_taunt", "unit_order_buyback","unit_order_glyph","unit_order_eject_item_from_stash",
       "unit_order_cast_rune", "unit_order_ping_ability","unit_order_move_to_direction", "unit_order_patrol",
       "unit_order_vector_target_position", "unit_order_radar","unit_order_set_item_combine_lock", "unit_order_continue",'player_slot'],axis=1)


dota = players_df.merge(matches_df,on='match_id')

hero_names_df=pd.read_csv('/Users/reshmabanaganapalli/Documents/Python_projects/dota/hero_names.csv')

dota =  dota.merge(hero_names_df, on='hero_id')

dota.drop(['name'],axis=1,inplace=True)

avg_gold_per_hero = dota.groupby('localized_name')['gold_per_min'].mean()

sorted_gold_per_hero  = avg_gold_per_hero.sort_values(ascending=False)

sorted_gold_per_hero.head(10).plot(kind = 'bar', title = 'Heros gold per minute', xlabel = 'Hero Name',ylabel = 'Avg gold per min')