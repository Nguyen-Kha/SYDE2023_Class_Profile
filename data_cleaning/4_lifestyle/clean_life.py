import numpy as np
import pandas as pd
import math
from sklearn.preprocessing import MultiLabelBinarizer

###### DEV VARIABLES ########
input_csv_path = 'C:\\Users\\Kha\\Documents\\Programming\\SYDE2023_Class_Profile\\csv\\raw\\4_LIFE.csv'
output_rename_column_path = 'C:\\Users\\Kha\\Documents\\Programming\\SYDE2023_Class_Profile\\csv\\renamed_columns\\4_LIFE_renamed.csv'
output_pii_path = 'C:\\Users\\Kha\\Documents\\Programming\\SYDE2023_Class_Profile\\csv\\final\\4_LIFE_PII_final.csv'
output_standard_path = 'C:\\Users\\Kha\\Documents\\Programming\\SYDE2023_Class_Profile\\csv\\final\\4_LIFE_final.csv'
output_split_path = 'C:\\Users\\Kha\\Documents\\Programming\\SYDE2023_Class_Profile\\csv\\final\\split\\'

##### GLOBAL #######
yes_calied_list = []
yes_busted_list = []
syde_mentee_list = []
syde_mentor_list = []
coffee_chat_1a = []
coffee_chat_4a = []
resume_first_year = []
resume_upper_year = []
mock_int_first_year = []
mock_int_upper_year = []
syde_trad_dne = []
give_advice = []
receive_advice = []
job_give = []
job_receive = []
dated_lower = []
dated_upper = []
syde_acts_dne = []
addiction = []
adhd = []
anxiety = []
depression = []
disassociation = []
ed = []
ocd = []
ptsd = []
sleeping = []
suicidal = []
mh_none = []

###### MAPPINGS #########
syde_trad_dict = {
    'mentee': False,
    'mentor': False,
    'coffee_1a': False,
    'coffee_4a': False,
    'resume_first': False,
    'resume_upper': False,
    'int_first': False,
    'int_upper': False,
    'dne': False
}

syde_acts_dict = {
    'give_advice': False,
    'receive_advice': False,
    'job_give': False,
    'job_receive': False,
    'dated_lower': False,
    'dated_upper': False,
    'dne': False
}

mh_dict = {
    'addiction': False,
    'adhd': False,
    'anxiety': False,
    'depression': False,
    'disassociation': False,
    'ed': False,
    'ocd': False,
    'ptsd': False,
    'sleeping': False,
    'suicidal': False,
    'mh_none': False
}

friends_programs_dict = {
    'AE': 'Architectural Engineering',
    'AFM': 'Accounting and Financial Management',
    'ARBUS': 'Arts and Business',
    'Anthropology': 'Anthropology',
    'ArBus': 'Arts and Business',
    'Architectural Eng': 'Architectural Engineering',
    'Architectural Engineering': 'Architectural Engineering',
    'Arts & Business': 'Arts and Business',
    'BME': 'Biomedical Engineering',
    'Bio': 'Biology',
    'Biochemistry': 'Biochemistry',
    'Biomed Eng': 'Biomedical Engineering',
    'Biomedical Engineering': 'Biomedical Engineering',
    'Business': 'Business',
    'CHE': 'Chemical Engineering',
    'CPA': 'Chartered Professional Accountancy',
    'CS': 'Computer Science',
    'Chemical Engineering': 'Chemical Engineering',
    'Civil': 'Civil Engineering',
    'Computer Engineering': 'Computer Engineering',
    'Computer Science': 'Computer Science',
    'ECE': 'Electrical and Computer Engineering',
    'ENVE': 'Environmental Engineering',
    'Electrical Engineering': 'Electrical Engineering',
    'Enviro Eng and chemical Eng': 'Environmental Engineering, Chemical Engineering',
    'Environment': 'Environment',
    'Environment Faculty': 'Environment',
    'Environmental Engineering': 'Environmental Engineering',
    'GBDA': 'Global Buisness and Digital Arts',
    'Geomatics': 'Geomatics',
    'Kin': 'Kinesiology',
    'MGTE': 'Management Engineering',
    'Management Engineering': 'Management Engineering',
    'Management eng': 'Management Engineering',
    'Masters in Education': 'Masters in Education',
    'Math': 'Mathematics',
    'Mech': 'Mechanical Engineering',
    'Mechanical Engineering': 'Mechanical Engineering',
    'Mechatronics': 'Mechatronics Engineering',
    'Mechatronics Engineering': 'Mechatronics Engineering',
    'Mechatronics eng': 'Mechatronics Engineering',
    'Nano': 'Nanotechnology Engineering',
    'Nano Eng': 'Nanotechnology Engineering',
    'Nano Engineering': 'Nanotechnology Engineering',
    'Nano engineering': 'Nanotechnology Engineering',
    'Nanotech Engineering': 'Nanotechnology Engineering',
    'Nanotechnology': 'Nanotechnology Engineering',
    'Nanotechnology Engineering': 'Nanotechnology Engineering',
    'Optometry': 'Optometry',
    'Pharmacy': 'Pharmacy',
    'Physics and Astronomy': 'Physics and Astronomy',
    'Planning': 'Planning',
    'Psychology': 'Psychology',
    'Rec and Leisure': 'Recreation and Leisure Studies',
    'SE': 'Software Engineering',
    'SciBus': 'Science and Business',
    'Science': 'Science',
    'Software': 'Software Engineering',
    'Software Engineering': 'Software Engineering',
    'Tron': 'Mechatronics Engineering',
    'Urban Planning': 'Planning',
    'bba': 'Business',
    'biochemistry': 'Biochemistry',
    'biomedical science': 'Biomedical Sciences',
    'computer science': 'Computer Science',
    'etc.': '',
    'gbda': 'Global Business and Digital Arts',
    'geomatics': 'Geomatics',
    'health sciences': 'Health Sciences',
    'kinesiology': 'Kinesiology',
    'knowledge integration': 'Knowledge Integration',
    'math': 'Mathematics',
    'psych': 'Psychology',
    'software engineering': 'Software Engineering',
    'tron': 'Mechatronics Engineering',
    'urban planning': 'Planning'
}

