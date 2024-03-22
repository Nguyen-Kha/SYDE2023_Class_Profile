# necessary imports
import numpy as np  # use for array and matrix stuff
import pandas as pd  # use for dataframes, think of it as excel
import math
import matplotlib.pyplot as plt  # use to make graphs
import seaborn as sns
from collections import Counter

import helpers
import graphs
import functools

df_school = pd.read_csv("csv/school.csv")

#### TE #########
df_te = df_school[['te']]
df_te = df_te.dropna()

# Top 15 TEs
df_top_te = df_te.copy()
df_top_te['te'] = df_top_te['te'].map(lambda x: x.split(", "))
df_top_te = df_top_te.explode('te')
df_top_te  = df_top_te['te'].value_counts().reset_index()
df_top_te = df_top_te.loc[df_top_te['te'] > 3]
top_te_list = df_top_te['index'].tolist()

graphs.create_bar(
    df_te,
    'te',
    'course',
    'number of respondents',
    'TEs that you took',
    vertical = False,
    splice_required = True,
    labels = top_te_list,
    max_label_length=40
)
#### END: TE #########

#### CSE #########

#### END: CSE #########

#### favourite core course #######
graphs.create_bar(
    df_school,
    "fav_core",
    "Core Course",
    "Percentage of Respondents",
    "What was your favourite core course?",
    False,
    display_as_percentage=True,
    values_increment=5,
)
#### END: favourite core course #######

#### least favourite core #########

#### END: least favourite core #########

#### create favourite profs ######
graphs.create_bar(
    df_school,
    "fav_profs",
    "Professor",
    "Percentage of Respondents",
    "Who were your favourite profs?",
    False,
    display_as_percentage=True,
    splice_required=True,
)
#### END: create favourite profs ############

#### favourite TE #########
graphs.create_bar(
    df_school,
    "fav_te",
    "Technical Elective",
    "Percentage of Respondents",
    "What was your favourite TE?",
    False,
    display_as_percentage=True,
    splice_required=True,
    max_label_length=40,
)
#### END: favourite TE ##############

#### least favourite TE #########

#### END: least favourite TE #########

#### favourite CSE #########
graphs.create_bar(
    df_school,
    "fav_cse",
    "Complementary Studies Elective",
    "Percentage of Respondents",
    "What was your favourite CSE?",
    False,
    display_as_percentage=True,
    splice_required=True,
)
#### END: favourite CSE ############

#### least favourite CSE #########

#### END: least favourite CSE #########

#### CR NCR ############
graphs.create_bar(
    df_school,
    "cr_ncr",
    "Number of Courses",
    "Percentage of Respondents",
    "How many courses did you CR/NCR?",
    True,
    display_as_percentage=True,
)
#### END: CR NCR #########

#### failures #######
graphs.create_bar(
    df_school,
    "failed",
    "Options",
    "Percentage of Respondents",
    "From the options below, what have you failed?",
    False,
    display_as_percentage=True,
    splice_required=True,
    labels=[
        "I have not failed any of the above",
        "A course",
        "A work report",
        "An exam",
        "An assignment",
        "A quiz / test",
    ],
)
#### END failures #########

#### easiest term, hardest term, favourite term ######
df_terms = df_school[['easiest_term', 'hardest_term', 'fav_term']]

graphs.create_pie(
    df_terms,
    'easiest_term',
    'Which term did you find the easiest',
    labels = helpers.get_study_term_list(),
    percent_text_distance=1.08
)

graphs.create_pie(
    df_terms,
    'hardest_term',
    'Which term did you find the hardest',
    labels = helpers.get_study_term_list(),
    percent_text_distance=1.08
)

graphs.create_pie(
    df_terms,
    'fav_term',
    'Which term was your favourite',
    labels = helpers.get_study_term_list(),
    percent_text_distance=1.08
)
#### END: easiest term, hardest term, favourite term ######

#### least favourite term ########
df_least_fav_term = df_school[['least_fav_term']]
df_least_fav_term = df_least_fav_term.dropna()

graphs.create_pie(
    df_least_fav_term,
    'least_fav_term',
    'Which term was your least favourite',
    labels = helpers.get_study_term_list(),
    percent_text_distance=1.08
)
#### END: least favourite term ########

