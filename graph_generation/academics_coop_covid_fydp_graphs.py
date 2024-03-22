# necessary imports
import pandas as pd  # use for dataframes, think of it as excel

import helpers
import graphs

df_school = pd.read_csv("school.csv")
df_fydp = pd.read_csv('fydp.csv')
df_coop = pd.read_csv('coop.csv')

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
df_cse = df_school[['cse']]
df_cse = df_cse.dropna()

df_top_cse = df_cse.copy()
df_top_cse['cse'] = df_top_cse['cse'].map(lambda x: x.split(", "))
df_top_cse = df_top_cse.explode('cse')
df_top_cse = df_top_cse['cse'].value_counts().reset_index()
df_top_cse = df_top_cse.loc[df_top_cse['cse'] > 3]
top_cse_list = df_top_cse['index'].tolist()

graphs.create_bar(
    df_cse,
    'cse',
    'course',
    'Number of respondents',
    'CSEs that you took',
    vertical = False,
    splice_required = True,
    labels = top_cse_list,
    values_increment = 2
)
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
df_least_fav_core = df_school[['least_fav_core']]
df_least_fav_core = df_least_fav_core.dropna()

graphs.create_bar(
    df_least_fav_core,
    'least_fav_core',
    '',
    'Percent of respondents',
    'What was your least favourite core course',
    vertical = False,
    display_as_percentage = True
)
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

#### op spec minor ##########
df_op_spec_minor = df_school[['op_spec_minor']]
df_op_spec_minor = df_op_spec_minor.dropna()

graphs.create_bar(
    df_op_spec_minor,
    'op_spec_minor',
    '',
    'Number of respondents',
    'Options, Specializations, or Minors you enrolled in',
    vertical = False,
    splice_required = True
)
#### END; op spec minor #############

#### fydp proud ##########
df_fydp_proud = df_fydp[['fydp_proud']]
df_fydp_proud = df_fydp_proud.dropna()

graphs.create_pie(
    df_fydp_proud,
    'fydp_proud',
    'Are you proud of your FYDP',
    labels = ['Yes', 'No', 'Somewhat'],
    percent_text_distance=1.08
)
#### END: fydp proud

#### fydp future ##########
df_fydp_future = df_fydp[['fydp_future']]
df_fydp_future = df_fydp_future.dropna()

graphs.create_pie(
    df_fydp_future,
    'fydp_future',
    'Do you intend on continuing your FYDP in the future',
    labels = ['Yes', 'No', 'Unsure'],
    percent_text_distance=1.08
)
#### END: fydp future

#### enjoy coop position ########
enjoy_pos_list = [
    '1a_coop_enjoy_pos',
    '1b_coop_enjoy_pos',
    '2a_coop_enjoy_pos',
    '2b_coop_enjoy_pos',
    '3a_coop_enjoy_pos',
    '3b_coop_enjoy_pos'
]
df_coop_enjoy_pos = df_coop[enjoy_pos_list]

graphs.create_line(
    df_coop_enjoy_pos,
    enjoy_pos_list,
    'Co-op Term',
    'Enjoyment rating',
    'How much did you enjoy your co-op position',
    sequential_labels = helpers.get_coop_term_list(),
    only_show_average=True,
    values_min = 0,
    file_name='enjoy_coop_position_line'
)
#### END: enjoy coop position ########

#### enjoy coop location ##########
enjoy_loc_list = [
    '1a_coop_enjoy_loc',
    '1b_coop_enjoy_loc',
    '2a_coop_enjoy_loc',
    '2b_coop_enjoy_loc',
    '3a_coop_enjoy_loc',
    '3b_coop_enjoy_loc'
]
df_coop_enjoy_loc = df_coop[enjoy_loc_list]

graphs.create_line(
    df_coop_enjoy_loc,
    enjoy_loc_list,
    'Co-op Term',
    'Enjoyment rating',
    'How much did you enjoy your co-op location',
    sequential_labels = helpers.get_coop_term_list(),
    only_show_average=True,
    values_min = 0,
    file_name='enjoy_coop_location_line'
)
#### END: enjoy coop location ##########

#### return to previous employer #########
df_return_employer = df_coop[['return_to_employer']]
df_return_employer = df_return_employer.dropna()

graphs.create_pie(
    df_return_employer,
    'return_to_employer',
    'Have you ever returned to a previous employer for one of your co-ops',
    labels = ['Yes', 'No'],
    percent_text_distance=1.2
)
#### END: return to previous employer #########

#### why return to employer ##########
df_why_return_employer = df_coop[['why_return_to_employer']]
df_why_return_employer = df_why_return_employer.dropna()

graphs.create_bar(
    df_why_return_employer,
    'why_return_to_employer',
    '',
    'Percent of respondents',
    'Why did you return to a previous employer',
    vertical = False,
    display_as_percentage = True,
    splice_required = True,
    values_increment = 5,
    max_label_length=40
)
#### END: why return to employer ##########