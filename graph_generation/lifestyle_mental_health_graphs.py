# necessary imports
import numpy as np                # use for array and matrix stuff
import pandas as pd               # use for dataframes, think of it as excel
import math
import matplotlib.pyplot as plt   # use to make graphs
import seaborn as sns
from collections import Counter
# import helpers
import graphs
import functools

df = pd.read_csv('')
df1 = pd.read_csv('')

df_pa = df_pa = pd.read_csv('professional_activities.csv')

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