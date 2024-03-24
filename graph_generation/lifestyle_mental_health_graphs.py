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

df_pa = df_pa = pd.read_csv('professional_activities.csv')
df_social = pd.read_csv('social.csv')
df_st = pd.read_csv('syde_traditions.csv')
df_relationships = pd.read_csv('relationships.csv')
df_wild = pd.read_csv('wild.csv')

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

#### Create syde events stacked bar #######
syde_events_list = [
    'syde_event_1a',
    'syde_event_1b',
    'syde_event_2a',
    'syde_event_2b',
    'syde_event_3a',
    'syde_event_4a',
    'syde_event_4b'
]
df_syde_events = df_st[syde_events_list].copy()

graphs.create_bar_stacked(
    df_syde_events,
    syde_events_list,
    'Term',
    'Percentage of class',
    'Did you attend a SYDE event in these terms?',
    display_as_percentage = True,
    vertical = False,
    column_labels = ['1A', '1B', '2A', '2B', '3A', '4A', '4B'],
    file_name = 'syde_event_attendance'
)
#### END: create syde events stacked bar #############

#### Create serious relationships bar #######3
def clean_sr(value):
    if(value == '0.5 lol'):
        return 0
    else:
        return int(value)
df_sr = df_relationships[['serious_relationships']]
df_sr = df_sr.dropna()
df_sr['serious_relationships'] = df_sr['serious_relationships'].apply(clean_sr)

graphs.create_bar(
    df_sr,
    'serious_relationships',
    'Number of relationships',
    'Percentage of respondents',
    'How many serious relationships have you been in',
    vertical = True,
    display_as_percentage=5,
    values_increment = 5
)
#### END create serious relationships bar ##########

#### Create serious relationships meet bar
def clean_sr_meet(value):
    if('Extracurriculars (includes school clubs, design teams, external groups, etc.)' in value):
        value = value.replace('Extracurriculars (includes school clubs, design teams, external groups, etc.)', 'Extracurriculars')
    return value
df_sr_meet = df_relationships[['serious_relationships_meet']]
df_sr_meet = df_sr_meet.dropna()
df_sr_meet['serious_relationships_meet'] = df_sr_meet['serious_relationships_meet'].apply(clean_sr_meet)

graphs.create_bar(
    df_sr_meet,
    'serious_relationships_meet',
    'Methods of meeting significant other',
    'Number of respondents',
    'How did you meet your partner in serious relationships',
    vertical = False,
    splice_required = True,
)
#### END: Create serious relationships meet bar

#### create sydecest pie #########
df_sydecest = df_relationships[['sydecest']]
df_sydecest

graphs.create_pie(
    df_sydecest,
    'sydecest',
    'Did you engage in sydecest',
    percent_text_distance = 1.2,
    labels = ['Yes', 'No']
)
#### END: create sydecest pie ##########

#### create sydecest wishful pie ######
df_sydecest_wish = df_relationships[['sydecest', 'sydecest_wishful']]
df_sydecest_wish = df_sydecest_wish.dropna()
df_sydecest_wish = df_sydecest_wish.loc[df_sydecest_wish['sydecest'] == 'No']

graphs.create_pie(
    df_sydecest_wish,
    'sydecest_wishful',
    'If you did not engage in sydecest, did you want to?',
    percent_text_distance = 1.2,
    labels = ['Yes', 'No']
)
#### END: create sydecest wishful pie ########

#### create alcohol category traversal line
list_alcohol = ['alcohol_1a',
 'alcohol_c1',
 'alcohol_1b',
 'alcohol_c2',
 'alcohol_2a',
 'alcohol_c3',
 'alcohol_2b',
 'alcohol_c4',
 'alcohol_3a',
 'alcohol_c5',
 'alcohol_3b',
 'alcohol_c6',
 'alcohol_4a',
 'alcohol_4b']

df_alcohol = df_wild[list_alcohol]

graphs.create_line_category_traversal(
    df_alcohol,
    list_alcohol,
    'Term',
    'Frequency of alcohol usage',
    'How often did you consume alcohol each term',
    'alcohol_consumption',
    ['Never', 'Once or twice a term', 'Monthly', 'Biweekly', 'Weekly', '2 - 3 times a week', '4 - 7 times a week'],
    only_show_average = True,
    sequential_label_rotation_angle = 45,
    sequential_label_names = helpers.get_study_coop_term_list()
)
#### END: create alcohol category traversal line #####

#### create weed category traversal line
list_weed = [
    'weed_1a',
    'weed_c1',
    'weed_1b',
    'weed_c2',
    'weed_2a',
    'weed_c3',
    'weed_2b',
    'weed_c4',
    'weed_3a',
    'weed_c5',
    'weed_3b',
    'weed_c6',
    'weed_4a',
    'weed_4b'
]

df_weed = df_wild[list_weed]

graphs.create_line_category_traversal(
    df_weed,
    list_weed,
    'Term',
    'Frequency of marijuana usage',
    'How often did you consume marijuana each term',
    'weed_consumption',
    ['Never', 'Once or twice a term', 'Monthly', 'Biweekly', 'Weekly', '2 - 3 times a week', '4 - 7 times a week'],
    only_show_average = True,
    sequential_label_rotation_angle = 45,
    sequential_label_names = helpers.get_study_coop_term_list()
)
#### END: create weed category traversal line ######

#### create party category traversal line ######
list_party = [
    'party_1a',
    'party_1b',
    'party_2a',
    'party_2b',
    'party_3a',
    'party_3b',
    'party_4a',
    'party_4b',
]

df_party = df_wild[list_party]

graphs.create_line_category_traversal(
    df_party,
    list_party,
    'Term',
    'Frequency of partying',
    'How often did you party each term',
    'partying',
    ['Never', 'Once or twice a term', 'Monthly', 'Biweekly', 'Weekly', '2 - 3 times a week', '4 - 7 times a week'],
    only_show_average = True,
    sequential_label_rotation_angle = 45,
    sequential_label_names = helpers.get_study_term_list()
)
#### END: create party category traversal line ########

#### Create milestone bar #######
df_milestones = df_wild[['hye_milestones']]
df_milestones = df_milestones.dropna()

graphs.create_bar(
    df_milestones,
    'hye_milestones',
    'Milestones',
    'Number of respondents',
    'Which of the following have you participated in',
    vertical = True,
    splice_required = True,
    figure_width = 22,
    max_label_length = 45,
    title_label_rotation_angle = 45,
)
#### END: create milestone bar