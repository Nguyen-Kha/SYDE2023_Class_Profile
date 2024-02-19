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

df_join_year = df[['join_year']]
df_join_year = df_join_year.dropna(axis=0)
graphs.create_pie(df_join_year, 'join_year', 'Year you joined the SYDE 2023 cohort', ['1A (Fall 2018)', '1B (Spring 2019)', '3B (Winter 2022)'])

df_years_complete_degree = df[['years_complete_degree']].dropna(axis=0)
graphs.create_pie(df_years_complete_degree, 'years_complete_degree', 'How many years it took for you to complete the degree')

df_race = df[['race']].dropna(axis=0)
graphs.create_bar(
    df_race, 
    'race', 
    'Ethnic bacakground of respondent', 
    'Percentage of class', 
    'What is your ethnic background', 
    True,
    splice_required = True, 
    display_as_percentage = True,
    rotation_angle = 45
)

df_birth_year = df[['birth_year']].dropna(axis = 0)
graphs.create_pie(df_birth_year, 'birth_year', 'In which year were you born?', labels = [1998, 1999, 2000, 2001])

df_gender = df[['gender']].dropna(axis=0)
graphs.create_bar(
    df_gender, 
    'gender', 
    'gender', 
    'Percentage of class', 
    'Which gender(s) do you identify with', 
    vertical = True,
    values_increment = 5,
    splice_required = True, 
    display_as_percentage = True,
    rotation_angle = 0
)

df_sex = df[['sex']].dropna(axis=0)
graphs.create_bar(
    df_sex, 
    'sex', 
    'Sexual Orientation', 
    'Percentage of class', 
    'Which sexual orientations do you identify with', 
    vertical = True,
    values_increment = 10,
    splice_required = True, 
    display_as_percentage = True,
    rotation_angle = 0
)

df_birth_location = df[['birth_location']].dropna(axis=0)
graphs.create_bar(
    df_birth_location, 
    'birth_location', 
    'Location of Birth', 
    'Percentage of class', 
    'Where were you born?', 
    vertical = False,
    display_as_percentage = True,
    rotation_angle = 0
)

df_hometown = df[['hometown_location']].dropna(axis=0)
graphs.create_bar(
    df_hometown, 
    'hometown_location', 
    'Hometown', 
    'Percentage of class', 
    'In which city do you consider to be your hometown?', 
    vertical = False,
    display_as_percentage = True,
    rotation_angle = 0
)

df_politics = df[['politics']].dropna(axis=0)
graphs.create_bar(
    df_politics, 
    'politics', 
    'Political Identity', 
    'Percentage of class', 
    'How would you describe yourself politically?', 
    vertical = True,
    display_as_percentage = True,
    rotation_angle = 0,
    labels = ['Far Left', 'Left', 'Center Left', 'Center', 'Center Right', 'Right', 'Far Right']
)

df_election = df[['election']].dropna(axis=0)
graphs.create_bar(
    df_election, 
    'election', 
    'Political Party', 
    'Percentage of class', 
    'If the election was held today (June 2023), which party would you vote for?', 
    vertical = True,
    display_as_percentage = True,
    rotation_angle = 45,
    labels = ['Green', 'NDP', 'Liberal', 'Conservative', "People's Party of Canada", 'I would not vote']
)

df_religion = df[['religion']].dropna(axis=0)
graphs.create_bar(
    df_religion, 
    'religion', 
    'Religion', 
    'Percentage of class', 
    'What is your school of religious thought?', 
    vertical = True,
    values_increment = 5,
    display_as_percentage = True,
    rotation_angle = 45,
)

df_number_languages = df[['number_languages']].dropna(axis=0)
graphs.create_bar(
    df_number_languages, 
    'number_languages', 
    'Langauge', 
    'Number of Speakers', 
    'What languages can you speak?', 
    vertical = False,
    splice_required = True,
    values_increment = 5,
    display_as_percentage = False,
    rotation_angle = 45,
    drop_values = ['English']
)

df_languages = df[['languages']].dropna(axis=0)
graphs.create_bar(
    df_languages, 
    'languages', 
    'Langauge', 
    'Number of Speakers', 
    'What languages are spoken at home?', 
    vertical = False,
    splice_required = True,
    values_increment = 5,
    display_as_percentage = False,
)

df_citizenship = df[['citizenship']].dropna(axis = 0)
graphs.create_pie(df_citizenship, 'citizenship', 'What is your citizenship status')


df_politics_vs_parents = df[['politics', 'politics_parents']]
if(df_politics_vs_parents['politics'].isnull().values.any()):
    df_politics_vs_parents = df_politics_vs_parents.dropna(subset = ['politics'])
