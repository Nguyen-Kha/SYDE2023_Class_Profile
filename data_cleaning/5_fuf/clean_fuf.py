import numpy as np
import pandas as pd
import math

###### DEV VARIABLES ########
input_csv_path = 'C:\\Users\\Kha\\Documents\\Programming\\SYDE2023_Class_Profile\\csv\\raw\\5_FUF.csv'
output_rename_column_path = 'C:\\Users\\Kha\\Documents\\Programming\\SYDE2023_Class_Profile\\csv\\renamed_columns\\5_FUF_renamed.csv'
output_pii_path = 'C:\\Users\\Kha\\Documents\\Programming\\SYDE2023_Class_Profile\\csv\\final\\5_FUF_PII_final.csv'
output_standard_path = 'C:\\Users\\Kha\\Documents\\Programming\\SYDE2023_Class_Profile\\csv\\final\\5_FUF_final.csv'
output_split_path = 'C:\\Users\\Kha\\Documents\\Programming\\SYDE2023_Class_Profile\\csv\\final\\split\\'

##### GLOBAL #######

ft_job_city = []
ft_job_country = []

###### MAPPINGS #########

knowing_yourself_list = [
    'iq_1',
    'eq_1',
    'social_skills_1',
    'attractiveness_1',
    'earning_potential_1',
    'morals_1',
    'ethics_1',
    'work_ethic_1',
    'confidence_1',
    'self_understanding_1',
    'teamwork_1',
    'self_esteem_1',
    'iq_4',
    'eq_4',
    'social_skills_4',
    'attractiveness_4',
    'earning_potential_4',
    'morals_4',
    'ethics_4',
    'work_ethic_4',
    'confidence_4',
    'self_understanding_4',
    'teamwork_4',
    'self_esteem_4'
]

different_program_dict = {
    'University of Toronto: UX Design': 'University of Toronto - UX Design',
    'UofT - Engineering Science': 'University of Toronto - Engineering Science',
    'waterloo, cs': 'University of Waterloo - Computer Science',
    'University of Waterloo: BMath Data Science': 'University of Waterloo - BMath Data Science',
    'University of Waterloo: Computer Science': 'University of Waterloo - Computer Science',
    'University of Waterloo: Management Engineering': 'University of Waterloo - Management Engineering',
    'UofW: Computer Science ': 'University of Waterloo - Computer Science',
    'McGill:CS': 'McGill University - Computer Science',
    'University of Waterloo: Software Engineering': 'University of Waterloo - Software Engineering',
    "UW: CS, Queen's: Engineering, Queen's CS": 'University of Waterloo - Computer Science, Queens University - Engineering, Queens University - Computer Science',
    'UW: CS': 'University of Waterloo - Computer Science',
    'University of Waterloo: GBDA': 'University of Waterloo - Global Business and Digital Arts',
    'University of Waterloo: GBDA Co-op': 'University of Waterloo - Global Business and Digital Arts',
    'University of Waterloo: Math': 'University of Waterloo - Mathematics',
    'Stanford: philosophy': 'Stanford University - Philosophy',
    'University of Waterloo: Mechatronics': 'University of Waterloo - Mechatronics Engineering',
    'University of Waterloo: Computer Science ': 'University of Waterloo - Computer Science',
    'UW Computer Science': 'University of Waterloo - Computer Science',
    'Waterloo: Mechatronics': 'University of Waterloo - Mechatronics Engineering'
}

grad_trip_location_dict = {
    'South Island, New Zealand': 'New Zealand',
    'asia': 'Asia',
    'Japan and Korea': 'Japan, Korea',
    'London and Paris': 'London, Paris',
    'Europe and USA': 'Europe, USA',
    'Portugal and Spain': 'Portugal, Spain',
    'South East Asia (Vietnam, Thailand, Cambodia, Singapore) and Europe (Spain, France, England, Switzerland, Italy) ': 'Vietnam, Thailand, Cambodia, Singapore, Spain, France, England, Switzerland, Italy',
    'Camping at Frontenac Park': 'Frontenac Park'
}

replace_strings_fuf_list = [
    'part_time_job_school',
    'future_eng_role',
    'future_industries',
    'grad_trip',
    'ft_category',
    'ft_remote',
    'ft_industry',
    'ft_find_job',
    'ft_other_categories',
    'sft_categories',
    'investments',
    'syde_missing_courses',
    'syde_excessive_courses'
]

