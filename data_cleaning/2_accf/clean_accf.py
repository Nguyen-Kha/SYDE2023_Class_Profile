import pandas as pd
import numpy as np
import math

###### DEV VARIABLES ########
input_csv_path = 'C:\\Users\\Kha\\Documents\\Programming\\SYDE2023_Class_Profile\\csv\\raw\\2_ACCF.csv'
output_rename_column_path = 'C:\\Users\\Kha\\Documents\\Programming\\SYDE2023_Class_Profile\\csv\\renamed_columns\\2_ACCF_renamed.csv'
output_pii_path = 'C:\\Users\\Kha\\Documents\\Programming\\SYDE2023_Class_Profile\\csv\\final\\2_ACCF_PII_final.csv'
output_standard_path = 'C:\\Users\\Kha\\Documents\\Programming\\SYDE2023_Class_Profile\\csv\\final\\2_ACCF_final.csv'
output_split_path = 'C:\\Users\\Kha\\Documents\\Programming\\SYDE2023_Class_Profile\\csv\\final\\split\\'

##### GLOBAL #######

###### MAPPINGS #########

cleaned_courses_dict = {
    "MCSI 446" : "MSCI 446",
    "MSCI546" : "MSCI 546",
    "MSCi 551" : "MSCI 551",
    "SYDE 599 - Computational Simulation" : "SYDE 599 - Computational Simulation of Societal and Environmental Systems",
    "SYDE 599 - Computational Simulation of Social and Environmental Systems" : "SYDE 599 - Computational Simulation of Societal and Environmental Systems",
    "Social & Environmental Systems" : "SYDE 599 - Computational Simulation of Societal and Environmental Systems",
    "SYDE 599 - Deep Learing" : "SYDE 599 - Deep Learning",
    "BME 550 - Sports Engineering": "BME 550",
    "MTE241": "MTE 241",
    "KOREA 101" : "KOREA 101R",
    "MUSCI 140" : "MUSIC 140",
    "MUSCI 101" : "MUSIC 101"
}

profs_dict = {
    "Alex Wong": "Alexander Wong",
    "Alexander Wong": "Alexander Wong",
    "Alexis Dolphin": "Alexis Dolphin",
    "Ali Ayub": "Ali Ayub",
    "Andrew McMurry": "Andrew McMurry",
    "Andrew Morton": "Andrew Morton",
    "Audrey Chung": "Audrey Chung",
    "Behrad Khamesee": "Behrad Khamesee",
    "Brenda Lee": "Brenda Lee",
    "Brian Tripp": "Bryan Tripp",
    "CGM": "Carolyn MacGregor",
    "Carolyn MacGregor": "Carolyn MacGregor",
    "Carolyn Macgregor": "Carolyn MacGregor",
    "Charbel Azzi": "Charbel Azzi",
    "Chris Eliasmith": "Chris Eliasmith",
    "Chris McClellan": "Chris McClellan",
    "Cosmin Munteanu": "Cosmin Munteanu",
    "David Clausi": "David Clausi",
    "Elizabeth Kittel": "Elizabeth Kittel",
    "Fieguth": "Paul Fieguth",
    "Glen Heppler": "Glenn Heppler",
    "Gordon Savage": "Gordon Savage",
    "Igor": "Igor Ivkovic",
    "Igor Ivkovic": "Igor Ivkovic",
    "Igor Ivkovik": "Igor Ivkovic",
    "Jean-Pierre Hickey": "Jean-Pierre Hickey",
    "Jennifer Howcroft": "Jennifer Howcroft",
    "Jenny Howcroft": "Jenny Howcroft",
    "Joel Blit": "Joel Blit",
    "Katie Plaisance": "Katie Plaisance",
    "Laura Gray": "Laura Gray",
    "Lisa Aultman-Hall": "Lisa Aultman-Hall",
    "Lukasz Golab": "Lukasz Golab",
    "Mary Robinson": "Mary Robinson",
    "Mary Wells": "Mary Wells",
    "Matthew Borland": "Matthew Borland",
    "Nasser Azad": "Nasser Azad",
    "Nima Maftoon": "Nima Maftoon",
    "Orion Bruckman": "Orion Bruckman",
    "Paul Fieguth": "Paul Fieguth",
    "Paul Figueth": "Paul Fieguth",
    "Peter Balka": "Peter Balka",
    "Reem Roufail": "Reem Roufail",
    "Rodrigo Costa": "Rodrigo Costa",
    "Roydon Fraser": "Roydon Fraser",
    "Scott Campbell": "Scott Campbell",
    "Sean": "Sean Speziale",
    "Sean Speziale": "Sean Speziale",
    "Shi Cao": "Shi Cao",
    "Siby Samuel": "Siby Samuel",
    "Simon Wood": "Simon Wood",
    "Simone Philpot": "Simone Philpot",
    "Stan Dimitrov": "Stan Dimitrov",
    "Stephen Birkett": "Stephen Birkett",
    "igor ivkovic": "Igor Ivkovic",
    "ivkovic igor": "Igor Ivkovic"
}