######## FUNCTIONS #############

def rename_column_headers(df):
    df = df.rename(columns = {
        "What is your unique ID" : "uid",
        "How many hours a term on average did you spend on side projects" : "side_project_hours",
        "How many hackathons / designathons / datathons / engineering competitions have you participated in during your undergrad career" : "hackathons",
        "Regarding hackathon (and other associated competitions) wins, select the statement that best relates to you" : "hackathon_results",
        "For the following terms, select which activities you participated in [1A (Fall 2018)]" : "prof_ec_1a",
        "For the following terms, select which activities you participated in [1A Co-op (Winter 2019)]" : "prof_ec_c1",
        "For the following terms, select which activities you participated in [1B (Spring 2019)]" : "prof_ec_1b",
        "For the following terms, select which activities you participated in [1B Co-op (Fall 2019)]" : "prof_ec_c2",
        "For the following terms, select which activities you participated in [2A (Winter 2020)]" : "prof_ec_2a",
        "For the following terms, select which activities you participated in [2A Co-op (Spring 2020)]" : "prof_ec_c3",
        "For the following terms, select which activities you participated in [2B (Fall 2020)]" : "prof_ec_2b",
        "For the following terms, select which activities you participated in [2B Co-op (Winter 2021)]" : "prof_ec_c4",
        "For the following terms, select which activities you participated in [3A (Spring 2021)]" : "prof_ec_3a",
        "For the following terms, select which activities you participated in [3A Co-op (Fall 2021)]" : "prof_ec_c5",
        "For the following terms, select which activities you participated in [3B (Winter 2022)]" : "prof_ec_3b",
        "For the following terms, select which activities you participated in [3B Co-op (Spring 2022)]" : "prof_ec_c6",
        "For the following terms, select which activities you participated in [4A (Fall 2022)]" : "prof_ec_4a",
        "For the following terms, select which activities you participated in [4B (Spring 2023)]" : "prof_ec_4b",
        "Have you ever ... [Worked on an entrepreneurial venture during undergrad]" : "hye_enterpreneur",
        "Have you ever ... [Participated in varsity athletics]" : "hye_varsity",
        "Have you ever ... [Published Research]" : "hye_research",
        "Have you ever ... [Started a club]" : "hye_start_club",
        "In these career-based extracurriculars, what type of role did you mainly play " : "prof_ec_role",
        "Outside of coursework, did you work on any projects involving the following: [Mechanical Systems]" : "mech_projects",
        "Outside of coursework, did you work on any projects involving the following: [Electrical Systems]" : "elec_projects",
        "Outside of coursework, did you work on any projects involving the following: [Computer Systems]" : "comp_projects",
        "What are your disciplines of interest?" : "disciplines_of_interest",
        "Have you ever tried to 'Cali or Bust'?" : "cali_or_bust",
        "Which unique extracurriculars (both fun and professional) were you regularly participating in?" : "consistent_ec",
        "How many friends did you make during undergrad" : "friends_undergrad",
        "How many friends do you have in SYDE 2023" : "friends_syde",
        "From the people who you consider to be your 5 closest friends, how many of them are in SYDE?" : "friends_syde_5",
        "I felt that the class was very cliquey" : "clique",
        "If you had non-SYDE friends, which programs were they in?" : "non_syde_friends_program",
        "For all of your school terms, how many SYDE roommates did you live with?" : "syde_roommates_study",
        "For all of your school terms, how many roommates (both SYDE and non-SYDE) did you have in total?" : "roommates_study",
        "For all of your co-op terms, how many SYDE roommates did you live with?" : "syde_roommates_coop",
        "For all of your co-op terms, how many roommates (both SYDE and non-SYDE) did you have in total?" : "roommates_coop",
        "Did you attend at least one SYDE event during the following terms [1A]" : "syde_event_1a",
        "Did you attend at least one SYDE event during the following terms [1B]" : "syde_event_1b",
        "Did you attend at least one SYDE event during the following terms [2A]" : "syde_event_2a",
        "Did you attend at least one SYDE event during the following terms [2B]" : "syde_event_2b",
        "Did you attend at least one SYDE event during the following terms [3A]" : "syde_event_3a",
        "Did you attend at least one SYDE event during the following terms [4A]" : "syde_event_4a",
        "Did you attend at least one SYDE event during the following terms [4B]" : "syde_event_4b",
        "Did you participate in the following" : "syde_traditions",
        "Have you ever syde" : "syde_acts",
        "How many upper year SYDEs are you still in contact with" : "upper_year_sydes",
        "How many lower year SYDEs are you still in contact with" : "lower_year_sydes",
        "During your undergrad career, how many serious relationships have you been in?" : "serious_relationships",
        "How did you meet your partners in your serious relationships?" : "serious_relationships_meet",
        "How many months in your undergrad career was spent in a serious relationship?" : "serious_relationship_month_undergrad",
        "In months, how long was your longest serious relationship?" : "serious_relationships_longest",
        "Did you commit SYDEcest" : "sydecest",
        "If you did not commit SYDEcest, did you want to?" : "sydecest_wishful",
        "If you committed SYDEcest, with how many different classmates did you commit it with" : "sydecest_people",
        "For the following terms, state your level of alcohol consumption [1A]" : "alcohol_1a",
        "For the following terms, state your level of alcohol consumption [1A Co-op]" : "alcohol_c1",
        "For the following terms, state your level of alcohol consumption [1B]" : "alcohol_1b",
        "For the following terms, state your level of alcohol consumption [1B Co-op]" : "alcohol_c2",
        "For the following terms, state your level of alcohol consumption [2A]" : "alcohol_2a",
        "For the following terms, state your level of alcohol consumption [2A Co-op]" : "alcohol_c3",
        "For the following terms, state your level of alcohol consumption [2B]" : "alcohol_2b",
        "For the following terms, state your level of alcohol consumption [2B Co-op]" : "alcohol_c4",
        "For the following terms, state your level of alcohol consumption [3A]" : "alcohol_3a",
        "For the following terms, state your level of alcohol consumption [3A Co-op]" : "alcohol_c5",
        "For the following terms, state your level of alcohol consumption [3B]" : "alcohol_3b",
        "For the following terms, state your level of alcohol consumption [3B Co-op]" : "alcohol_c6",
        "For the following terms, state your level of alcohol consumption [4A]" : "alcohol_4a",
        "For the following terms, state your level of alcohol consumption [4B]" : "alcohol_4b",
        "For the following terms, state your level of marijuana consumption [1A]" : "weed_1a",
        "For the following terms, state your level of marijuana consumption [1A Co-op]" : "weed_c1",
        "For the following terms, state your level of marijuana consumption [1B]" : "weed_1b",
        "For the following terms, state your level of marijuana consumption [1B Co-op]" : "weed_c2",
        "For the following terms, state your level of marijuana consumption [2A]" : "weed_2a",
        "For the following terms, state your level of marijuana consumption [2A Co-op]" : "weed_c3",
        "For the following terms, state your level of marijuana consumption [2B]" : "weed_2b",
        "For the following terms, state your level of marijuana consumption [2B Co-op]" : "weed_c4",
        "For the following terms, state your level of marijuana consumption [3A]" : "weed_3a",
        "For the following terms, state your level of marijuana consumption [3A Co-op]" : "weed_c5",
        "For the following terms, state your level of marijuana consumption [3B]" : "weed_3b",
        "For the following terms, state your level of marijuana consumption [3B Co-op]" : "weed_c6",
        "For the following terms, state your level of marijuana consumption [4A]" : "weed_4a",
        "For the following terms, state your level of marijuana consumption [4B]" : "weed_4b",
        "For the following terms, state how often you partied [1A]" : "party_1a",
        "For the following terms, state how often you partied [1B]" : "party_1b",
        "For the following terms, state how often you partied [2A]" : "party_2a",
        "For the following terms, state how often you partied [2B]" : "party_2b",
        "For the following terms, state how often you partied [3A]" : "party_3a",
        "For the following terms, state how often you partied [3B]" : "party_3b",
        "For the following terms, state how often you partied [4A]" : "party_4a",
        "For the following terms, state how often you partied [4B]" : "party_4b",
        "What is your favourite food place in the plaza?" : "plaza_food",
        "What is your favourite restaurant in the KW region?" : "kw_food",
        "On average, how many times did you cook per week during a school term?" : "cook_school",
        "On average, how many times did you eat out per week during a school term?" : "eat_out_school",
        "How would you rate your cooking ability ... [In 1st year]" : "cooking_ability_1",
        "How would you rate your cooking ability ... [In 4th year]" : "cooking_ability_4",
        "What sports / fitness activities (intramural, personal, professional, etc.) did you participate in during your undergrad career" : "sports",
        "What are some of your hobbies? (aka what do you like to do for fun?)" : "hobbies",
        "Have you ever milestones" : "hye_milestones",
        "How many times have you slept in the SYDE Lounge?" : "sleep_syde_lounge",
        "How often did you exercise in ... [Grade 12 / Pre-University]" : "exercise_g12",
        "How often did you exercise in ... [1st year]" : "exercise_1",
        "How often did you exercise in ... [2nd year]" : "exercise_2",
        "How often did you exercise in ... [3rd year]" : "exercise_3",
        "How often did you exercise in ... [4th year]" : "exercise_4",
        "What is your perceived fitness level in [Grade 12 / Pre University]" : "fitness_level_g12",
        "What is your perceived fitness level in [4th year]" : "fitness_level_4",
        "What time did you usually go to sleep during an academic term?" : "sleep_time",
        "What kind of mental health challenges did you experience throughout the course of the degree" : "mental_health_challenges",
        "What were some sources of mental health concerns, or affected your mental health negatively" : "mental_health_bad_sources",
        "What type of support did you seek out for your mental health challenges" : "mental_health_support_types",
        "Did you seek out professional mental health support at any point in your undergrad career" : "mental_health_professional",
        "Have you ever helped a friend through a mental health crisis?" : "mental_health_friend_crisis",
        "Have you experienced Imposter Syndrome at any point in your undergrad career" : "impostor_syndrome",
        "UWaterloo provided adequate mental health support for its students" : "uwaterloo_mental_health_support",
        "How many times have you cried on campus" : "cry_on_campus",
        "Where have you cried on campus" : "cry_on_campus_locations"
    })

    return df

