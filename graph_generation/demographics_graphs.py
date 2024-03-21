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

df_before_syde = pd.read_csv('csv/before_syde.csv')
df_household = pd.read_csv('../csv/final/split/household.csv')
df_high_school = pd.read_csv('../csv/final/split/high_school.csv')

## HOW DID YOU HEAR ABOUT SYDE
graphs.create_bar(
    df_before_syde, 
    'hear_about_syde', 
    'Option', 
    'Percentage of Respondents', 
    'How did you hear about SYDE?',
    False,
    display_as_percentage=True,
    values_increment=5,
    convert_to_string=True,
)
#### END: how did you hear about SYDE

#### household income #####
df_income = df_household[['household_income']]
df_income = df_income.dropna()

income_list = [
    '$1 - $25 000',
    '$25 001 - $50 000',
    '$50 001 - $75 000',
    '$75 001 - $100 000',
    '$100 001 - $150 000',
    '$150 001 - $200 000',
    '$200 001 - $250 000',
    '$250 001 - $300 000',
    '$300 000 +',
    'Unsure',
    'Prefer not to say'
]

graphs.create_bar(
    df_income,
    'household_income',
    'Household Income (CAD)',
    'Percentage of respondents',
    'What was your household income in 2018',
    vertical = True,
    display_as_percentage = True,
    labels = income_list,
    title_label_rotation_angle=45
)

def group_lower_income(value):
    if(value == '$1 - $25 000' or value == '$25 001 - $50 000'):
        return '$1 - $50 000'
    elif(value == '$50 001 - $75 000' or value == '$75 001 - $100 000'):
        return '$50 001 - $100 000'
    return value

df_income_grouped = df_household[['household_income']].copy()
df_income_grouped = df_income_grouped.dropna()
df_income_grouped['household_income'] = df_income_grouped['household_income'].apply(group_lower_income)

income_grouped_list = [
    '$1 - $50 000',
    '$50 001 - $100 000',
    '$100 001 - $150 000',
    '$150 001 - $200 000',
    '$200 001 - $250 000',
    '$250 001 - $300 000',
    '$300 000 +',
    'Unsure',
    'Prefer not to say'
]

graphs.create_bar(
    df_income_grouped,
    'household_income',
    'Household Income (CAD)',
    'Percentage of respondents',
    'What was your household income in 2018',
    vertical = True,
    display_as_percentage = True,
    labels = income_grouped_list,
    title_label_rotation_angle=45
)
#### END: household income ######

#### create education parents #########
def clean_edu_parents(value):
    if(value == 'Professional Degree (JD, MD, etc.)'):
        return 'Professional Degree'
    elif(value == 'High school diploma or equivalent'):
        return 'High School Diploma'
    return value

df_edu_parents = df_household[['edu_parents']].copy()
df_edu_parents = df_edu_parents.dropna()
df_edu_parents['edu_parents'] = df_edu_parents['edu_parents'].apply(clean_edu_parents)
df_edu_parents['edu_parents'].unique().tolist()

edu_parents_list = [
    'Less than high school',
    'High School Diploma',
    'Diploma',
    "Associate's Degree",
    "Bachelor's Degree",
    "Master's Degree",
    'Doctoral Degree (PhD)',
    'Professional Degree'
]

graphs.create_bar(
    df_edu_parents,
    'edu_parents',
    'Level of Education Achieved',
    'Percentage of respondents',
    'What was the highest level attained by your parents',
    vertical = True,
    display_as_percentage = True,
    labels = edu_parents_list,
    title_label_rotation_angle=30
)
#### END: create education parents #########

#### create parents stem eng ######
df_stem_eng = df_household[['stem_edu_parents', 'eng_parents']]
df_stem_eng = df_stem_eng.dropna()

graphs.create_bar_stacked(
    df_stem_eng,
    ['stem_edu_parents', 'eng_parents'],
    '',
    'Percentage of respondents',
    'Your Parents with STEM and Engineering',
    labels = ['Yes', 'No'],
    column_labels = ['Did any of your parents study STEM', 'Do any of your parents work in engineering'],
    figure_height = 4,
    display_as_percentage = True
)
#### END: create parents stem eng ######

#### admission average #########
df_ad_avg = df_high_school[['admission_average']].copy()
df_ad_avg = df_ad_avg.dropna()
df_ad_avg['admission_average'] = df_ad_avg['admission_average'].map(lambda x: math.floor(x))
df_ad_avg = df_ad_avg.loc[df_ad_avg['admission_average'] != 9]

graphs.create_bar(
    df_ad_avg,
    'admission_average',
    'Admission Average (%)',
    'Percentage of class',
    'What was your admission average in high school',
    vertical = True,
    display_as_percentage = True,
    labels = list(np.arange(89, 100, 1)),
    graph_name_labels = list(np.arange(89, 100, 1))
)
#### END: admission average ############

#### high school specialized programs
df_hs_spec_programs = df_high_school[['hs_spec_programs']]
df_hs_spec_programs = df_hs_spec_programs.dropna()
df_hs_spec_programs = df_hs_spec_programs[df_hs_spec_programs['hs_spec_programs'] != 'None']

graphs.create_bar(
    df_hs_spec_programs,
    'hs_spec_programs',
    'Specialized Programs',
    'Number of responses',
    'Were you enrolled in any specialized programs while in High School',
    vertical = False,
    splice_required = True
)
#### END: high school specialized programs