exchange_university_dict = {
    "Charles III University of Madrid" : "Universidad Carlos III de Madrid",
    "Delft" : "Technische Universiteit Delft",
    "EPFL" : "Ecole Polytechnique Federale de Lausanne",
    "Lund" : "Lunds Universitet",
    "NUD" : "National University of Singapore",
    "NUS" : "National University of Singapore",
    "UC3M" : "Universidad Carlos III de Madrid",
    "University Carlos III of Madrid (UC3M)" : "Universidad Carlos III de Madrid",
    "University College London" : "University College London"
}

######## FUNCTIONS #############

def rename_column_headers(df):
    df = df.rename(columns = {
        "What is your unique ID?" : "uid",
        "Which Technical Electives (TEs) did you take" : "te",
        "Which Complementary Studies Electives (CSEs) did you take" : "cse",
        "What was your most favourite core course" : "fav_core",
        "What was your least favourite core course" : "least_fav_core",
        "What was your most favourite TE (which TE would you most recommend)" : "fav_te",
        "What was your least favourite TE" : "least_fav_te",
        "What was your most favourite CSE (which CSE would you most recommend)" : "fav_cse",
        "What was your least favourite CSE" : "least_fav_cse",
        "What was your easiest term?" : "easiest_term",
        "What was your most difficult term?" : "hardest_term",
        "What was your most favourite term?" : "fav_term",
        "What was your least favourite term?" : "least_fav_term",
        "Who are your favourite professors" : "fav_profs",
        "Did you take any Options, Specializations, or Minors" : "op_spec_minor_bool",
        "Which Options, Specializations, or Minors did you take?" : "op_spec_minor",
        "Which of the following have you failed" : "failed",
        "How many times have you had to resubmit a work term report" : "wkrpt_resubmit",
        "How did you finish your work reports" : "wkrpt_start",
        "How many times have you overloaded a term" : "overload_term",
        "How many times have you taken a course over co-op" : "overload_coop",
        "For which reasons did you overload a term or taken a course over co-op" : "why_overload",
        "How many courses did you CR/NCR?" : "cr_ncr",
        "Did you apply for exchange?" : "apply_for_exchange",
        "When did you go on exchange?" : "exchange_term",
        "If you were accepted for exchange and did not go on exchange, why?" : "cancelled_exchange",
        "Which university did you attend on exchange?" : "exchange_uni",
        "In which country was your host university?" : "exchange_country",
        "How likely are you to recommend exchange to a (lower year) classmate" : "exchange_rec",
        "Was your FYDP SYDE-only or multidisciplinary" : "fydp_group",
        "What was your primary FYDP problem space" : "fydp_problem_space",
        "Which domain best describes your FYDP" : "fydp_domain",
        "How much money did you spend on your FYDP" : "fydp_money",
        "Are you proud of your FYDP" : "fydp_proud",
        "Do you or your group plan on pursuing your FYDP further beyond 4B" : "fydp_future",
        "Do you have any comments on the FYDP overall" : "fydp_comments",
        "On a scale of 0 - 10, how would you rate your co-op POSITIONS in terms of enjoyment [1A Co-op (Winter 2019)]" : "1a_coop_enjoy_pos",
        "On a scale of 0 - 10, how would you rate your co-op POSITIONS in terms of enjoyment [1B Co-op (Fall 2019)]" : "1b_coop_enjoy_pos",
        "On a scale of 0 - 10, how would you rate your co-op POSITIONS in terms of enjoyment [2A Co-op (Summer 2020)]" : "2a_coop_enjoy_pos",
        "On a scale of 0 - 10, how would you rate your co-op POSITIONS in terms of enjoyment [2B Co-op (Winter 2021)]" : "2b_coop_enjoy_pos",
        "On a scale of 0 - 10, how would you rate your co-op POSITIONS in terms of enjoyment [3A Co-op (Fall 2021)]" : "3a_coop_enjoy_pos",
        "On a scale of 0 - 10, how would you rate your co-op POSITIONS in terms of enjoyment [3B Co-op (Summer 2022)]" : "3b_coop_enjoy_pos",
        "On a scale of 0 - 10, how would you rate your co-op LOCATIONS in terms of enjoyment [1A Co-op (Winter 2019)]" : "1a_coop_enjoy_loc",
        "On a scale of 0 - 10, how would you rate your co-op LOCATIONS in terms of enjoyment [1B Co-op (Fall 2019)]" : "1b_coop_enjoy_loc",
        "On a scale of 0 - 10, how would you rate your co-op LOCATIONS in terms of enjoyment [2A Co-op (Summer 2020)]" : "2a_coop_enjoy_loc",
        "On a scale of 0 - 10, how would you rate your co-op LOCATIONS in terms of enjoyment [2B Co-op (Winter 2021)]" : "2b_coop_enjoy_loc",
        "On a scale of 0 - 10, how would you rate your co-op LOCATIONS in terms of enjoyment [3A Co-op (Fall 2021)]" : "3a_coop_enjoy_loc",
        "On a scale of 0 - 10, how would you rate your co-op LOCATIONS in terms of enjoyment [3B Co-op (Summer 2022)]" : "3b_coop_enjoy_loc",
        "Have you ever returned to a previous employer" : "return_to_employer",
        "If you have returned to a previous employer, for which of the following reasons did you return" : "why_return_to_employer",
        "If you had multiple offers in a recruiting season, what factors affected your choice of co-op [Potential Skills to be Developed]" : "factor_coop_skills",
        "If you had multiple offers in a recruiting season, what factors affected your choice of co-op [Team / Project I would be working with / on]" : "factor_coop_project",
        "If you had multiple offers in a recruiting season, what factors affected your choice of co-op [Company Reputation]" : "factor_coop_reputation",
        "If you had multiple offers in a recruiting season, what factors affected your choice of co-op [Location]" : "factor_coop_location",
        "If you had multiple offers in a recruiting season, what factors affected your choice of co-op [Compensation]" : "factor_coop_compensation",
        "If you had multiple offers in a recruiting season, what factors affected your choice of co-op [Opportunity to return full-time]" : "factor_coop_full_time",
        "Have you ever ... [Been late to an interview]" : "hye_late_interview",
        "Have you ever ... [Missed an interview]" : "hye_miss_interview",
        "Have you ever ... [Reneged an offer on WaterlooWorks]" : "hye_reneg",
        "Have you ever ... [Been banned from WaterlooWorks]" : "hye_banned",
        "Have you ever ... [Got screwed over by CECA]" : "hye_screwed",
        "Have you ever ... [Failed a PD course]" : "hye_failed_pd",
        "Have you ever ... [Been fired from a co-op position]" : "hye_fired",
        "Which PD courses have you taken" : "pd_courses",
        "How useful did you find the PD courses" : "pd_useful",
        "I finished the PD assignments ..." : "pd_finish",
        "Which statement do you agree more with" : "pd_completion",
        "Fuck PD?" : "fuck_pd",
        "I enjoyed in-person learning more than online learning" : "in_person_vs_online",
        "How did you find the quality of online instruction compared to a regular school term" : "quality_online",
        "Where did you live during the 2B academic term" : "location_2b",
        "Where did you live during the 3A academic term" : "location_3a",
        "Who did you live with during the ... [2A Co-op term (Spring 2020)]" : "roommates_2a_coop",
        "Who did you live with during the ... [2B Academic term (Fall 2020)]" : "roommates_2b_study",
        "Who did you live with during the ... [2B Co-op term (Winter 2021)]" : "roommates_2b_coop",
        "Who did you live with during the ... [3A Academic term (Spring 2021)]" : "roommates_3a_study",
        "Who did you live with during the ... [3A Co-op term (Fall 2021)]" : "roommates_3a_coop",
        "How many people were in your quarantine social circle in 2020?" : "social_circle",
        "From the number of people in your quarantine social circle in 2020, how many of them are still your friends today?" : "social_circle_exist",
        "From your quarantine social circle, have people left your social circle, joined your circle, or both compared to today" : "social_circle_delta",
        "How many times have you caught COVID?" : "covid_times"
    })

    return df

