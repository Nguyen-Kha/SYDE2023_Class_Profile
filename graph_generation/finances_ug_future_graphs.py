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

df_finance = pd.read_csv('../csv/final/split/finances.csv')
df_ug_reflections = pd.read_csv('../csv/final/split/undergrad_reflections.csv')
df_future_plans = pd.read_csv('../csv/final/split/future_plans.csv')

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

#### Create alt syde choice #####################
df_other_school = df_ug_reflections[['syde_again', 'other_school_program']]
df_other_school = df_other_school.loc[df_other_school['syde_again'] == 'No']
df_other_school = df_other_school.dropna()

graphs.create_bar(
    df_other_school,
    'other_school_program',
    'Alternative school and program',
    'Number of respondents',
    'Which program would you have gone into instead',
    vertical = False,
    splice_required = True,
    max_label_length = 30
)
#### END; crate alt syde choice ##################

#### Create syde satisfaction stacked bar ###########
syde_satisfaction_list = [ 'syde_satisfied',
 'syde_belonged',
 'syde_community']

df_syde_satisfaction = df_ug_reflections[syde_satisfaction_list]
df_syde_satisfaction

graphs.create_bar_stacked(
    df_syde_satisfaction,
    syde_satisfaction_list,
    '',
    'Percent of respondents',
    'State your level of agreement with your satisfaction with SYDE',
    vertical = False,
    display_as_percentage = True,
    labels = helpers.get_agree_no_opinion_scale(),
    column_labels = ['I am satisfied with the SYDE Program', 'I belonged in SYDE', 'I felt like I was a part of the SYDE community']
)
#### END:  Create syde satisfaction stacked bar ###########

#### Create engineering stacked bar ######
aspire_eng_list = ['aspiring_engineer',
 'syde_trad_eng',
]

df_aspire_eng = df_ug_reflections[aspire_eng_list]
df_aspire_eng = df_aspire_eng.dropna()

graphs.create_bar_stacked(
    df_aspire_eng,
    aspire_eng_list,
    '',
    'Percent of respondents',
    'State your level of agreement with your view on engineering',
    vertical = False,
    display_as_percentage = True,
    labels = helpers.get_agree_no_opinion_scale(),
    column_labels = ['I consider myself to be an aspiring engineer', 'SYDE prepared me for a traditional engineering career']
)
#### END: create engineering stacked bar ##############

#### create syde quality stacked bar ##########33
syde_quality_list = ['syde_prof_quality',
 'syde_course_quality',
 'syde_support_quality',
]

df_syde_quality = df_ug_reflections[syde_quality_list]
df_syde_quality = df_syde_quality.dropna()

graphs.create_bar_stacked(
    df_syde_quality,
    syde_quality_list,
    '',
    'Percent of respondents',
    'State your level of agreement with the quality of SYDE',
    vertical = False,
    display_as_percentage = True,
    labels = helpers.get_agree_no_opinion_scale(),
    column_labels = ["The quality of professors' instructional content was acceptable", 'The quality of the SYDE courses was acceptable', 'The support given by the SYDE administration was acceptable']
)
#### END: create syde quality stacked bar #################

#### create uni satisfaction stacked bar
uni_satisfaction_list = ['uw_satisfied',
 'friends_outside_syde',
 'friends_outside_eng',
 'ec_satisfied'
]

df_uni_satisfaction = df_ug_reflections[uni_satisfaction_list]
df_uni_satisfaction = df_uni_satisfaction.dropna()

graphs.create_bar_stacked(
    df_uni_satisfaction,
    uni_satisfaction_list,
    '',
    'Percent of respondents',
    'State your level of agreement with the following university experiences',
    vertical = False,
    display_as_percentage = True,
    labels = helpers.get_agree_no_opinion_scale(),
    column_labels = [
        'I am satisfied with my experience at UW',
        'I made a lot of friends outside of SYDE',
        'I made a lot of friends outside of UW Engineering',
        'I am satisfied with the extracurriculars I participated in'
    ]
)
#### END: create uni satisfaction stacked bar #########

#### Create p eng pie ###########
df_peng = df_future_plans[['p_eng']]
df_peng = df_peng.dropna()

graphs.create_pie(
    df_peng,
    'p_eng',
    'Do you intend on getting a P.Eng',
    labels = ['Yes', 'Undecided', 'No'],
    percent_text_distance = 1.07
)
#### END: create p eng pie ##########

#### create marriage bar #########
def clean_marriage(value):
    if(value == 0):
        return 'I do not intend on getting married'
    return str(int(value))

df_marriage = df_future_plans[['age_of_marriage']]
df_marriage = df_marriage.dropna()
# marriage_list = list(map(lambda x: str(int(x)), sorted(df_marriage['age_of_marriage'].unique().tolist())))
marriage_list = np.arange(25, 35, 1) # get bounds from above
marriage_list = list(map(lambda x: str(int(x)), marriage_list))
marriage_list.insert(0, 'I do not intend on getting married')

df_marriage['age_of_marriage'] = df_marriage['age_of_marriage'].apply(clean_marriage)
df_marriage

graphs.create_bar(
    df_marriage,
    'age_of_marriage',
    'Desired age of marriage',
    'Number of respondents',
    'At which age would you like to get married',
    vertical = True,
    labels = marriage_list,
    max_label_length = 10 
)
#### END; Create marriage bar #############

#### create children bar ##########
def clean_children(value):
    if(value == 0):
        return 'I do not plan on having children'
    return str(int(value))

df_children = df_future_plans[['age_of_children']] 
df_children = df_children.dropna()
df_children = df_children[df_children['age_of_children'] != 2]
df_children['age_of_children'] = df_children['age_of_children'].apply(clean_children)
children_list = np.arange(26, 36, 1) # list(sorted(df_children['age_of_children'].unique().tolist()))
children_list = list(map(lambda x: str(int(x)), children_list))
children_list.insert(0, 'I do not plan on having children')

graphs.create_bar(
    df_children,
    'age_of_children',
    'Desired age of having children',
    'Number of respondents',
    'At which age would you like to have children',
    vertical = True,
    labels = children_list,
    max_label_length = 10
)
#### END: create children bar ##########

#### Create post grad plans bar ##########
def clean_postgrad_plans(value):
    if(value == 'Working (already have a job lined up)'):
        return 'Working'
    elif(value == 'Grad school / Professional school / Other Education'):
        return 'Further Education'
    return value

df_postgrad = df_future_plans[['postgrad_plans']].copy()
df_postgrad = df_postgrad.dropna()
df_postgrad['postgrad_plans'] = df_postgrad['postgrad_plans'].apply(clean_postgrad_plans)

graphs.create_bar(
    df_postgrad,
    'postgrad_plans',
    '',
    'Percentage of respondents',
    'What are your post-grad plans',
    vertical = True,
    display_as_percentage = True,
    values_increment = 5
)
#### END: Create post grad plans bar

#### Create postgrad leave canada pie #############
df_postgrad_leave_ca = df_future_plans[['postgrad_leave_canada']]
df_postgrad_leave_ca = df_postgrad_leave_ca.dropna()

graphs.create_pie(
    df_postgrad_leave_ca,
    'postgrad_leave_canada',
    'Do your post-grad plans require you to leave Canada',
    labels = ['Yes', 'No'],
    percent_text_distance=1.2
)
#### END: create postgrad leave canada pie #########