def encode_cali_or_bust(df):
    global yes_calied_list
    global yes_busted_list
    
    df['cali_or_bust'].apply(parse_cali_or_bust)
    df_cali_or_bust = concat_cali_or_bust_df()
    
    return df_cali_or_bust
    
def parse_cali_or_bust(answer):
    global yes_calied_list
    global yes_busted_list
    
    if(type(answer) == float):
        if(math.isnan(answer)):
            yes_calied_list.append(np.nan)
            yes_busted_list.append(np.nan)
            return None        
    
    if("busted" in answer.lower() and "cali" in answer.lower()):
        yes_calied_list.append(1)
        yes_busted_list.append(1)
    elif(answer == "Yes, Busted"):
        yes_calied_list.append(0)
        yes_busted_list.append(1)
    elif(answer == "Yes, Cali-ed"):
        yes_calied_list.append(1)
        yes_busted_list.append(0)
    elif(answer == "No"):
        yes_calied_list.append(0)
        yes_busted_list.append(0)
    else:
        if("busted" in answer.lower()):
            yes_calied_list.append(0)
            yes_busted_list.append(1)
        elif("cali" in answer.lower()):
            yes_calied_list.append(1)
            yes_busted_list.append(0)
        else:
            yes_calied_list.append(np.nan)
            yes_busted_list.append(np.nan)
    
    # no return

def concat_cali_or_bust_df():
    global yes_calied_list
    global yes_busted_list
    
    df_extended = pd.DataFrame({
        "cali_or_bust_cali": yes_calied_list,
        "cali_or_bust_bust": yes_busted_list
    })
    
    return df_extended

