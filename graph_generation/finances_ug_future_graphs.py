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

df_finance = pd.read_csv('../csv/final/split/finances.csv')
df_ug_reflections = pd.read_csv('../csv/final/split/undergrad_reflections.csv')

#### Create debt bar ############3
def bin_debt(value):
    if(value == 0):
        return '0'
    elif(value > 0 and value <= 10000):
        return '1 - 10 000'
    elif(value > 10000.01 and value <= 20000):
        return '10 001 - 20 000'
    elif(value > 20000.01 and value <= 30000):
        return '20 001 - 30 000'
    elif(value > 30000.01 and value <= 40000):
        return '30 001 - 40 000'
    elif(value > 40000):
        return '40 000 +'
    
df_bin_debt = df_finance[['debt']].copy()
df_bin_debt = df_bin_debt.dropna()
df_bin_debt['debt'] = df_bin_debt['debt'].apply(bin_debt)
bin_debt_list = ['0', '1 - 10 000', '10 001 - 20 000', '20 001 - 30 000', '30 001 - 40 000', '40 000 +']

graphs.create_bar(
    df_bin_debt,
    'debt',
    'Amount of debt (CAD)',
    'Percentage of respondents',
    'How much debt are you graduating with',
    vertical = True,
    display_as_percentage = True,
    labels = bin_debt_list,
    values_increment = 5
)
#### END: create debt bar ####################3

#### create tuition bar ###########33
df_tuition = df_finance[['tuition_self_fund']].copy()
df_tuition = df_tuition.dropna()
tuition_list = ['0%', '1% - 20%', '21% - 40%', '41% - 60%', '61% - 80%', '80% - 99%', '100%']

graphs.create_bar(
    df_tuition,
    'tuition_self_fund',
    'Percent of tuition that YOU paid',
    'Percentage of respondents',
    'How much of tuition did you pay for on your own?',
    vertical = True,
    display_as_percentage = True,
    labels = tuition_list,
    values_increment = 5
)
#### END: create tuition bar #############

#### create choose syde again pie #######
df_syde_again = df_ug_reflections[['syde_again']]
df_syde_again = df_syde_again.dropna()

graphs.create_pie(
    df_syde_again,
    'syde_again',
    'If you went back in time, would you have chosen SYDE again',
    percent_text_distance=1.2
)
#### END: create choose syde again pie