######## FUNCTIONS #############

def rename_column_headers(df):
    df = df.rename(columns = {
        "What is your unique ID?" : "uid",
        "How much debt will you be graduating with" : "debt",
        "Approximately what percentage of your tuition was self-funded" : "tuition_self_fund",
        "Did you opt out of any WUSA optional fees?" : "wusa_optional",
        "Which FEDS/WUSA services have you used?" : "wusa_services_used",
        "Have you ever worked at a part time job during a school term" : "part_time_job_school",
        "Have you ever worked at a full time job / internship during a school term" : "job_school",
        "Did you receive scholarships or financial awards during your undergrad career" : "scholarships",
        "Which of the following financial instruments have you invested in" : "investments",
        "While living in Waterloo, how much did you spend on groceries per month on average?" : "groceries_per_month",
        "Did you set a monthly budget while living in Waterloo" : "monthly_budget",
        "Approximately how much money did you spend on course materials in total?" : "cost_course_materials",
        "Going back in time with the knowledge you have now, would you have chosen SYDE again?" : "syde_again",
        "If you would not choose SYDE again, which university and which program would you have chosen instead?" : "other_school_program",
        "State your level of agreement with the following statements [I am satisfied with the SYDE program]" : "syde_satisfied",
        "State your level of agreement with the following statements [I felt like I belonged in SYDE]" : "syde_belonged",
        "State your level of agreement with the following statements [I felt like I was a part of the SYDE community]" : "syde_community",
        "State your level of agreement with the following statements [I consider myself to be an aspiring engineer]" : "aspiring_engineer",
        "State your level of agreement with the following statements [SYDE prepared me for a traditional engineering career]" : "syde_trad_eng",
        "State your level of agreement with the following statements [The quality of professors' instructional content was acceptable]" : "syde_prof_quality",
        "State your level of agreement with the following statements [The quality of the SYDE courses was acceptable]" : "syde_course_quality",
        "State your level of agreement with the following statements [The support given by the SYDE administration was acceptable]" : "syde_support_quality",
        "What type of courses did you think SYDE was missing from its curriculum?" : "syde_missing_courses",
        "What type of courses did you think SYDE was excessive in the SYDE curriculum" : "syde_excessive_courses",
        "State your level of agreement with the following statements [I am satisfied with my experience at UW]" : "uw_satisfied",
        "State your level of agreement with the following statements [I made a lot of friends outside of SYDE]" : "friends_outside_syde",
        "State your level of agreement with the following statements [I made a lot of friends outside of UW Engineering]" : "friends_outside_eng",
        "State your level of agreement with the following statements [I am satisfied with the extracurriculars I participated in]" : "ec_satisfied",
        "How much did you enjoy Kitchener Waterloo as a city in ... [First Year]" : "kw_enjoy_1",
        "How much did you enjoy Kitchener Waterloo as a city in ... [Fourth Year]" : "kw_enjoy_4",
        "How much did you enjoy the UW atmosphere in ... [First Year]" : "uw_atmosphere_1",
        "How much did you enjoy the UW atmosphere in ... [Second Year]" : "uw_atmosphere_2",
        "How much did you enjoy the UW atmosphere in ... [Third Year]" : "uw_atmosphere_3",
        "How much did you enjoy the UW atmosphere in ... [Fourth Year]" : "uw_atmosphere_4",
        "Knowing yourself in FIRST YEAR (1A), state your level of self-perception for the following traits as a FIRST YEAR (1A) student [General Intelligence]" : "iq_1",
        "Knowing yourself in FIRST YEAR (1A), state your level of self-perception for the following traits as a FIRST YEAR (1A) student [Emotional Intelligence]" : "eq_1",
        "Knowing yourself in FIRST YEAR (1A), state your level of self-perception for the following traits as a FIRST YEAR (1A) student [Interpersonal Skills]" : "social_skills_1",
        "Knowing yourself in FIRST YEAR (1A), state your level of self-perception for the following traits as a FIRST YEAR (1A) student [Physical Attractiveness]" : "attractiveness_1",
        "Knowing yourself in FIRST YEAR (1A), state your level of self-perception for the following traits as a FIRST YEAR (1A) student [Earning Potential]" : "earning_potential_1",
        "Knowing yourself in FIRST YEAR (1A), state your level of self-perception for the following traits as a FIRST YEAR (1A) student [Sense of Morals]" : "morals_1",
        "Knowing yourself in FIRST YEAR (1A), state your level of self-perception for the following traits as a FIRST YEAR (1A) student [Sense of Ethics]" : "ethics_1",
        "Knowing yourself in FIRST YEAR (1A), state your level of self-perception for the following traits as a FIRST YEAR (1A) student [Work Ethic]" : "work_ethic_1",
        "Knowing yourself in FIRST YEAR (1A), state your level of self-perception for the following traits as a FIRST YEAR (1A) student [Confidence]" : "confidence_1",
        "Knowing yourself in FIRST YEAR (1A), state your level of self-perception for the following traits as a FIRST YEAR (1A) student [Self Understanding]" : "self_understanding_1",
        "Knowing yourself in FIRST YEAR (1A), state your level of self-perception for the following traits as a FIRST YEAR (1A) student [Teamwork]" : "teamwork_1",
        "Knowing yourself in FIRST YEAR (1A), state your level of self-perception for the following traits as a FIRST YEAR (1A) student [Self Esteem]" : "self_esteem_1",
        "Now as a FOURTH YEAR (4B) student, state your level of self-perception for the following traits as a FOURTH YEAR (4B) student [General Intelligence]" : "iq_4",
        "Now as a FOURTH YEAR (4B) student, state your level of self-perception for the following traits as a FOURTH YEAR (4B) student [Emotional Intelligence]" : "eq_4",
        "Now as a FOURTH YEAR (4B) student, state your level of self-perception for the following traits as a FOURTH YEAR (4B) student [Interpersonal Skills]" : "social_skills_4",
        "Now as a FOURTH YEAR (4B) student, state your level of self-perception for the following traits as a FOURTH YEAR (4B) student [Physical Attractiveness]" : "attractiveness_4",
        "Now as a FOURTH YEAR (4B) student, state your level of self-perception for the following traits as a FOURTH YEAR (4B) student [Earning Potential]" : "earning_potential_4",
        "Now as a FOURTH YEAR (4B) student, state your level of self-perception for the following traits as a FOURTH YEAR (4B) student [Sense of Morals]" : "morals_4",
        "Now as a FOURTH YEAR (4B) student, state your level of self-perception for the following traits as a FOURTH YEAR (4B) student [Sense of Ethics]" : "ethics_4",
        "Now as a FOURTH YEAR (4B) student, state your level of self-perception for the following traits as a FOURTH YEAR (4B) student [Work Ethic]" : "work_ethic_4",
        "Now as a FOURTH YEAR (4B) student, state your level of self-perception for the following traits as a FOURTH YEAR (4B) student [Confidence]" : "confidence_4",
        "Now as a FOURTH YEAR (4B) student, state your level of self-perception for the following traits as a FOURTH YEAR (4B) student [Self Understanding]" : "self_understanding_4",
        "Now as a FOURTH YEAR (4B) student, state your level of self-perception for the following traits as a FOURTH YEAR (4B) student [Teamwork]" : "teamwork_4",
        "Now as a FOURTH YEAR (4B) student, state your level of self-perception for the following traits as a FOURTH YEAR (4B) student [Self Esteem]" : "self_esteem_4",
        "Did you attend convocation?" : "convocation",
        "Do you intend on eventually working in a traditional engineering role or at a traditional engineering firm" : "future_eng_role",
        "Do you intend on getting your P.Eng.?" : "p_eng",
        "How many classmates do you expect to still be in touch with?" : "in_touch_classmates",
        "To which UW departments do you plan on donating to in the future?" : "donations",
        "At what age do you plan on getting married (or wish to be married)?" : "age_of_marriage",
        "At what age do you plan on having children (or wish to have) children?" : "age_of_children",
        "In which city and country do you plan on settling down?" : "location_settling",
        "State you level of agreement with the following statement [I am optimistic about my job security in the future]" : "job_security_optimism",
        "State you level of agreement with the following statement [I am optimistic about the state of the job market]" : "job_market_optimism",
        "State you level of agreement with the following statement [I have a clear direction of where I would like to take my career]" : "career_direction",
        "Regarding your career, rank the importance of each aspect when it comes to taking an offer for a full time position [Job satisfaction]" : "ft_job_satisfaction",
        "Regarding your career, rank the importance of each aspect when it comes to taking an offer for a full time position [Work Life Balance]" : "ft_wlb",
        "Regarding your career, rank the importance of each aspect when it comes to taking an offer for a full time position [Impact on Society]" : "ft_impact",
        "Regarding your career, rank the importance of each aspect when it comes to taking an offer for a full time position [Compensation]" : "ft_comp",
        "Regarding your career, rank the importance of each aspect when it comes to taking an offer for a full time position [Prestige]" : "ft_prestige",
        "Regarding your career, rank the importance of each aspect when it comes to taking an offer for a full time position [Team Members]" : "ft_team",
        "Regarding your career, rank the importance of each aspect when it comes to taking an offer for a full time position [Boss / Management]" : "ft_boss",
        "Regarding your career, rank the importance of each aspect when it comes to taking an offer for a full time position [Perks (free food, events, office life)]" : "ft_perks",
        "Regarding your career, rank the importance of each aspect when it comes to taking an offer for a full time position [Benefits]" : "ft_benefits",
        "Regarding your career, rank the importance of each aspect when it comes to taking an offer for a full time position [Type of Projects worked on]" : "ft_projects",
        "Regarding your career, rank the importance of each aspect when it comes to taking an offer for a full time position [Skill development]" : "ft_skill_development",
        "Regarding your career, rank the importance of each aspect when it comes to taking an offer for a full time position [Location]" : "ft_location",
        "Regarding your career, rank the importance of each aspect when it comes to taking an offer for a full time position [Company Culture]" : "ft_company_culture",
        "Regarding your career, rank the importance of each aspect when it comes to taking an offer for a full time position [Proximity to friends and family]" : "ft_proximity_social",
        "Regarding your career, rank the importance of each aspect when it comes to taking an offer for a full time position [Industry]" : "ft_company_industry",
        "Regarding your career, rank the importance of each aspect when it comes to taking an offer for a full time position [Remote Work flexibility]" : "ft_remote_flex",
        "10 years from now, which industries would you like to work in?" : "future_industries",
        "10 years from now, which job title would you like to have?" : "future_job_title",
        "10 years from now, what type of higher education would you wish to pursue" : "future_higher_ed",
        "Did you go on a grad trip?" : "grad_trip",
        "If you have went or are planning on going on a grad trip, where would you be going?" : "grad_trip_location",
        "Do you intend on attending the 5-year UW Engineering Reunion in 2028?" : "reunion",
        "What are your current plans for postgrad?" : "postgrad_plans",
        "Does your current postgrad plan require you to leave Canada" : "postgrad_leave_canada",
        "If you plan on leaving Canada, when do you expect to return to Canada" : "return_to_canada",
        "If you are leaving Canada, why would you want to return to Canada, or why would you not want to return?" : "return_to_canada_reasons",
        "In which of the following areas do you wish to see the most positive change in the world" : "world_change",
        "What is the title of your job?" : "ft_job_title",
        "Select the category that best represents your job" : "ft_category",
        "In which location is your job based in?" : "ft_job_location",
        "Is your job remote?" : "ft_remote",
        "For which company will you be working for?" : "ft_company",
        "What is the size of this company?" : "ft_company_size",
        "Select the industry that best relates to your company" : "ft_industry",
        "What is your First Year Total Compensation in CAD?" : "ft_tc",
        "Regarding your total compensation, what is your base salary in CAD?" : "ft_tc_base",
        "Regarding your total compensation, how much will you be receiving in equity in CAD?" : "ft_tc_equity",
        "Regarding your total compensation, what is your signing bonus in CAD?" : "ft_tc_bonus",
        "How did you find this position?" : "ft_find_job",
        "When did you receive your offer letter?" : "ft_offer_letter",
        "What factors influenced your choice for full-time employment? " : "ft_factors",
        "How many applications did you send out while searching for a full time position" : "ft_apps",
        "How many interviews did you receive while searching for a full time position" : "ft_interviews",
        "What was the most amount of interview rounds did you go through during your full time job search process?" : "ft_interview_rounds",
        "How many offers did you receive while searching for a full time position?" : "ft_offers",
        "Which of the following job categories did you desire or consider when applying for full time jobs?" : "ft_other_categories",
        "Are you actively pursuing full time employment search?" : "sft_pursuing",
        "Which of the following job categories did you desire or consider when applying for full time jobs? Sft" : "sft_categories",
        "How many applications have you sent out?" : "sft_apps",
        "How many interviews have you received?" : "sft_interviews",
        "In which locations have you considered or desired to work in / relocate to" : "sft_locations",
        "When did you receive your offer?" : "higher_ed_offer",
        "What type of educational program did you get accepted to?" : "higher_ed_program",
        "Which school will you be attending for your studies" : "higher_ed_school",
        "For Masters and PhD students, which program will you be doing your degree in?" : "higher_ed_degree",
        "For Masters and PhD students who require a supervisor,  have you previously done research for your supervisor before?" : "higher_ed_supervisor",
        "What are your plans after post grad?" : "higher_ed_postgrad_plans",
        "Where do you plan to be living for postgrad?" : "time_off_living",
        "What do you plan on doing, or plan on working on during this period of time?" : "time_off_doing",
        "How long do you plan on taking time off or pursuing this personal venture?" : "time_off_personal_venture",
        "What do you hope to do within the next year?" : "time_off_future_plans"
    })

    return df