def encode_syde_traditions(df):
    global syde_trad_dict
    
    reset_syde_traditions_dict()
    df['syde_traditions'].apply(parse_syde_traditions)
    df_syde_traditions = concat_syde_traditions()
    
    return df_syde_traditions
    

def parse_syde_traditions(answer):
    global syde_trad_dict
    global syde_mentee_list
    global syde_mentor_list
    global coffee_chat_1a
    global coffee_chat_4a
    global resume_first_year
    global resume_upper_year
    global mock_int_first_year
    global mock_int_upper_year
    global syde_trad_dne
    
    reset_syde_traditions_dict()
    
    if(type(answer) == float):
        if(math.isnan(answer)):
            syde_mentee_list.append(np.nan)
            syde_mentor_list.append(np.nan)
            coffee_chat_1a.append(np.nan)
            coffee_chat_4a.append(np.nan)
            resume_first_year.append(np.nan)
            resume_upper_year.append(np.nan)
            mock_int_first_year.append(np.nan)
            mock_int_upper_year.append(np.nan)
            syde_trad_dne.append(np.nan)
            return None
    
    individual_traditions = answer.split(",")
    for i in individual_traditions:
        i = i.strip()
        if(i == "Being a SYDE mentee"):
            syde_mentee_list.append(1)
            syde_trad_dict['mentee'] = True
        if(i == "Being a SYDE mentor"):
            syde_mentor_list.append(1)
            syde_trad_dict['mentor'] = True
        if(i == "1A <> 4A SYDE Coffee Chats as a 1A"):
            coffee_chat_1a.append(1)
            syde_trad_dict['coffee_1a'] = True
        if(i == "4A <> 1A SYDE Coffee Chats as a 4A"):
            coffee_chat_4a.append(1)
            syde_trad_dict['coffee_4a'] = True
        if(i == "SYDE Resume Critiques as a first year"):
            resume_first_year.append(1)
            syde_trad_dict['resume_first'] = True
        if(i == "SYDE Resume Critiques as an upper year"):
            resume_upper_year.append(1)
            syde_trad_dict['resume_upper'] = True
        if(i == "SYDE Mock Interviews as a first year"):
            mock_int_first_year.append(1)
            syde_trad_dict['int_first'] = True
        if(i == "SYDE Mock Interviews as an upper year"):
            mock_int_upper_year.append(1)
            syde_trad_dict['int_upper'] = True
        if(i == "I did not participate in any of these"):
            syde_trad_dne.append(1)
            syde_trad_dict['dne'] = True
    
    # Read dictionary and update values that don't exist
    if(not syde_trad_dict['mentee']):
        syde_mentee_list.append(0)
    if(not syde_trad_dict['mentor']):
        syde_mentor_list.append(0)
    if(not syde_trad_dict['coffee_1a']):
        coffee_chat_1a.append(0)
    if(not syde_trad_dict['coffee_4a']):
        coffee_chat_4a.append(0)
    if(not syde_trad_dict['resume_first']):
        resume_first_year.append(0)
    if(not syde_trad_dict['resume_upper']):
        resume_upper_year.append(0)
    if(not syde_trad_dict['int_first']):
        mock_int_first_year.append(0)
    if(not syde_trad_dict['int_upper']):
        mock_int_upper_year.append(0)
    if(not syde_trad_dict['dne']):
        syde_trad_dne.append(0)
        
    reset_syde_traditions_dict()

def concat_syde_traditions():
    global syde_mentee_list
    global syde_mentor_list
    global coffee_chat_1a
    global coffee_chat_4a
    global resume_first_year
    global resume_upper_year
    global mock_int_first_year
    global mock_int_upper_year
    global syde_trad_dne
    
    df_extended = pd.DataFrame({
        "syde_traditions_mentee": syde_mentee_list,
        "syde_traditions_mentor": syde_mentor_list,
        "syde_traditions_coffee_1a": coffee_chat_1a,
        "syde_traditions_coffee_4a": coffee_chat_4a,
        "syde_traditions_resume_first": resume_first_year,
        "syde_traditions_resume_upper": resume_upper_year,
        "syde_traditions_mock_int_first": mock_int_first_year,
        "syde_traditions_mock_int_upper": mock_int_upper_year,
        "syde_traditions_none": syde_trad_dne
    })
    
    return df_extended

def reset_syde_traditions_dict():
    global syde_trad_dict
    
    syde_trad_dict = {
        'mentee': False,
        'mentor': False,
        'coffee_1a': False,
        'coffee_4a': False,
        'resume_first': False,
        'resume_upper': False,
        'int_first': False,
        'int_upper': False,
        'dne': False
    }

def encode_syde_acts(df):
    global syde_acts_dict
    
    reset_syde_acts_dict()
    df['syde_acts'].apply(parse_syde_acts)
    df_syde_acts = concat_syde_acts()
    
    return df_syde_acts