df_politics_vs_parents['politics_parents'] = df_politics_vs_parents['politics_parents'].fillna("No Answer")
labels_politics_vs_parents = ['Far Left', 'Left', 'Center Left', 'Center', 'Center Right', 'Right', 'Far Right', 'No Answer'] ######
list_df_bar_politics_vs_parents = []
for label in labels_politics_vs_parents:
    df_temp = df_politics_vs_parents[df_politics_vs_parents['politics'] == label]
    if(df_temp.size != 0):
        df_temp = df_temp.rename(columns = {'politics_parents': label})
        df_temp = df_temp.drop(columns = 'politics')
        list_df_bar_politics_vs_parents.append(df_temp)
df_politics_vs_parents_cleaned = functools.reduce(lambda df1, df2: df1.append(df2), list_df_bar_politics_vs_parents)
df_politics_vs_parents_cleaned = df_politics_vs_parents_cleaned.reset_index().drop(columns='index')
graphs.create_stacked_bar(
    df_politics_vs_parents_cleaned,
    column_name_list = ['Far Left', 'Left', 'Center Left', 'Center', 'Center Right', 'Right'],
    title_label = 'SYDE 2023 political views',
    values_label = 'Number of students',
    title = "SYDE 2023 political views vs Parents' political views",
    vertical = True,
    labels = ['Left', 'Center Left', 'Center', 'Center Right', 'Right', 'Far Right', 'No Answer'],
    values_increment = 5,
    colours = ['#F62D2D', '#D3212D', '#A2264B', '#722B6A', '#412F88', '#1034A6','black'],
    legend_title = "Parents' political views"
)


df_politics_vs_election = df[['politics', 'election']]
df_politics_vs_election = df_politics_vs_election.dropna()
df_politics_vs_election = df_politics_vs_election[df_politics_vs_election != 'I am legally unable to vote in a Canadian federal election']
labels_politics_vs_election_politics = ['Far Left', 'Left', 'Center Left', 'Center', 'Center Right', 'Right'] 
labels_politics_vs_election_election = ['Green', 'NDP', 'Liberal', 'Conservative', "People's Party of Canada", 'I would not vote']
list_df_politics_vs_election = []
for label in labels_politics_vs_election_election:
    df_temp = df_politics_vs_election[df_politics_vs_election['election'] == label]
    if(df_temp.size != 0):
        df_temp = df_temp.rename(columns = {'politics': label})
        df_temp = df_temp.drop(columns = 'election')
        list_df_politics_vs_election.append(df_temp)
df_politics_vs_election_cleaned = functools.reduce(lambda df1, df2: df1.append(df2), list_df_politics_vs_election)
df_politics_vs_election_cleaned = df_politics_vs_election_cleaned.reset_index().drop(columns='index')
graphs.create_stacked_bar(
    df_politics_vs_election_cleaned,
    column_name_list = labels_politics_vs_election_election,
    title_label = 'Canadian Federal Political Party',
    values_label = 'Number of Students',
    title = 'Who would SYDE 2023 vote for based on their political view',
    vertical = True,
    labels = labels_politics_vs_election_politics,
    values_increment = 5,
    colours = ['#F62D2D', '#D3212D', '#A2264B', '#722B6A', '#412F88', '#1034A6'],
    title_label_rotation_angle=45,
    legend_title = 'SYDE 2023 political views'
)




df_religion_vs_parents = df[['religion', 'religion_parents']].dropna(axis = 0)
df_religion_splice = df_religion_vs_parents[df_religion_vs_parents['religion_parents'].str.contains(',')]
df_religion_no_splice = df_religion_vs_parents[~df_religion_vs_parents['religion_parents'].str.contains(',')]
df_religion_splice['religion_parents'] = df_religion_splice['religion_parents'].map(lambda x: x.split(", ")) # turn commas into array
df_religion_splice = df_religion_splice.explode('religion_parents') # turn array into individual values with first column
df_religion_vs_parents = pd.concat([df_religion_splice, df_religion_no_splice]).reset_index().drop(columns = 'index')
list_religion = (
    df_religion_vs_parents \
    .groupby('religion') \
    .size() \
    .reset_index(name = 'count') \
    .sort_values('count', ascending = False) \
    .reset_index() \
    .drop(columns = 'index'))['religion'].tolist() # get religions in descending order
list_religion_parents = df_religion_vs_parents['religion_parents'].unique().tolist()
list_df_religion = []
for religion in list_religion:
    df_temp = df_religion_vs_parents[df_religion_vs_parents['religion'] == religion]
    if(df_temp.size != 0):
        df_temp = df_temp.rename(columns = {'religion_parents': religion})
        df_temp = df_temp.drop(columns = 'religion')
        list_df_religion.append(df_temp)
df_religion_vs_parents_cleaned = functools.reduce(lambda df1, df2: df1.append(df2), list_df_religion).reset_index().drop(columns = 'index')
graphs.create_stacked_bar(
    df_religion_vs_parents_cleaned,
    column_name_list = list_religion,
    title_label = 'SYDE 2023 Religion',
    values_label = 'Number of Students',
    title = "SYDE 2023 Religion compared to their parents' religion",
    vertical = True,
#     labels = list_religion_parents,
    values_increment = 5,
    title_label_rotation_angle=45
)