def clean_all_taken_courses(course):
    # Deal with NaN
    if(type(course) == float):
        if(math.isnan(course)):
            return course
        
    cleaned_courses_string = ""
    course = course.replace("MSCI 245 ECE 358", "MSCI 245, ECE 358")
    individual_course = course.split(",")
    
    for i in individual_course:
        try:
            cleaned_course = cleaned_courses_dict[i.strip()]
        except:
            cleaned_course = i.strip()
        
        if(cleaned_courses_string == ""):
            cleaned_courses_string = cleaned_course
        else:
            cleaned_courses_string = cleaned_courses_string + ", " + cleaned_course
    
    return cleaned_courses_string

def clean_fav_profs(prof):
    if(type(prof) == float):
        if(math.isnan(prof)):
            return prof
    
    cleaned_prof_string = ""

    individual_profs = prof.split(",")
    for i in individual_profs:
        try:
            cleaned_prof = profs_dict[i.strip()]
        except:
            cleaned_prof = i.strip()
        
        if(cleaned_prof_string == "" or len(cleaned_prof_string) == 0):
            cleaned_prof_string = cleaned_prof
        else:
            cleaned_prof_string = cleaned_prof_string + ", " + cleaned_prof
    
    return cleaned_prof_string

def clean_coop_position_rating(rating):
    try:
        if(rating == '0 (I despised this co-op job)'):
                return 0
        elif (rating == '5 (This job was alright)'):
            return 5
        elif (rating == '10 (I loved this co-op job)'):
            return 10
        else:
            clean_rating = int(rating)
            return clean_rating
    except:
#         if(type(rating) == float and math.isnan(rating) == True):
#             return rating
        return rating

def clean_coop_location_rating(rating):
    try:
        if(rating == '0 (I despised this co-op location)'):
            return 0
        elif(rating == '10 (I loved this co-op location)'):
            return 10
        else:
            clean_rating = int(rating)
            return clean_rating
    except:
#         if(type(rating) == float and math.isnan(rating) == True):
#         return rating
        return rating

def clean_exchange_unis(uni):
    try:
        uni = exchange_university_dict[uni]
        return uni
    except:
        return uni
    
def strip_core_course_names(answer):
    if(type(answer) == float):
        if(math.isnan(answer)):
            return np.nan
    
    return answer[:9].strip()

def main():
    # Load CSV
    df = pd.read_csv(input_csv_path)
    df = df.drop(columns = ['Timestamp', 'Questions Comments Concerns Suggestions Feedback for this section'])

    df_accf_clean = rename_column_headers(df)
    df_rename_column = df_accf_clean.copy()
    df_rename_column.to_csv(output_rename_column_path, index=False, encoding='utf-8')

    # Clean TEs
    df_accf_clean['te'] = df_accf_clean['te'].apply(clean_all_taken_courses)

    # Clean CSEs
    df_accf_clean['cse'] = df_accf_clean['cse'].apply(clean_all_taken_courses)

    # Clean favourite TE
    df_accf_clean['fav_te'] = df_accf_clean['fav_te'].apply(clean_all_taken_courses)

    # Clean least favourite TE
    df_accf_clean['least_fav_te'] = df_accf_clean['least_fav_te'].apply(clean_all_taken_courses)

    # Clean favourite CSE
    df_accf_clean['fav_cse'] = df_accf_clean['least_fav_cse'].apply(clean_all_taken_courses)

    # Clean least favourite CSE
    df_accf_clean['least_fav_cse'] = df_accf_clean['least_fav_cse'].apply(clean_all_taken_courses)

    # Clean favourite profs
    df_accf_clean['fav_profs'] = df_accf_clean['fav_profs'].apply(clean_fav_profs)

    # Clean co-op position rating
    df_accf_clean['1a_coop_enjoy_pos'] = df_accf_clean['1a_coop_enjoy_pos'].apply(clean_coop_position_rating)
    df_accf_clean['1b_coop_enjoy_pos'] = df_accf_clean['1b_coop_enjoy_pos'].apply(clean_coop_position_rating)
    df_accf_clean['2a_coop_enjoy_pos'] = df_accf_clean['2a_coop_enjoy_pos'].apply(clean_coop_position_rating)
    df_accf_clean['2b_coop_enjoy_pos'] = df_accf_clean['2b_coop_enjoy_pos'].apply(clean_coop_position_rating)
    df_accf_clean['3a_coop_enjoy_pos'] = df_accf_clean['3a_coop_enjoy_pos'].apply(clean_coop_position_rating)
    df_accf_clean['3b_coop_enjoy_pos'] = df_accf_clean['3b_coop_enjoy_pos'].apply(clean_coop_position_rating)

    # Clean co-op location rating
    df_accf_clean['1a_coop_enjoy_loc'] = df_accf_clean['1a_coop_enjoy_loc'].apply(clean_coop_location_rating)
    df_accf_clean['1a_coop_enjoy_loc'] = df_accf_clean['1a_coop_enjoy_loc'].apply(clean_coop_location_rating)
    df_accf_clean['1b_coop_enjoy_loc'] = df_accf_clean['1b_coop_enjoy_loc'].apply(clean_coop_location_rating)
    df_accf_clean['2a_coop_enjoy_loc'] = df_accf_clean['2a_coop_enjoy_loc'].apply(clean_coop_location_rating)
    df_accf_clean['2b_coop_enjoy_loc'] = df_accf_clean['2b_coop_enjoy_loc'].apply(clean_coop_location_rating)
    df_accf_clean['3a_coop_enjoy_loc'] = df_accf_clean['3a_coop_enjoy_loc'].apply(clean_coop_location_rating)
    df_accf_clean['3b_coop_enjoy_loc'] = df_accf_clean['3b_coop_enjoy_loc'].apply(clean_coop_location_rating)

    # Clean exchange university
    df_accf_clean['exchange_uni'] = df_accf_clean['exchange_uni'].apply(clean_exchange_unis)

    # Clean core courses
    df_accf_clean['fav_core'] = df_accf_clean['fav_core'].apply(strip_core_course_names)
    df_accf_clean['least_fav_core'] = df_accf_clean['least_fav_core'].apply(strip_core_course_names)
    
    # Export CSV
    # df_accf_clean.to_csv(output_standard_path, index=False, encoding="utf-8")
    df_accf_pii = df_accf_clean[['location_2b', 'location_3a']]
    df_accf_pii = df_accf_pii.sample(frac = 1)
    df_accf_no_pii = df_accf_clean.drop(columns = ['location_2b', 'location_3a'])

    df_accf_pii.to_csv(output_pii_path, index=False, encoding='utf-8')
    df_accf_no_pii.to_csv(output_standard_path, index=False, encoding='utf-8')

    df_school = df_accf_clean[[
        'uid',
        'te',
        'cse',
        'fav_core',
        'least_fav_core',
        'fav_te',
        'least_fav_te',
        'fav_cse',
        'least_fav_cse',
        'easiest_term',
        'hardest_term',
        'fav_term',
        'least_fav_term',
        'fav_profs',
        'op_spec_minor_bool',
        'op_spec_minor',
        'failed',
        'wkrpt_resubmit',
        'wkrpt_start',
        'overload_term',
        'overload_coop',
        'why_overload',
        'cr_ncr'
    ]]

    df_exchange = df_accf_clean[[
        'uid',
        'apply_for_exchange',
        'exchange_term',
        'cancelled_exchange',
        'exchange_uni',
        'exchange_country',
        'exchange_rec'
    ]]

    df_fydp = df_accf_clean[[
        'uid',
        'fydp_group',
        'fydp_problem_space',
        'fydp_domain',
        'fydp_money',
        'fydp_proud',
        'fydp_future',
        'fydp_comments'
    ]]

    df_coop = df_accf_clean[[
        'uid',
        '1a_coop_enjoy_pos',
        '1b_coop_enjoy_pos',
        '2a_coop_enjoy_pos',
        '2b_coop_enjoy_pos',
        '3a_coop_enjoy_pos',
        '3b_coop_enjoy_pos',
        '1a_coop_enjoy_loc',
        '1b_coop_enjoy_loc',
        '2a_coop_enjoy_loc',
        '2b_coop_enjoy_loc',
        '3a_coop_enjoy_loc',
        '3b_coop_enjoy_loc',
        'return_to_employer',
        'why_return_to_employer',
        'factor_coop_skills',
        'factor_coop_project',
        'factor_coop_reputation',
        'factor_coop_location',
        'factor_coop_compensation',
        'factor_coop_full_time',
        'hye_late_interview',
        'hye_miss_interview',
        'hye_reneg',
        'hye_banned',
        'hye_screwed',
        'hye_fired'
    ]]

    df_pd = df_accf_clean[[
        'uid',
        'hye_failed_pd',
        'pd_courses',
        'pd_useful',
        'pd_finish',
        'pd_completion',
        'fuck_pd'
    ]]

    df_covid = df_accf_clean[[
        'uid',
        'in_person_vs_online',
        'quality_online',
        'roommates_2a_coop',
        'roommates_2b_study',
        'roommates_2b_coop',
        'roommates_3a_study',
        'roommates_3a_coop',
        'social_circle',
        'social_circle_exist',
        'social_circle_delta',
        'covid_times'
    ]]

    df_school.to_csv(output_split_path + 'school.csv', index = False, encoding='utf-8')
    df_exchange.to_csv(output_split_path + 'exchange.csv', index = False, encoding='utf-8')
    df_fydp.to_csv(output_split_path + 'fydp.csv', index = False, encoding='utf-8')
    df_coop.to_csv(output_split_path + 'coop.csv', index = False, encoding='utf-8')
    df_pd.to_csv(output_split_path + 'pd.csv', index = False, encoding='utf-8')
    df_covid.to_csv(output_split_path + 'covid.csv', index = False, encoding='utf-8')

if __name__ == "__main__":
    main()