def parse_syde_acts(answer):
    global syde_acts_dict
    global give_advice
    global receive_advice
    global job_give
    global job_receive
    global dated_lower
    global daetd_upper
    global syde_acts_dne
    
    reset_syde_acts_dict()
    
    if(type(answer) == float):
        if(math.isnan(answer)):
            give_advice.append(np.nan)
            receive_advice.append(np.nan)
            job_give.append(np.nan)
            job_receive.append(np.nan)
            dated_lower.append(np.nan)
            dated_upper.append(np.nan)
            syde_acts_dne.append(np.nan)
            return None
    
    individual_acts = answer.split(",")
    for i in individual_acts:
        i = i.strip()
        if(i == "Given advice to a lower year SYDE"):
            give_advice.append(1)
            syde_acts_dict['give_advice'] = True
        elif(i == "Received advice from an upper year SYDE"):
            receive_advice.append(1)
            syde_acts_dict['receive_advice'] = True
        elif(i == "Given a job referral to a lower year SYDE"):
            job_give.append(1)
            syde_acts_dict['job_give'] = True
        elif(i == "Received a job referral from an upper year SYDE"):
            job_receive.append(1)
            syde_acts_dict['job_receive'] = True
        elif(i == "Dated a lower year SYDE"):
            dated_lower.append(1)
            syde_acts_dict['dated_lower'] = True
        elif(i == "Dated an upper year SYDE"):
            dated_upper.append(1)
            syde_acts_dict['dated_upper'] = True
        elif(i == "I did not do any of these"):
            syde_acts_dne.append(1)
            syde_acts_dict['dne'] = True
    
    if(not syde_acts_dict['give_advice']):
        give_advice.append(0)
    if(not syde_acts_dict['receive_advice']):
        receive_advice.append(0)
    if(not syde_acts_dict['job_give']):
        job_give.append(0)
    if(not syde_acts_dict['job_receive']):
        job_receive.append(0)
    if(not syde_acts_dict['dated_lower']):
        dated_lower.append(0)
    if(not syde_acts_dict['dated_upper']):
        dated_upper.append(0)
    if(not syde_acts_dict['dne']):
        syde_acts_dne.append(0)
        
    reset_syde_acts_dict()

def concat_syde_acts():
    global give_advice
    global receive_advice
    global job_give
    global job_receive
    global dated_lower
    global dated_upper
    global syde_acts_dne
    
    df_extended = pd.DataFrame({
        'syde_acts_give_advice': give_advice,
        'syde_acts_receive_advice': receive_advice,
        'syde_acts_job_give': job_give,
        'syde_acts_job_receive': job_receive,
        'syde_acts_dated_lower': dated_lower,
        'syde_acts_dated_upper': dated_upper,
        'syde_acts_none': syde_acts_dne
    })
    
    return df_extended

def reset_syde_acts_dict():
    global syde_acts_dict
    
    syde_acts_dict = {
        'give_advice': False,
        'receive_advice': False,
        'job_give': False,
        'job_receive': False,
        'dated_lower': False,
        'dated_upper': False,
        'dne': False
    }

def remove_comma_for_milestones(answer):
    if(type(answer) == float):
        if(math.isnan(answer)):
            return answer
    
    if("Been to Brixton's, Chainsaw's, Becky's Apartment, Night School, Stark and Perri's, or Bomber Wednesday's before they closed down" in answer):
        answer = answer.replace(
            "Been to Brixton's, Chainsaw's, Becky's Apartment, Night School, Stark and Perri's, or Bomber Wednesday's before they closed down",
            "Been to Brixton's Chainsaw's Becky's Apartment Night School Stark and Perri's or Bomber Wednesday's before they closed down"
        )
    
    return answer

def encode_milestones(df):
    
    mlb = MultiLabelBinarizer()
    df_extended = pd.DataFrame(mlb.fit_transform(df['hye_milestones'].apply(convert_string_to_list)), columns=mlb.classes_)
    return df_extended
    pass

def convert_string_to_list(answer):
    if(type(answer) == float):
        if(math.isnan(answer)):
            return answer
        
    return answer.split(", ")

def rename_hye_milestones(df):
    df = df.rename(columns = {
        "Attended a Sex Toy Bingo": "hye_milestones_bingo",
        "Attended an EngPlay": "hye_milestones_engplay",
        "Attended an EngSoc Semi Formal": "hye_milestones_semi",
        "Been chased by a goose": "hye_milestones_goose",
        "Been to Brixton's Chainsaw's Becky's Apartment Night School Stark and Perri's or Bomber Wednesday's before they closed down": "hye_milestones_old_bar",
        "Been to Ezra for Hoco / St Paddys": "hye_milestones_ezra",
        "Been to Phil's": "hye_milestones_phils",
        "Been to a GradComm PubCrawl": "hye_milestones_pubcrawl",
        "Been to a bar": "hye_milestones_bar",
        "Been to a night club": "hye_milestones_club",
        "Did photoshoots around campus": "hye_milestones_photoshoots",
        "Dressed up for a costume themed event": "hye_milestones_costume",
        "Explored the KW region": "hye_milestones_kw",
        "Flirted with a TA": "hye_milestones_flirt_ta",
        "Flirted with a professor": "hye_milestones_flirt_prof",
        "I did not participate in any of these": "hye_milestones_none",
        "Invested money for the first time": "hye_milestones_invest",
        "Joined an intramural sports team": "hye_milestones_sports",
        "Participated in B.O.A.T.S.": "hye_milestones_boats",
        "Participated in Orientation Week as a leader": "hye_milestones_oweek_leader",
        "Participated in an Engineering Competition": "hye_milestones_eng_comp",
        "Performed at Coffee House": "hye_milestones_coffee_house",
        "Pretended to be a Laurier Golden Hawk": "hye_milestones_laurier",
        "Pulled an all-nighter on campus": "hye_milestones_all_nighter",
        "Rode the bull at Dallas": "hye_milestones_dallas",
        "Survived a full day on free food": "hye_milestones_free_food",
        "Visited International News in the SLC between the hours of 2 AM - 5 AM": "hye_milestones_inews",
        "Went on a spontaneous road trip": "hye_milestones_road_trip"
    })
    
    return df

def encode_mh(df):
    reset_mh_dict()
    df['mental_health_challenges'].apply(parse_mh)
    df_mh = concat_mh_df()
    return df_mh
    