def standardize_knowing_yourself(answer):
    if(type(answer) == float):
        if(math.isnan(answer)):
            return None
    
    if(answer == '1 (Below Average)'):
        return 1
    elif(answer == '3 (Average)'):
        return 3
    elif(answer == '5 (Above Average)'):
        return 5
    else:
        return int(answer)
    
def rename_different_program(answer):
    if(type(answer) == float):
        if(math.isnan(answer)):
            return answer
        
    return different_program_dict[answer]

def rename_grad_trip_location(answer):
    if(type(answer) == float):
        if(math.isnan(answer)):
            return answer
    
    try:
        return grad_trip_location_dict[answer]
    except:
        return answer
    
def split_ft_job_location(df):
    df['ft_job_location'].apply(parse_ft_job_location)
    df_extended = concat_ft_job_location()
    return df_extended
    

def parse_ft_job_location(answer):
    global ft_job_city
    global ft_job_country
    
    if(type(answer) == float):
        if(math.isnan(answer)):
            ft_job_city.append(np.nan)
            ft_job_country.append(np.nan)
            return None
    
    pair = answer.split(",")
    ft_job_city.append(pair[0].strip())
    ft_job_country.append(pair[1].strip())
    
def concat_ft_job_location():
    global ft_job_city
    global ft_job_country
    
    df_extended = pd.DataFrame({
        'ft_job_city': ft_job_city,
        'ft_job_country': ft_job_country
    })
    
    return df_extended

