# necessary imports
import pandas as pd               # use for dataframes, think of it as excel
# import helpers
import graphs

# Figure out better way to do rice purity

df = pd.read_csv()

list_71 = ['hye_fabricated',
 'hye_collab',
 'hye_materials',
 'hye_plagiarized',
 'hye_false_resume',
 'hye_cheated',
 'hye_cheated_online',
 'hye_policy_71',
 'hye_probation']
df_71 = df[list_71]
graphs.create_bar_stacked(
    df_71,
    list_71,
    title_label = 'have you ever...',
    values_label = 'Percentage of SYDE 2023',
    title = 'Policy 71 core',
    vertical = False,
    display_as_percentage = True,
    file_name = 'policy_71_core'
)

df_casual_relationships = df[['casual_relationships']]
graphs.create_bar(
    df_casual_relationships,
    'casual_relationships',
    'number of casual relationships',
    'number of students',
    'casual relationships',
    vertical = True,
    drop_values = [50],
)

df_casual_relationships_meet = df[['casual_relationships_meet']]
graphs.create_bar(
    df_casual_relationships_meet,
    'casual_relationships_meet',
    'places where you met your casual partner',
    'number of students',
    'meeting casual relationships',
    vertical = True,
    splice_required = True,
    drop_values = ['I have not participated in a casual relationship'],
    title_label_rotation_angle = 45
)

df_virgin = df[['virgin_before', 'virgin_after']]
graphs.create_bar_stacked(
    df_virgin,
    ['virgin_before', 'virgin_after'],
    'are you a virgin?',
    'percent of class',
    "let's play 21 questions",
    vertical = False,
    display_as_percentage = True,
    file_name='virginity'
)

df_unique_sex_partners = df[['unique_sex_partners']]
graphs.create_bar(
    df_unique_sex_partners,
    'unique_sex_partners',
    'unique sexual partners',
    'number of students',
    'Unique sexual partners',
    vertical = True,
    drop_values = [42]
)

df_first_sex = df[['first_sex']]
first_sex_labels = ['Before high school', 'High school', '1A', '1A Co-op', '1B', '1B Co-op', '2A', '2A Co-op', '2B', '2B Co-op', '3A', '3A Co-op', '3B', '3B Co-op', '4A', '4B', 'I have not engaged in sexual activity']
first_sex_labels.reverse()
graphs.create_bar(
    df_first_sex,
    'first_sex',
    'term',
    'number of students',
    'Time of first sexual activity',
    vertical = False,
    labels = first_sex_labels
)

list_hye_sex = ['hye_hold_hands',
 'hye_date',
 'hye_kissed',
 'hye_relationship',
 'hye_nudes',
 'hye_oral',
 'hye_hooked_up']
df_hye_sex = df[list_hye_sex]
graphs.create_bar_stacked(
    df_hye_sex,
    list_hye_sex,
    'have you ever...',
    'percent of students',
    'have you ever...',
    vertical = False,
    display_as_percentage = True,
    labels = ['Experienced before university', 'Experienced during university', 'No'],
    file_name='have_you_ever_done_these_sex_acts'
)

list_drugs = ['first_caffeine',
 'first_alcohol',
 'first_weed',
 'first_cigs',
 'first_vape',
 'first_mdma',
 'first_adderall',
 'first_shrooms',
 'first_lsd',
 'first_cocaine',
 'first_dmt',
 'first_ketamine',
 'first_opiods']

df_drugs = df[list_drugs]
graphs.create_bar_stacked(
    df_drugs,
    list_drugs,
    'drugs',
    'percent of students',
    "it's a gateway drug man don't do it",
    vertical = False,
    display_as_percentage = True,
    labels = ['First tried before university', 'First tried during university', 'Have not tried'],
    file_name='first_drugs'
)

list_drug_milestones = ['Gone to class drunk', 'Taken a test / exam drunk', 'Blacked out from alcohol', 'Gone to class high', 'Taken a test / exam high', 'Greened out from marijuana', 'I have not done any of these']
list_drug_milestones.reverse()
df_drug_milestones = df[['hye_drugs']]
graphs.create_bar(
    df_drug_milestones,
    'hye_drugs',
    'Experiences',
    'Percentage of Students',
    'Drug Milestones',
    vertical = False,
    splice_required = True,
    labels = list_drug_milestones,
    values_increment = 5
)

list_syde_lounge = ['hye_lounge_drank',
 'hye_lounge_weed',
 'hye_lounge_drugs',
 'hye_lounge_sex']
df_syde_lounge = df[list_syde_lounge]
graphs.create_bar_stacked(
    df_syde_lounge,
    list_syde_lounge,
    'syde lounge acts',
    'percent of respondents',
    'private private lounge',
    vertical = False,
    display_as_percentage = True,
    labels = ['Yes', 'No'],
    file_name='syde_lounge_activities'
)

df_showers = df[['showers_week']]
graphs.create_bar(
    df_showers,
    'showers_week',
    'number of showers',
    'percentage of respondents',
    'How many showers do you take in a week (you filthy animals)',
    vertical = True,
    values_increment = 5
)