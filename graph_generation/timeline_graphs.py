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
df_lectures = pd.read_csv('timeline_lectures.csv')
df_stress = pd.read_csv('timeline_stress.csv')
df_rent = pd.read_csv('timeline_rent.csv')
df_pay = pd.read_csv('timeline_pay.csv')
df_find_job = pd.read_csv('timeline_find_job.csv')
df_ww_rating = pd.read_csv('timeline_ww_rating.csv')

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

#### Create Lecture attendance line #########
df_lectures_working = df_lectures.drop(columns = 'uid')
df_lectures_working = df_lectures_working.drop(index = 33).reset_index().drop(columns = 'index')
df_lectures_working = df_lectures_working.fillna(df_lectures_working.median())
lectures_list = df_lectures_working.columns.tolist()

graphs.create_line(
    df_lectures_working,
    lectures_list,
    'Study Term', 
    'Lecture Attendance', 
    'How often did you come to lectures',
    only_show_average = True,
    sequential_labels = helpers.get_study_term_list(),
    values_min = 1
)
#### END: Create lecture attendance line #######

#### Create stress levels line #################
df_stress_working = df_stress.drop(columns = 'uid').drop(index = 33).reset_index().drop(columns = 'index')
df_stress_working = df_stress_working.fillna(df_stress_working.median())
stress_list = df_stress_working.columns.tolist()

graphs.create_line(
    df_stress_working,
    stress_list,
    'Study Term',
    'Reported Stress Level',
    'How stressful was this term',
    values_min = 1,
    sequential_labels = helpers.get_study_term_list(),
    only_show_average = True,
    figure_height = 7,
)
#### END: Create stress levels line ###############

#### Create rent boxplot ##########################
df_rent_working = df_rent.drop(columns = 'uid').drop(index = 33).reset_index().drop(columns = 'index')
# df_rent_working = df_rent_working.fillna(df_rent_working.median())
rent_columns = df_rent_working.columns.tolist()

graphs.create_boxplot(
    df_rent_working,
    rent_columns,
    'Term',
    '$ CAD paid for rent',
    'How much did you pay in rent',
    column_labels = helpers.get_study_coop_term_list(),
    values_min = 0,
    values_max = 2400,
    values_increment = 200,
    drop_values = {'rent_1a': 4285, 'rent_c6': 4000}
)
#### END: Create rent boxplot ####################

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

#### Create Employment rate line graph ###################

df_employed_working = df_employed.drop(columns = 'uid')
employed_status_list = df_employed_working.columns.tolist()
df_employed_working[employed_status_list] = df_employed_working[employed_status_list].applymap(lambda x: 1 if x == 'Yes' else 0)

df_employed_working = helpers.transform_df_for_single_line(df_employed_working, employed_status_list, True)

graphs.create_line(
    df_employed_working,
    employed_status_list,
    'Co-op Term',
    'Percent of class employed',
    'SYDE 2023 Employment rate',
    values_min = 0,
    values_max = 100,
    values_increment = 10,
    value_is_percentage = True,
    sequential_labels = ['Co-op 1','Co-op 2','Co-op 3','Co-op 4','Co-op 5','Co-op 6'],
)
#### END:  Create Employment rate line graph ###################

#### Create Co-op pay boxplot ########################
df_pay_working = df_pay.join(df_employed.set_index('uid'), on = 'uid')
df_pay_working = df_pay_working.drop(columns = 'uid').drop(index = 33).reset_index().drop(columns = 'index')

pay_columns = df_pay_working.columns.tolist()[0:6]
employed_columns = df_pay_working.columns.tolist()[6:]

# If you didn't have a job, then your pay was 0
for i in range(0, len(pay_columns)):
    df_pay_working.loc[df_pay_working[employed_columns[i]] == 'No', pay_columns[i]] = 0
    
df_pay_working = df_pay_working.drop(columns = employed_columns)
df_pay_working = df_pay_working.fillna(df_pay_working.median())
df_pay_working

graphs.create_boxplot(
    df_pay_working,
    pay_columns,
    'Co-op Term',
    '$ CAD per hour',
    'What was your rate of compensation?',
    column_labels = helpers.get_coop_term_list(),
    values_min = 0.01,
    values_max = 80,
    values_increment = 5,
)
#### END: Create Co-op Pay boxplot ######################

#### Create find job stacked bar #######################
df_find_job_working = df_find_job.join(df_employed.set_index('uid'), on = 'uid')
df_find_job_working = df_find_job_working.drop(columns = 'uid').drop(index = 33).reset_index().drop(columns = 'index')

find_job_columns = df_find_job_working.columns.tolist()[0:6]
employed_columns = df_find_job_working.columns.tolist()[6:]

for i in range(0, len(find_job_columns)):
    df_find_job_working.loc[df_find_job_working[employed_columns[i]] == 'No', find_job_columns[i]] = 'Unemployed'

df_find_job_working = df_find_job_working.drop(columns = employed_columns)
df_find_job_working = df_find_job_working.fillna("Not Disclosed")
df_find_job_working

graphs.create_bar_stacked(
    df_find_job_working,
    find_job_columns,
    'Co-op Term',
    'Percentage of Students',
    'How did you find your co-op job',
    vertical = True,
    column_labels = helpers.get_coop_term_list(),
    display_as_percentage = True,
    labels = ['WaterlooWorks', 'Networking / Referral', 'Cold Applying / External', 'Previous employer', 'CECA', 'Family', 'Not Disclosed', 'Unemployed']
)
#### END: Create find job stacked bar ###################

#### Create WaterlooWorks rating stacked bar ############
df_ww_rating_working = df_ww_rating.join(df_employed.set_index('uid'), on = 'uid')
df_ww_rating_working = df_ww_rating_working.drop(columns = 'uid').drop(index = 33).reset_index().drop(columns = 'index')

ww_rating_columns = df_ww_rating_working.columns.tolist()[0:6]
employed_columns = df_ww_rating_working.columns.tolist()[6:]

for i in range(0, len(ww_rating_columns)):
    df_ww_rating_working.loc[df_ww_rating_working[employed_columns[i]] == 'No', ww_rating_columns[i]] = 'Unemployed'
    
df_ww_rating_working = df_ww_rating_working.drop(columns = employed_columns)
df_ww_rating_working = df_ww_rating_working.fillna("Not Disclosed")

graphs.create_bar_stacked(
    df_ww_rating_working,
    ww_rating_columns,
    'Co-op Term',
    'Percentage of Students',
    'What was your rating on WaterlooWorks for that co-op term',
    vertical = True,
    column_labels = helpers.get_coop_term_list(),
    display_as_percentage = True,
    labels = ['Satisfactory', 'Good', 'Very Good', 'Excellent', 'Outstanding', 'Not Disclosed', 'Unemployed']
)
#### END: Create WaterlooWorks rating stacked bar ###############