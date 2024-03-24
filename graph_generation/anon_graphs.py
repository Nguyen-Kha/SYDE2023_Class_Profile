# necessary imports
import numpy as np
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
    column_labels=['Fabricated data', 'Unauthorized collaboration with others before COVID', 'Used previous course materials', 'Plagiarized', 'Falsified information on resumes', 'Cheated in an in-person test environment before COVID', 'Cheated on a test environment during COVID', 'Received a Policy 71 allegation', 'Placed on Academic or Disciplinary probation'],
    file_name = 'policy_71_core'
)

df_casual_relationships = df[['casual_relationships']]
df_casual_relationships = df_casual_relationships.loc[df_casual_relationships['casual_relationships'] != 50]
df_casual_relationships = df_casual_relationships.dropna()
casual_relationships_list = list(np.arange(0,9,1))

graphs.create_bar(
    df_casual_relationships,
    'casual_relationships',
    'Number of casual relationships',
    'Percentage of respondents',
    'How many casual relationships have you been in',
    vertical = True,
    display_as_percentage=True,
    labels = casual_relationships_list,
    graph_name_labels = casual_relationships_list
)

df_casual_relationships_meet = df[['casual_relationships_meet']]
graphs.create_bar(
    df_casual_relationships_meet,
    'casual_relationships_meet',
    '',
    'Percentage of Respondents',
    'How have you met your partners in casual relationships',
    vertical = False,
    display_as_percentage=True,
    splice_required = True,
    drop_values = ['I have not participated in a casual relationship'],
    values_increment=5
)

df_virgin = df[['virgin_before', 'virgin_after']]
graphs.create_bar_stacked(
    df_virgin,
    ['virgin_before', 'virgin_after'],
    '',
    'percent of class',
    "let's play 21 questions",
    vertical = False,
    display_as_percentage = True,
    column_labels=['Were you a virgin before entering university', 'Were you a virgin after leaving university'],
    file_name='virginity',
    figure_height=5
)

df_unique_sex_partners = df[['unique_sex_partners']]
df_unique_sex_partners = df_unique_sex_partners.dropna()
graphs.create_bar(
    df_unique_sex_partners,
    'unique_sex_partners',
    'Number of unique sexual partners',
    'Percentage of respondents',
    'How many unique sexual partners have you had',
    vertical = True,
    display_as_percentage=True,
    labels = list(np.arange(0, 10, 1)),
    graph_name_labels=list(np.arange(0, 10, 1)),
    drop_values = [42],
    values_increment=5
)

df_first_sex = df[['first_sex']]
first_sex_labels = ['Before high school', 'High school', '1A', '1A Co-op', '1B', '1B Co-op', '2A', '2A Co-op', '2B', '2B Co-op', '3A', '3A Co-op', '3B', '3B Co-op', '4A', '4B', 'I have not engaged in sexual activity']
graphs.create_bar(
    df_first_sex,
    'first_sex',
    'Term',
    'Percentage of respondents',
    'First occurence of sexual activity',
    vertical = False,
    display_as_percentage=True,
    labels = first_sex_labels,
    values_increment= 2
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
    '',
    'Percentage of respondents',
    'Rice Purity',
    vertical = False,
    display_as_percentage = True,
    labels = ['Experienced before university', 'Experienced during university', 'No'],
    column_labels = ['Held hands romantically', 'Been on a date', 'Kissed a member of the preferred sex', 'Been in a relationship', 'Sent or received nudes', 'Given or received oral sex', 'Hooked up with someone'],
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
    column_labels = ['Caffeine', 'Alcohol', 'Marijuana', 'Cigarettes', 'Vaping', 'MDMA', 'Adderall', 'Psylocibin', 'LSD', 'Cocaine', 'DMT', 'Ketamine', 'Opiods'],
    file_name='first_drugs'
)

list_drug_milestones = ['Gone to class drunk', 'Taken a test / exam drunk', 'Blacked out from alcohol', 'Gone to class high', 'Taken a test / exam high', 'Greened out from marijuana', 'I have not done any of these']
df_drug_milestones = df[['hye_drugs']]
graphs.create_bar(
    df_drug_milestones,
    'hye_drugs',
    '',
    'Percentage of Students',
    'Drug Milestones',
    vertical = False,
    display_as_percentage=True,
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
    '',
    'percent of respondents',
    'private private lounge',
    vertical = False,
    display_as_percentage = True,
    labels = ['Yes', 'No'],
    column_labels=['Drank in the SYDE lounge', 'Consumed marijuana in the SYDE lounge', 'Done harder drugs in the SYDE lounge', 'Engaged in sexual activity in the SYDE lounge'],
    figure_height= 6,
    file_name='syde_lounge_activities'
)

df_showers = df[['showers_week']]
df_showers = df_showers.dropna()
graphs.create_bar(
    df_showers,
    'showers_week',
    'number of showers',
    'percentage of respondents',
    'How many showers do you take in a week (you filthy animals)',
    vertical = True,
    labels = list(np.arange(0, 15, 1)),
    graph_name_labels=list(np.arange(0, 15, 1)),
    display_as_percentage=True,
    values_increment = 5
)