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
df_gpa = pd.read_csv('timeline_gpa.csv')
df_employed = pd.read_csv('timeline_employed.csv')
df_coop_category = pd.read_csv('timeline_coop_category.csv')
df_location = pd.read_csv('timeline_location.csv')

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

#### Create gpa boxplot ###################
df_gpa_working = df_gpa.drop(index = 33) # This row has all null
df_gpa_working = df_gpa_working.drop(columns = 'uid')
df_gpa_working = df_gpa_working.fillna(df_gpa_working.median())
df_gpa_working_columns = df_gpa_working.columns.tolist()

graphs.create_boxplot(
    df_gpa_working,
    df_gpa_working_columns,
    'Term',
    'Percentage',
    'GPA per Term',
    vertical = True,
    values_min = 60,
    values_max = 100,
    values_increment = 5,
    column_labels = ['1A', '1B', '2A', '2B', '3A', '3B', '4A', '4B'],
    value_is_percentage = True,
#     figure_height = 15,
#     figure_width = 15
)
#### END: Create gpa boxplot ##############

#### Create Co-op Category Stacked bar ##########

def change_coop_category(value):
    if(type(value) == float):
        if(math.isnan(value)):
            return np.nan
    
    if(value == '3D Modelling'):
        value = 'Mechanical / Hardware'
    elif(value == 'Teacher Assistant / Curriculum Planning'):
        value = 'Project Management'
    elif(value == 'Manufacturing Technician'):
        value = 'Mechanical / Hardware'
    elif(value == 'analyst mixed with tech support'):
        value = 'Analyst'
    elif(value == 'Event planning'):
        value = 'Project Management'
    elif(value == 'Automation'):
        value = 'Mechanical / Hardware'
    elif(value == 'UX/Data Analyst'):
        value = 'UI / UX'
    elif(value == 'Design'):
        value = 'UI / UX'
    elif(value == 'Hardware (Embedded Software, Electrical)'):
        value = 'Mechanical / Hardware'
    elif(value == 'Data Science' or value == 'Machine Learning / Artificial Intelligence' or value == 'Data Engineering'):
        value = 'DE / DS / ML / AI'
    elif(value == 'Mechanical'):
        value = 'Mechanical / Hardware'
    return value

# SELECT coop_category.*, employed.* FROM coop_category JOIN employed ON coop_category.uid = employed.uid
df_coop_category_working = df_coop_category.join(df_employed.set_index('uid'), on = 'uid')
df_coop_category_working = df_coop_category_working.drop(columns = 'uid')

coop_cat_list = df_coop_category_working.columns.tolist()[0:6]
employed_status_list = df_coop_category_working.columns.tolist()[6:]

employed_status_list = list(map(lambda x: x.replace('\n', ""), employed_status_list))
df_coop_category_working = df_coop_category_working.drop(index = 33)


for i in range(0, len(coop_cat_list)):
    df_coop_category_working.loc[df_coop_category_working[employed_status_list[i]] == 'No', coop_cat_list[i] ] = 'Unemployed'
df_coop_category_working = df_coop_category_working.drop(columns = list(employed_status_list))
df_coop_category_working = df_coop_category_working.fillna("Uncategorized")

for i in range(0, len(coop_cat_list)):
    df_coop_category_working[coop_cat_list[i]] = df_coop_category_working[coop_cat_list[i]].apply(change_coop_category)
    
graphs.create_bar_stacked(
    df_coop_category_working,
    coop_cat_list,
    'Co-op Term',
    'Percentage of Students',
    'Co-op categories by term',
    display_as_percentage = True,
    vertical = True,
    labels = ['Software', 'UI / UX','Product Management','Product Design', 'IT', 'QA', 'Analyst', 'Mechanical / Hardware',   'Project Management',   'DE / DS / ML / AI', 'Research', 'Technical Writing','Uncategorized', 'Unemployed'],
    column_labels = ['Co-op 1','Co-op 2','Co-op 3','Co-op 4','Co-op 5','Co-op 6'],
    file_name="coop_term_roles_stacked_bar",
)

#### END: Create Co-op Category Stacked bar ##########

#### Create Co-op Location Stacked bar ################

def replace_blank_location(value):
    if(value == ""):
        return "Undisclosed"
    return value

def change_location_region(value):
    if(value == 'GTA' or value == 'Halton' or value == 'Hamilton'):
        value = 'GTHA'
    elif(value == 'Southwestern US' or value == 'Midwestern US' or value == 'Southern US' or value == 'California'):
        value = 'Other US'
    elif(value == 'NCR'):
        value = 'ON'
    elif(value == 'NYC'):
        value = 'Northeastern US'
    return value

df_location_working = df_location.drop(columns = 'uid')
df_location_working = df_location_working.fillna("Undisclosed,Undisclosed,Undisclosed,Undisclosed,Undisclosed")
location_columns = df_location_working.columns.tolist()

# Get the region of the location
df_location_working[location_columns] = df_location_working[location_columns].applymap(lambda x: x.split(",")[3].strip())
for i in location_columns:
    df_location_working[i] = df_location_working[i].apply(replace_blank_location)
    df_location_working[i] = df_location_working[i].apply(change_location_region)
df_location_working

graphs.create_bar_stacked(
    df_location_working,
    location_columns,
    'Co-op Term',
    'Percentage of Class',
    'Co-op Locations',
    vertical = True,
    labels = ['Toronto', 'GTHA', 'KWC', 'ON', 'BC', 'Central Canada', 'QC', 'Bay Area', 'Northwestern US', 'Northeastern US', 'Other US', 'Europe', 'Undisclosed'],
    display_as_percentage = True,
    column_labels = ['Co-op 1','Co-op 2','Co-op 3','Co-op 4','Co-op 5','Co-op 6'],
    file_name = "coop_locations_stacked_bar"
)
#### END: Create co-op location stacked bar ##############