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