def replace_strings_fuf(answer):
    if(type(answer) == float):
        if(math.isnan(answer)):
            return None
        
    if("Yes, a food / service related job" in answer):
        answer = answer.replace("Yes, a food / service related job", "Yes a food / service related job")
    if("Yes, an extended co-op" in answer):
        answer = answer.replace("Yes, an extended co-op", "Yes an extended co-op")
    if("Yes, at another type of job" in answer):
        answer = answer.replace("Yes, at another type of job", "Yes at another type of job")
    if("Managed Services (WealthSimple)" in answer):
        answer = answer.replace("Managed Services (WealthSimple)", "Managed Services")
    if("Materials (SYDE 285, SYDE 286)" in answer):
        answer = answer.replace("Materials (SYDE 285, SYDE 286)", "Materials")
    if("Mechanical Engineering (SYDE 381, SYDE 383)" in answer):
        answer = answer.replace("Mechanical Engineering (SYDE 381, SYDE 383)", "Mechanical Engineering")
    if("Computer Systems and Hardware (SYDE 192)" in answer):
        answer = answer.replace("Computer Systems and Hardware (SYDE 192)", "Computer Systems and Hardware")
    if("Electrical Engineering (SYDE 292)" in answer):
        answer = answer.replace("Electrical Engineering (SYDE 292)", "Electrical Engineering")
    if("Physical Systems (SYDE 252, SYDE 351)" in answer):
        answer = answer.replace("Physical Systems (SYDE 252, SYDE 351)", "Physical Systems")
    if("Yes, I have already worked in a traditional engineering role / firm and intend on continuing this path" in answer):
        answer = answer.replace(
            "Yes, I have already worked in a traditional engineering role / firm and intend on continuing this path",
            "Yes I have already worked in a traditional engineering role / firm and intend on continuing this path"
        )
    if("Yes, I have not yet but I would like to" in answer):
        answer = answer.replace("Yes, I have not yet but I would like to", "Yes I have not yet but I would like to")
    if("No, I have already worked in a traditional engineering role / firm and do not intend to pursue this in the future" in answer):
        answer = answer.replace(
            "No, I have already worked in a traditional engineering role / firm and do not intend to pursue this in the future",
            "No I have already worked in a traditional engineering role / firm and do not intend to pursue this in the future"
        )
    if("No, I have not yet and would not want to" in answer):
        answer = answer.replace("No, I have not yet and would not want to", "No I have not yet and would not want to")
    if("Consulting (General, Tech, Design)" in answer):
        answer = answer.replace("Consulting (General, Tech, Design)", "Consulting")
    if("No, but I have one planned" in answer):
        answer = answer.replace("No, but I have one planned", "No but I have one planned")
    if("No, I do not intend on going on a grad trip" in answer):
        answer = answer.replace("No, I do not intend on going on a grad trip", "No I do not intend on going on a grad trip")
    if("Hardware (Embedded Software, Electrical)" in answer):
        answer = answer.replace("Hardware (Embedded Software, Electrical)", "Hardware")
    if("Yes, but is hybrid" in answer):
        answer = answer.replace("Yes, but is hybrid", "Yes but is hybrid")
    if("Cold Applying (on company website, LinkedIn, job boards, etc.)" in answer):
        answer = answer.replace("Cold Applying (on company website, LinkedIn, job boards, etc.)", "Cold Applying")
        
    return answer

