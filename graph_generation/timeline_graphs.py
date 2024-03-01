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
df_easy_useful = pd.read_csv('timeline_easy_useful_courses.csv')

#### Create easiness vs usefulness scatter plot ###################
df_eu_working = df_easy_useful.drop(columns = 'uid')
df_eu_working = df_eu_working.fillna(df_eu_working.median())

easy_useful_sorted_list = sorted(df_eu_working.columns.tolist())

# Create 2 dataframes for easiness ratings and usefulness ratings
df_eu_working_easiness = df_eu_working[easy_useful_sorted_list[0:int(len(df_eu_working.columns.tolist()) / 2)]]
df_eu_working_usefulness = df_eu_working[easy_useful_sorted_list[int(len(df_eu_working.columns.tolist()) / 2) : int(len(df_eu_working.columns.tolist()))]]

# Get mean easiness ratings
df_eu_working_easiness = pd.DataFrame(df_eu_working_easiness.mean().to_dict(), index=['easiness'])
df_eu_working_easiness = df_eu_working_easiness.transpose()
df_eu_working_easiness['course'] = helpers.get_syde_core_courses_list()
df_eu_working_easiness = df_eu_working_easiness.reset_index().drop(columns = 'index')

# Get mean usefulness ratings
df_eu_working_usefulness = pd.DataFrame(df_eu_working_usefulness.mean().to_dict(), index=['usefulness'])
df_eu_working_usefulness = df_eu_working_usefulness.transpose()
df_eu_working_usefulness['course'] = helpers.get_syde_core_courses_list()
df_eu_working_usefulness = df_eu_working_usefulness.reset_index().drop(columns = 'index')

# Join dataframes, normalize, only show course numbers
df_eu_working = df_eu_working_easiness.join(df_eu_working_usefulness.set_index('course'), on = 'course')
df_eu_working[['easiness', 'usefulness']] = df_eu_working[['easiness', 'usefulness']] - 4
df_eu_working['course'] = df_eu_working['course'].apply(lambda x: x.replace("SYDE ", ""))

graphs.create_scatter(
    df_eu_working,
    'easiness',
    'usefulness',
    'SYDE Core Courses: How Easy and How Useful?',
    x_axis_label = 'Easiness rating of course',
    y_axis_label = 'Usefulness rating of course',
    annotate = True,
    annotated_column_name = 'course',
    x_values_min = -3,
    x_values_max = 3,
    x_values_increment = 1,
    y_values_min = -3,
    y_values_max = 3,
    y_values_increment = 1
)
#### END: Create easiness vs usefulness scatter plot ###################