def parse_mh(answer):
    global addiction
    global adhd
    global anxiety
    global depression
    global disassociation
    global ed
    global ocd
    global ptsd
    global sleeping
    global suicidal
    global mh_none
    global mh_dict
    
    reset_mh_dict()
    
    if(type(answer) == float):
        if(math.isnan(answer)):
            addiction.append(np.nan)
            adhd.append(np.nan)
            anxiety.append(np.nan)
            depression.append(np.nan)
            disassociation.append(np.nan)
            ed.append(np.nan)
            ocd.append(np.nan)
            ptsd.append(np.nan)
            sleeping.append(np.nan)
            suicidal.append(np.nan)
            mh_none.append(np.nan)
            return None
        
    individual_mh = answer.split(",")
    for i in individual_mh:
        i = i.strip()
        if(i == 'Addiction'):
            addiction.append(1)
            mh_dict['addiction'] = True
        elif(i == 'ADHD / ADD'):
            adhd.append(1)
            mh_dict['adhd'] = True
        elif(i == 'Anxiety'):
            anxiety.append(1)
            mh_dict['anxiety'] = True
        elif(i == 'Depression'):
            depression.append(1)
            mh_dict['depression'] = True
        elif(i == 'Disassociation'):
            disassociation.append(1)
            mh_dict['disassociation'] = True
        elif(i == 'Eating Disorder'):
            ed.append(1)
            mh_dict['ed'] = True
        elif(i == 'Obsessive Compulsive Disorder (OCD)'):
            ocd.append(1)
            mh_dict['ocd'] = True
        elif(i == 'PTSD'):
            ptsd.append(1)
            mh_dict['ptsd'] = True
        elif(i == 'Sleeping Disorders'):
            sleeping.append(1)
            mh_dict['sleeping'] = True
        elif(i == 'Suicidal Ideation'):
            suicidal.append(1)
            mh_dict['suicidal'] = True
        elif(i == 'I did not experience any mental health challenges'):
            mh_none.append(1)
            mh_dict['mh_none'] = True
        
    if(not mh_dict['addiction']):
        addiction.append(0)
    if(not mh_dict['adhd']):
        adhd.append(0)
    if(not mh_dict['anxiety']):
        anxiety.append(0)
    if(not mh_dict['depression']):
        depression.append(0)
    if(not mh_dict['disassociation']):
        disassociation.append(0)
    if(not mh_dict['ed']):
        ed.append(0)
    if(not mh_dict['ocd']):
        ocd.append(0)
    if(not mh_dict['ptsd']):
        ptsd.append(0)
    if(not mh_dict['sleeping']):
        sleeping.append(0)
    if(not mh_dict['suicidal']):
        suicidal.append(0)
    if(not mh_dict['mh_none']):
        mh_none.append(0)
    
    reset_mh_dict()

def concat_mh_df():
    global addiction
    global adhd
    global anxiety
    global depression
    global disassociation 
    global ed
    global ocd
    global ptsd
    global sleeping
    global suicidal
    global mh_none
    
    df_extended = pd.DataFrame({
        'mh_addiction': addiction,
        'mh_adhd': adhd,
        'mh_anxiety': anxiety,
        'mh_depression': depression,
        'mh_disassociation': disassociation,
        'mh_eating_disorder': ed,
        'mh_ocd': ocd,
        'mh_ptsd': ptsd,
        'mh_sleeping_disorders': sleeping,
        'mh_suicidal': suicidal,
        'mh_none': mh_none
        
    })
    
    return df_extended

def reset_mh_dict():
    global mh_dict
    mh_dict = {
        'addiction': False,
        'adhd': False,
        'anxiety': False,
        'depression': False,
        'disassociation': False,
        'ed': False,
        'ocd': False,
        'ptsd': False,
        'sleeping': False,
        'suicidal': False,
        'mh_none': False
    }

def clean_friends_programs(answer):
    if(type(answer) == float):
        if(math.isnan(answer)):
            return None
    try:
        answer = answer.replace("etc.", "")
        
        cleaned_friend_program_string = ""
        
        individual_programs = answer.split(",")
        for i in individual_programs:
            cleaned_program = friends_programs_dict[i.strip()]
            
            if (cleaned_friend_program_string == ""):
                cleaned_friend_program_string = cleaned_friend_program_string + cleaned_program
            else:
                cleaned_friend_program_string = cleaned_friend_program_string + ", " + cleaned_program

        return cleaned_friend_program_string
    except:
        return None
    
def clean_perceived_fitness(answer):
    if(type(answer) == float):
        if(math.isnan(answer)):
            return answer
    
    if(answer == "1 (I am not fit)"):
        return 1
    elif(answer == "5 (I live in the gym)"):
        return 5
    else:
        return int(answer)

def adjust_undergrad_relationship_length(answer):
    if(type(answer) == float):
        if(math.isnan(answer)):
            return answer
    
    if(answer > 56):
        return 56
    elif(answer < 0):
        return 0
    else:
        return int(answer)
    
def clean_cooking(answer):
    if(type(answer) == float):
        if(math.isnan(answer)):
            return None
    
    if(answer == '1 (Instant Ramen)'):
        return 1
    elif(answer == '5 (3 Michelin stars)'):
        return 5
    else:
        return int(answer)

def remove_commas_lifestyle(answer):
    if(type(answer) == float):
        if(math.isnan(answer)):
            return None
    
    if('I have participated in a hackathon, but have never won' in answer):
        answer = answer.replace(
            'I have participated in a hackathon, but have never won',
            'I have participated in a hackathon but have never won'
        )
    elif('Career focused clubs (UW/UX, Blueprint, Hack the North organizers)' in answer):
        answer = answer.replace(
            'Career focused clubs (UW/UX, Blueprint, Hack the North organizers)',
            'Career focused clubs'
        )
    elif('Extracurriculars (includes school clubs, design teams, external groups, etc.)' in answer):
        answer = answer.replace(
            'Extracurriculars (includes school clubs, design teams, external groups, etc.)',
            'Extracurriculars'
        )
    elif('Self help (books, podcasts, etc.)' in answer):
        answer = answer.replace(
            'Self help (books, podcasts, etc.)',
            'Self help materials'
        )
    elif('Online communities (reddit, etc.)' in answer):
        answer = answer.replace(
            'Online communities (reddit, etc.)',
            'Online communities'
        )
    elif('Other university resources (support groups, profs, UW staff, etc.)' in answer):
        answer = answer.replace(
            'Other university resources (support groups, profs, UW staff, etc.)',
            'Other university resources'
        )
    elif('No, but I wish I did' in answer):
        answer = answer.replace(
            'No, but I wish I did',
            'No but I wish I did'
        )
    elif('Yes, but no longer' in answer):
        answer = answer.replace(
            'Yes, but no longer',
            'Yes but no longer'
        )
    elif('Yes, but still do' in answer):
        answer = answer.replace(
            'Yes, but still do',
            'Yes but still do'
        )
    
    return answer

