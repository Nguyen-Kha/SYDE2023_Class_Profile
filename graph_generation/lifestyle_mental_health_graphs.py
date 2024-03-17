# necessary imports
import numpy as np                # use for array and matrix stuff
import pandas as pd               # use for dataframes, think of it as excel
import math
import matplotlib.pyplot as plt   # use to make graphs
import seaborn as sns
from collections import Counter
import helpers
import graphs
import functools

df = pd.read_csv('')
df1 = pd.read_csv('')

df_pa = df_pa = pd.read_csv('professional_activities.csv')
df_social = pd.read_csv('social.csv')

#### Create disciplines of interest bar #####################
df_disciplines = df_pa[['disciplines_of_interest']]
df_disciplines = df_disciplines.dropna()

graphs.create_bar(
    df_disciplines,
    'disciplines_of_interest',
    'Disciplines',
    'Number of respondents',
    'What are your disciplines of interest',
    vertical = False,
    splice_required = True,
    figure_height = 12,
    max_label_length = 30,
)
#### END: Create disciplines of interest bar ################

#### Create cali or bust bar ################
def clean_cali_or_bust(answer):
    if("busted" in answer.lower() and "cali" in answer.lower()):
        return "Yes Cali-ed, Yes Busted"
    elif("busted" in answer.lower()):
        return "Yes Busted"
    elif("cali" in answer.lower()):
        return "Yes Cali-ed"
    
    return "No"
df_cali_bust = df_pa[['cali_or_bust']]
df_cali_bust = df_cali_bust.dropna()
df_cali_bust['cali_or_bust'] = df_cali_bust['cali_or_bust'].apply(clean_cali_or_bust)

graphs.create_bar(
    df_cali_bust,
    'cali_or_bust',
    'Cali?',
    'Number of Respondents',
    'Did you Cali or bust?',
    vertical = True,
    splice_required = True,
    figure_width = 7,
    labels = ['Yes Cali-ed','Yes Busted', 'No'],
    graph_name_labels = ['Yes, Cali-ed', 'Yes, Busted', 'No']
)
#### END: Create cali or bust bar ###############

#### create friends in undergrad bar ##############
df_friends_ug = df_social[['friends_undergrad']].copy()
df_friends_ug['friends_undergrad'] = df_friends_ug['friends_undergrad'].apply(helpers.turn_dates_into_actual_values)
df_friends_ug = df_friends_ug.dropna()

friends_undergrad_list = ['0', '1 - 5', '6 - 10', '11 - 15', '16 - 20', '21 - 25', '26 - 30', '30+']

graphs.create_bar(
    df_friends_ug,
    'friends_undergrad',
    'Number of friends in undergrad',
    'Percentage of Respondents',
    'How many friends did you have in undergrad?',
    vertical = True,
    display_as_percentage = True,
    labels = friends_undergrad_list,
    values_increment = 5
)
#### END: create friends in undergrad bar #############

#### Create friends in syde bar ###############
def bin_friends_syde(value):
    value = int(value)
    if(value == 0):
        return '0'
    elif(value >= 1 and value <= 5):
        return '1 - 5'
    elif(value >= 6 and value <= 10):
        return '6 - 10'
    elif(value >= 11 and value <= 15):
        return '11 - 15'
    elif(value >= 16 and value <= 20):
        return '16 - 20'
    elif(value >= 21 and value <= 25):
        return '21 - 25'
    elif(value >= 26 and value <= 30):
        return '26 - 30'
    else:
        return '30+'
    

df_friends_syde = df_social[['friends_syde']].copy()
df_friends_syde = df_friends_syde.dropna()
df_friends_syde['friends_syde'] = df_friends_syde['friends_syde'].apply(helpers.remove_nonnumeric_char)
df_friends_syde['friends_syde'] = df_friends_syde['friends_syde'].apply(bin_friends_syde)

friends_syde_list = ['0', '1 - 5', '6 - 10', '11 - 15', '16 - 20', '21 - 25', '26 - 30', '30+']

graphs.create_bar(
    df_friends_syde,
    'friends_syde',
    'Number of friends in syde',
    'Percentage of Respondents',
    'How many friends did you have in SYDE?',
    vertical = True,
    display_as_percentage = True,
    labels = friends_syde_list,
    values_increment = 5
)
#### END: create friends in syde bar ################

#### Create closest 5 friends in syde bar #############
df_friends_syde_5 = df_social[['friends_syde_5']].copy()
df_friends_syde_5 = df_friends_syde_5.dropna()

graphs.create_bar(
    df_friends_syde_5,
    'friends_syde_5',
    'Number of closest friends in syde',
    'Percentage of Respondents',
    'Of your 5 closest friends, how many of them are in SYDE',
    vertical = True,
    display_as_percentage = True,
    values_increment = 5
)
#### END: create closest 5 friends in syde bar ##########

#### Create clique bar #########
df_clique = df_social[['clique']].copy()
df_clique = df_clique.dropna()

graphs.create_bar(
    df_clique,
    'clique',
    'Cliquiness response',
    'Percentage of Respondents',
    'State your level of agreement: Our SYDE cohort was cliquey',
    vertical = True,
    display_as_percentage = True,
    values_increment = 5,
    labels = helpers.get_agree_scale()
)
#### END: create clique bar ##########