def main():
    df = pd.read_csv(input_csv_path)
    df = df.drop(columns = ['Timestamp', 'Questions Comments Concerns Suggestions Feedback for this section'])

    df_fuf_clean = rename_column_headers(df)
    df_rename_column = df_fuf_clean.copy()
    df_rename_column.to_csv(output_rename_column_path, index = False, encoding = 'utf-8')

    for i in knowing_yourself_list:
        df_fuf_clean[i] = df_fuf_clean[i].apply(standardize_knowing_yourself)
    
    df_fuf_clean['other_school_program'] = df_fuf_clean['other_school_program'].apply(rename_different_program)
    df_fuf_clean['grad_trip_location'] = df_fuf_clean['grad_trip_location'].apply(rename_grad_trip_location)

    df_ft_job_location = split_ft_job_location(df_fuf_clean)
    df_fuf_clean = pd.concat([df_fuf_clean, df_ft_job_location], axis = 1, join = "inner")

    for i in replace_strings_fuf_list:
        df_fuf_clean[i] = df_fuf_clean[i].apply(replace_strings_fuf)

    # df_fuf_clean.to_csv(output_standard_path, index = False, encoding = 'utf-8')
    df_fuf_pii = df_fuf_clean[['grad_trip_location', 'ft_company', 'higher_ed_school', 'higher_ed_degree']]
    df_fuf_pii = df_fuf_pii.sample(frac = 1)
    df_fuf_no_pii = df_fuf_clean.drop(columns = ['grad_trip_location', 'ft_company', 'higher_ed_school', 'higher_ed_degree'])

    df_fuf_pii.to_csv(output_pii_path, index=False, encoding='utf-8')
    df_fuf_no_pii.to_csv(output_standard_path, index=False, encoding='utf-8')

    df_finances = df_fuf_clean[[
        'uid',
        'debt',
        'tuition_self_fund',
        'wusa_optional',
        'wusa_services_used',
        'part_time_job_school',
        'job_school',
        'scholarships',
        'investments',
        'groceries_per_month',
        'monthly_budget',
        'cost_course_materials'
    ]]

    df_undergrad_reflections = df_fuf_clean[[
        'uid',
        'syde_again',
        'other_school_program',
        'syde_satisfied',
        'syde_belonged',
        'syde_community',
        'aspiring_engineer',
        'syde_trad_eng',
        'syde_prof_quality',
        'syde_course_quality',
        'syde_support_quality',
        'syde_missing_courses',
        'syde_excessive_courses',
        'uw_satisfied',
        'friends_outside_syde',
        'friends_outside_eng',
        'ec_satisfied',
        'kw_enjoy_1',
        'kw_enjoy_4',
        'uw_atmosphere_1',
        'uw_atmosphere_2',
        'uw_atmosphere_3',
        'uw_atmosphere_4'
    ]]

    df_ug_si = df_fuf_clean[[
        'uid',
        'iq_1',
        'eq_1',
        'social_skills_1',
        'attractiveness_1',
        'earning_potential_1',
        'morals_1',
        'ethics_1',
        'work_ethic_1',
        'confidence_1',
        'self_understanding_1',
        'teamwork_1',
        'self_esteem_1',
        'iq_4',
        'eq_4',
        'social_skills_4',
        'attractiveness_4',
        'earning_potential_4',
        'morals_4',
        'ethics_4',
        'work_ethic_4',
        'confidence_4',
        'self_understanding_4',
        'teamwork_4',
        'self_esteem_4'
    ]]

    df_future_plans = df_fuf_clean[[
        'uid',
        'convocation',
        'future_eng_role',
        'p_eng',
        'in_touch_classmates',
        'donations',
        'age_of_marriage',
        'age_of_children',
        'location_settling',
        'grad_trip',
        'reunion',
        'world_change',
        'future_industries',
        'future_job_title',
        'future_higher_ed',
        'postgrad_plans',
        'postgrad_leave_canada',
        'return_to_canada',
        'return_to_canada_reasons'
    ]]

    df_future_job_reflections = df_fuf_clean[[
        'uid',
        'job_security_optimism',
        'job_market_optimism',
        'career_direction',
        'ft_job_satisfaction',
        'ft_wlb',
        'ft_impact',
        'ft_comp',
        'ft_prestige',
        'ft_team',
        'ft_boss',
        'ft_perks',
        'ft_benefits',
        'ft_projects',
        'ft_skill_development',
        'ft_location',
        'ft_company_culture',
        'ft_proximity_social',
        'ft_company_industry',
        'ft_remote_flex'
    ]]

    df_ft = df_fuf_clean[[
        'uid',
        'ft_job_title',
        'ft_category',
        'ft_job_location',
        'ft_remote',
        'ft_company_size',
        'ft_industry',
        'ft_tc',
        'ft_tc_base',
        'ft_tc_equity',
        'ft_tc_bonus',
        'ft_find_job',
        'ft_offer_letter',
        'ft_factors',
        'ft_apps',
        'ft_interviews',
        'ft_interview_rounds',
        'ft_offers',
        'ft_other_categories',
        'ft_job_city',
        'ft_job_country'
    ]]

    df_sft = df_fuf_clean[[
        'uid',
        'sft_categories',
        'sft_pursuing',
        'sft_apps',
        'sft_interviews',
        'sft_locations'
    ]]

    df_higher_ed = df_fuf_clean[[
        'uid',
        'higher_ed_offer',
        'higher_ed_program',
        'higher_ed_supervisor',
        'higher_ed_postgrad_plans'
    ]]

    df_fto = df_fuf_clean[[
        'uid',
        'time_off_living',
        'time_off_doing',
        'time_off_personal_venture',
        'time_off_future_plans'
    ]]

    df_finances.to_csv(output_split_path + 'finances.csv', index = False, encoding='utf-8')
    df_undergrad_reflections.to_csv(output_split_path + 'undergrad_reflections.csv', index = False, encoding='utf-8')
    df_ug_si.to_csv(output_split_path + 'undergrad_self_improvement.csv', index = False, encoding='utf-8')
    df_future_plans.to_csv(output_split_path + 'future_plans.csv', index = False, encoding='utf-8')
    df_future_job_reflections.to_csv(output_split_path + 'future_job_reflections.csv', index = False, encoding='utf-8')
    df_ft.to_csv(output_split_path + 'full_time_jobs.csv', index = False, encoding='utf-8')
    df_sft.to_csv(output_split_path + 'searching_full_time_jobs.csv', index = False, encoding='utf-8')
    df_higher_ed.to_csv(output_split_path + 'higher_ed.csv', index = False, encoding='utf-8')
    df_fto.to_csv(output_split_path + 'future_time_off.csv', index = False, encoding='utf-8')

if __name__ == "__main__":
    main()