###### HELPERS #########
# def parse_unique_milestones(answer):
#     global unique_milestones
#     if(type(answer) == float):
#         if(math.isnan(answer)):
#             return None
#     individual_milestones = answer.split(",")
#     for i in individual_milestones:
#         unique_milestones.append(i.strip())

# friends_programs_list = []
# friends_programs = df['non_syde_friends_program'].str.strip().dropna().tolist()
# for i in friends_programs:
#     temp = i.split(",")
#     for j in temp:
#         friends_programs_list.append(j.strip())
# friends_programs_list = sorted(list(set(friends_programs_list)))

def main():
    df = pd.read_csv(input_csv_path, encoding='utf-8')
    df = df.drop(columns = ['Timestamp', 'Questions Comments Concerns Suggestions Feedback for this section'])

    df_life_clean = rename_column_headers(df)
    df_rename_column = df_life_clean.copy()
    df_rename_column.to_csv(output_rename_column_path, index = False, encoding = 'utf-8')

    df_cali_or_bust = encode_cali_or_bust(df_life_clean)
    df_life_clean = pd.concat([df_life_clean, df_cali_or_bust], axis = 1, join = "inner")

    df_syde_traditions = encode_syde_traditions(df_life_clean)
    df_life_clean = pd.concat([df_life_clean, df_syde_traditions], axis = 1, join = "inner")

    df_syde_acts = encode_syde_acts(df_life_clean)
    df_life_clean = pd.concat([df_life_clean, df_syde_acts], axis = 1, join = "inner")

    df_life_clean['hye_milestones'] = df_life_clean['hye_milestones'].apply(remove_comma_for_milestones)
    df_milestones = encode_milestones(df_life_clean)
    df_milestones = rename_hye_milestones(df_milestones)
    df_life_clean = pd.concat([df_life_clean, df_milestones], axis = 1, join = 'inner')
    

    df_mh = encode_mh(df_life_clean)
    df_life_clean = pd.concat([df_life_clean, df_mh], axis = 1, join = 'inner')

    df_life_clean['non_syde_friends_program'] = df_life_clean['non_syde_friends_program'].apply(clean_friends_programs)

    df_life_clean['fitness_level_g12'] = df_life_clean['fitness_level_g12'].apply(clean_perceived_fitness)
    df_life_clean['fitness_level_4'] = df_life_clean['fitness_level_4'].apply(clean_perceived_fitness)

    df_life_clean['serious_relationship_month_undergrad'] = df_life_clean['serious_relationship_month_undergrad'].apply(adjust_undergrad_relationship_length)
    df_life_clean['cooking_ability_1'] = df_life_clean['cooking_ability_1'].apply(clean_cooking)
    df_life_clean['cooking_ability_4'] = df_life_clean['cooking_ability_4'].apply(clean_cooking)

    df_life_clean['hackathon_results'] = df_life_clean['hackathon_results'].apply(remove_commas_lifestyle)
    df_life_clean['prof_ec_1a'] = df_life_clean['prof_ec_1a'].apply(remove_commas_lifestyle)
    df_life_clean['prof_ec_1b'] = df_life_clean['prof_ec_1b'].apply(remove_commas_lifestyle)
    df_life_clean['prof_ec_2a'] = df_life_clean['prof_ec_2a'].apply(remove_commas_lifestyle)
    df_life_clean['prof_ec_2b'] = df_life_clean['prof_ec_2b'].apply(remove_commas_lifestyle)
    df_life_clean['prof_ec_3a'] = df_life_clean['prof_ec_3a'].apply(remove_commas_lifestyle)
    df_life_clean['prof_ec_3b'] = df_life_clean['prof_ec_3b'].apply(remove_commas_lifestyle)
    df_life_clean['prof_ec_4a'] = df_life_clean['prof_ec_4a'].apply(remove_commas_lifestyle)
    df_life_clean['prof_ec_4b'] = df_life_clean['prof_ec_4b'].apply(remove_commas_lifestyle)
    df_life_clean['prof_ec_c1'] = df_life_clean['prof_ec_c1'].apply(remove_commas_lifestyle)
    df_life_clean['prof_ec_c2'] = df_life_clean['prof_ec_c2'].apply(remove_commas_lifestyle)
    df_life_clean['prof_ec_c3'] = df_life_clean['prof_ec_c3'].apply(remove_commas_lifestyle)
    df_life_clean['prof_ec_c4'] = df_life_clean['prof_ec_c4'].apply(remove_commas_lifestyle)
    df_life_clean['prof_ec_c5'] = df_life_clean['prof_ec_c5'].apply(remove_commas_lifestyle)
    df_life_clean['prof_ec_c6'] = df_life_clean['prof_ec_c6'].apply(remove_commas_lifestyle)

    df_life_clean['mental_health_support_types'] = df_life_clean['mental_health_support_types'].apply(remove_commas_lifestyle)
    df_life_clean['mental_health_professional'] = df_life_clean['mental_health_professional'].apply(remove_commas_lifestyle)
    df_life_clean['impostor_syndrome'] = df_life_clean['impostor_syndrome'].apply(remove_commas_lifestyle)
    
    # df_life_clean.to_csv(output_standard_path, index = False, encoding = 'utf-8')
    df_life_pii = df_life_clean[['consistent_ec', 'sports', 'hobbies']]
    df_life_pii = df_life_pii.sample(frac = 1)
    df_life_no_pii = df_life_clean.drop(columns = ['consistent_ec', 'sports', 'hobbies'])

    df_life_pii.to_csv(output_pii_path, index=False, encoding='utf-8')
    df_life_no_pii.to_csv(output_standard_path, index=False, encoding='utf-8')

    df_pa = df_life_clean[[
        'uid',
        'side_project_hours',
        'hackathons',
        'hackathon_results',
        'prof_ec_1a',
        'prof_ec_c1',
        'prof_ec_1b',
        'prof_ec_c2',
        'prof_ec_2a',
        'prof_ec_c3',
        'prof_ec_2b',
        'prof_ec_c4',
        'prof_ec_3a',
        'prof_ec_c5',
        'prof_ec_3b',
        'prof_ec_c6',
        'prof_ec_4a',
        'prof_ec_4b',
        'hye_enterpreneur',
        'hye_varsity',
        'hye_research',
        'hye_start_club',
        'prof_ec_role',
        'mech_projects',
        'elec_projects',
        'comp_projects',
        'disciplines_of_interest',
        'cali_or_bust',
        'cali_or_bust_cali',
        'cali_or_bust_bust'
    ]]

    df_social = df_life_clean[[
        'uid',
        'friends_undergrad',
        'friends_syde',
        'friends_syde_5',
        'clique',
        'non_syde_friends_program',
        'syde_roommates_study',
        'roommates_study',
        'syde_roommates_coop',
        'roommates_coop'
    ]]

    df_syde_trad = df_life_clean[[
        'uid',
        'syde_event_1a',
        'syde_event_1b',
        'syde_event_2a',
        'syde_event_2b',
        'syde_event_3a',
        'syde_event_4a',
        'syde_event_4b',
        'syde_acts',
        'upper_year_sydes',
        'lower_year_sydes',
        'sleep_syde_lounge',
        'syde_traditions',
        'syde_traditions_mentee',
        'syde_traditions_mentor',
        'syde_traditions_coffee_1a',
        'syde_traditions_coffee_4a',
        'syde_traditions_resume_first',
        'syde_traditions_resume_upper',
        'syde_traditions_mock_int_first',
        'syde_traditions_mock_int_upper',
        'syde_traditions_none',
        'syde_acts_give_advice',
        'syde_acts_receive_advice',
        'syde_acts_job_give',
        'syde_acts_job_receive',
        'syde_acts_dated_lower',
        'syde_acts_dated_upper',
        'syde_acts_none'
    ]]

    df_relationships = df_life_clean[[
        'uid',
        'serious_relationships',
        'serious_relationships_meet',
        'serious_relationship_month_undergrad',
        'serious_relationships_longest',
        'sydecest',
        'sydecest_wishful',
        'sydecest_people'
    ]]

    df_wild = df_life_clean[[
        'uid',
        'alcohol_1a',
        'alcohol_c1',
        'alcohol_1b',
        'alcohol_c2',
        'alcohol_2a',
        'alcohol_c3',
        'alcohol_2b',
        'alcohol_c4',
        'alcohol_3a',
        'alcohol_c5',
        'alcohol_3b',
        'alcohol_c6',
        'alcohol_4a',
        'alcohol_4b',
        'weed_1a',
        'weed_c1',
        'weed_1b',
        'weed_c2',
        'weed_2a',
        'weed_c3',
        'weed_2b',
        'weed_c4',
        'weed_3a',
        'weed_c5',
        'weed_3b',
        'weed_c6',
        'weed_4a',
        'weed_4b',
        'party_1a',
        'party_1b',
        'party_2a',
        'party_2b',
        'party_3a',
        'party_3b',
        'party_4a',
        'party_4b',
        'hye_milestones',
        'hye_milestones_bingo',
        'hye_milestones_engplay',
        'hye_milestones_semi',
        'hye_milestones_goose',
        'hye_milestones_old_bar',
        'hye_milestones_ezra',
        'hye_milestones_phils',
        'hye_milestones_pubcrawl',
        'hye_milestones_bar',
        'hye_milestones_club',
        'hye_milestones_photoshoots',
        'hye_milestones_costume',
        'hye_milestones_kw',
        'hye_milestones_flirt_ta',
        'hye_milestones_flirt_prof',
        'hye_milestones_none',
        'hye_milestones_invest',
        'hye_milestones_sports',
        'hye_milestones_boats',
        'hye_milestones_oweek_leader',
        'hye_milestones_eng_comp',
        'hye_milestones_coffee_house',
        'hye_milestones_laurier',
        'hye_milestones_all_nighter',
        'hye_milestones_dallas',
        'hye_milestones_free_food',
        'hye_milestones_inews',
        'hye_milestones_road_trip'
    ]]

    df_food = df_life_clean[[
        'uid',
        'plaza_food',
        'kw_food',
        'cook_school',
        'eat_out_school',
        'cooking_ability_1',
        'cooking_ability_4'
    ]]

    df_health = df_life_clean[[
        'uid',
        'exercise_g12',
        'exercise_1',
        'exercise_2',
        'exercise_3',
        'exercise_4',
        'fitness_level_g12',
        'fitness_level_4',
        'sleep_time',
        'mental_health_challenges',
        'mh_addiction',
        'mh_adhd',
        'mh_anxiety',
        'mh_depression',
        'mh_disassociation',
        'mh_eating_disorder',
        'mh_ocd',
        'mh_ptsd',
        'mh_sleeping_disorders',
        'mh_suicidal',
        'mh_none',
        'mental_health_bad_sources',
        'mental_health_support_types',
        'mental_health_professional',
        'mental_health_friend_crisis',
        'impostor_syndrome',
        'uwaterloo_mental_health_support',
        'cry_on_campus',
        'cry_on_campus_locations'
    ]]

    df_pa.to_csv(output_split_path + 'professional_activities.csv', index = False, encoding='utf-8')
    df_social.to_csv(output_split_path + 'social.csv', index = False, encoding='utf-8')
    df_syde_trad.to_csv(output_split_path + 'syde_traditions.csv', index = False, encoding='utf-8')
    df_relationships.to_csv(output_split_path + 'relationships.csv', index = False, encoding='utf-8')
    df_wild.to_csv(output_split_path + 'wild.csv', index = False, encoding='utf-8')
    df_food.to_csv(output_split_path + 'food.csv', index = False, encoding='utf-8')
    df_health.to_csv(output_split_path + 'health.csv', index = False, encoding='utf-8')

if __name__ == "__main__":
    main()