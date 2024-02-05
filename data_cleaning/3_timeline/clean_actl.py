import pandas as pd
import math
import re
import statistics
import numpy as np

###### DEV VARIABLES ########
input_csv_path = 'C:\\Users\\Kha\\Documents\\Programming\\SYDE2023_Class_Profile\\csv\\raw\\3_ACTL.csv'
output_rename_column_path = 'C:\\Users\\Kha\\Documents\\Programming\\SYDE2023_Class_Profile\\csv\\renamed_columns\\3_ACTL_renamed.csv'
output_standard_path = 'C:\\Users\\Kha\\Documents\\Programming\\SYDE2023_Class_Profile\\csv\\final\\3_ACTL_final.csv'
output_split_path = 'C:\\Users\\Kha\\Documents\\Programming\\SYDE2023_Class_Profile\\csv\\final\\split\\timeline_'

##### GLOBAL #######

temp_city_list = []
temp_province_list = []
temp_state_list = []
temp_region_list = []
temp_country_list = []

###### MAPPINGS #########
def standardize_coop_locations(location):
    if(type(location) == float):
        if(math.isnan(location)):
            return location
    
    location = location.lower()
    if("vancouver" in location or location == "vancovuer"):
        formatted_location = "Vancouver,British Colombia,,BC,Canada"
    elif("home toronto" in location or location == "etobicoke" or "north york" in location or location == "remote / toronto" or "toronto" in location):
        formatted_location = "Toronto,Ontario,,Toronto,Canada"
    elif("markham (home)" in location or "markham" in location):
        formatted_location = "Markham,Ontario,,GTA,Canada"
    elif("home" in location or location == "with family"):
        formatted_location = "Home,,,,"
    elif(location == "cambridge ontario, and st. catharines ontario"):
        formatted_location = "Cambridge,Ontario,,KWC,Canada"
    elif(location == "gta/montreal" or "montreal" in location):
         formatted_location = "Montreal,Quebec,,QC,Canada"
    elif("austin" in location):
        formatted_location = "Austin,,Texas,Southern US,USA"
    elif("barrie" in location):
        formatted_location = "Barrie,Ontario,,ON,Canada"
    elif(location == "bc"):
        formatted_location = ",British Colombia,,BC,Canada"
    elif("berlin" in location):
        formatted_location = "Berlin,,,Europe,Germany"
    elif("boston" in location):
        formatted_location = "Boston,,Massachusetts,Northeastern US,USA"
    elif("brampton" in location):
        formatted_location = "Brampton,Ontario,,GTA,Canada"
    elif("burlington" in location):
        formatted_location = "Burlington,Ontario,,Halton,Canada"
    elif("calgary" in location):
        formatted_location = "Calgary,Alberta,,AB,Canada"
    elif(location == "california"):
        formatted_location = ",,California,California,USA"
    elif("cambridge" in location):
        formatted_location = "Cambridge,Ontario,,KWC,Canada"
    elif(location == "canada" or location == "other province other than home"):
        formatted_location = ",,,,Canada"
    elif(location == "costa rica"):
        formatted_location = ",,,,Costa Rica"
    elif("edmonton" in location):
        formatted_location = "Edmonton,Alberta,,AB,Canada"
    # elif(location == "etobicoke"):
    #     formatted_location = "Toronto,Ontario,,GTA,Canada"
    elif(location == "fort erie"):
         formatted_location = "Fort Erie,Ontario,,ON,Canada"
    elif("fremont" in location):
         formatted_location = "Fremont,,California,Bay Area,USA"
    elif("guelph" in location):
         formatted_location = "Guelph,Ontario,,ON,Canada"
    elif("hamilton" in location):
         formatted_location = "Hamilton,Ontario,,Hamilton,Canada"
    elif(location == "honey harbour"):
         formatted_location = "Honey Harbour,Ontario,,ON,Canada"
    elif(location == "italy"):
         formatted_location = ",,,Europe,Italy"
    elif("kanata" in location):
         formatted_location = "Kanata,Ontario,,NCR,Canada"
    elif("kitchener" in location or location == "kitchener, waterloo" or location == "kw"):
         formatted_location = "Kitchener,Ontario,,KWC,Canada"
    elif(location == "lehi, utah"):
         formatted_location = "Lehi,,Utah,Southwestern US,USA"
    elif("menlo park" in location):
         formatted_location = "Menlo Park,,California,Bay Area,USA"
    elif(location == "michigan"):
         formatted_location = ",,Michigan,Midwestern US,USA"
    elif(location == "missisagua" or "mississauga" in location):
         formatted_location = "Mississauga,Ontario,,GTA,Canada"
    elif("mountain view" in location):
        formatted_location = "Mountain View,,California,Bay Area,USA"
    elif("new york" in location):
        formatted_location = "New York City,,New York,NYC,USA"
    elif("newmarket" in location):
        formatted_location = "Newmarket,Ontario,,ON,Canada"
    elif("oakville" in location):
        formatted_location = "Oakville,Ontario,,Halton,Canada"
    elif(location == "ontario"):
        formatted_location = ",Ontario,,ON,Canada"
    elif("ottawa" in location):
        formatted_location = "Ottawa,Ontario,,NCR,Canada"
    elif("palo alto" in location):
        formatted_location = "Palo Alto,,California,Bay Area,Canada"
    elif("phoenix" in location):
        formatted_location = "Phoenix,,Arizona,Southwestern US,Canada"
    elif("powell river" in location):
        formatted_location = "Powell River,British Colombia,,BC,Canada"
    elif("redmond" in location):
        formatted_location = "Redmond,,Washington,Northwestern US,USA"
    elif("redwood" in location):
        formatted_location = "Redwood City,,California,Bay Area,USA"
    elif("remote" in location):
        formatted_location = np.nan
    elif("san francisco" in location):
        formatted_location = "San Francisco,,California,Bay Area,USA"
    elif("santa clara" in location):
        formatted_location = "Santa Clara,,California,Bay Area,USA"
    elif("seattle" in location):
        formatted_location = "Seattle,,Washington,Northwestern US, USA"
    elif("trenton" in location):
        formatted_location = "Trenton,Ontario,,ON,Canada"
    elif(location == "u.s." or location == "united states"):
        formatted_location = ",,,,USA"
    elif("vaughan" in location):
        formatted_location = "Vaughan,Ontario,,GTA,Canada"
    elif("waterloo" in location):
        formatted_location = "Waterloo,Ontario,,KWC,Canada"
    elif("winnipeg" in location):
        formatted_location = "Winnipeg,Manitoba,,Central Canada,Canada"
    else:
        formatted_location = np.nan
    return formatted_location

######## FUNCTIONS #############

def rename_column_headers(df):
    df = df.rename(columns = {
        "What is your unique ID": "uid",
        "Acknowledgement": "acknowledgement",
        "Compared to all the courses we took in the degree, rank the EASINESS of the following courses [SYDE 101 (Intro. to Comm. in Eng.)]": "easiness_101",
        "Compared to all the courses we took in the degree, rank the EASINESS of the following courses [SYDE 101L (Graphics / SolidWorks)]": "easiness_101L",
        "Compared to all the courses we took in the degree, rank the EASINESS of the following courses [SYDE 111 (Calc 1)]": "easiness_111",
        "Compared to all the courses we took in the degree, rank the EASINESS of the following courses [SYDE 113 (Mtrix + Lin Sys)]": "easiness_113",
        "Compared to all the courses we took in the degree, rank the EASINESS of the following courses [SYDE 121 (C++)]": "easiness_121",
        "Compared to all the courses we took in the degree, rank the EASINESS of the following courses [SYDE 161 (Intro. to Des.)]": "easiness_161",
        "Compared to all the courses we took in the degree, rank the EASINESS of the following courses [SYDE 181 (Statics)]": "easiness_181",
        "Compared to all the courses we took in the degree, rank the USEFULNESS of the following courses [SYDE 101 (Intro. to Comm. in Eng.)]": "usefulness_101",
        "Compared to all the courses we took in the degree, rank the USEFULNESS of the following courses [SYDE 101L (Graphics / SolidWorks)]": "usefulness_101L",
        "Compared to all the courses we took in the degree, rank the USEFULNESS of the following courses [SYDE 111 (Calc 1)]": "usefulness_111",
        "Compared to all the courses we took in the degree, rank the USEFULNESS of the following courses [SYDE 113 (Mtrix + Lin Sys)]": "usefulness_113",
        "Compared to all the courses we took in the degree, rank the USEFULNESS of the following courses [SYDE 121 (C++)]": "usefulness_121",
        "Compared to all the courses we took in the degree, rank the USEFULNESS of the following courses [SYDE 161 (Intro. to Des.)]": "usefulness_161",
        "Compared to all the courses we took in the degree, rank the USEFULNESS of the following courses [SYDE 181 (Statics)]": "usefulness_181",
        "What was your Term GPA in 1A (%)": "gpa_1a",
        "How often did you attend lectures 1A": "lectures_1a",
        "Where did you live in in 1A": "living_1a",
        "What was your commute time to campus in minutes 1A": "commute_1a",
        "How many hours of sleep on average did you get each night during this term 1A": "sleep_1a",
        "How many hours of schoolwork did you do on average per week 1A": "schoolwork_1a",
        "How stressful was this term? 1A": "stress_1a",
        "What was your mental health like this term 1A": "mental_health_1a",
        "When searching for co-op jobs, how many applications did you send out 1A": "apps_1a",
        "When searching for co-op jobs, how many interviews did you get 1A": "interviews_1a",
        "When searching for co-op jobs, how many WaterlooWorks Ranked statuses did you receive? 1A": "ranked_1a",
        "When searching for co-op jobs, how many offers did you receive 1A": "offers_1a",
        "How much did you pay for rent this term per month 1A": "rent_1a",
        "Were you employed at a co-op job at any point in this term C1": "employed_c1",
        "What was the title of your job C1": "job_title_c1",
        "Select the category below that best represents your co-op job C1": "coop_cat_c1",
        "In which location(s) was your job located C1": "location_c1",
        "Was this position remote? C1": "remote_c1",
        "If you worked remotely, where did you live during this co-op term? C1": "living_c1",
        "What was the size of this company C1": "company_size_c1",
        "Select the industry that best relates to your company C1": "industry_c1",
        "Assuming a 37.5 hour work week, what was your hourly wage in CAD? C1": "pay_c1",
        "How did you find this job C1": "find_job_c1",
        "Which rating did you receive on WaterlooWorks for this co-op position C1": "ww_rating_c1",
        "What was your commute time to this job in minutes C1": "commute_c1",
        "How much did you enjoy working at this co-op placement C1": "enjoy_c1",
        "At this time, how relevant was this position for your future employment plans C1": "relevance_c1",
        "What was your mental health like this term C1": "mental_health_c1",
        "How much did you pay for rent this term per month C1": "rent_c1",
        "Compared to all the courses we took in the degree, rank the EASINESS of the following courses [SYDE 112 (Calc 2)]": "easiness_112",
        "Compared to all the courses we took in the degree, rank the EASINESS of the following courses [SYDE 114 (Mtrix + Lin Sys)]": "easiness_114",
        "Compared to all the courses we took in the degree, rank the EASINESS of the following courses [SYDE 162 (Human Factors)]": "easiness_162",
        "Compared to all the courses we took in the degree, rank the EASINESS of the following courses [SYDE 182 (Dynamics)]": "easiness_182",
        "Compared to all the courses we took in the degree, rank the EASINESS of the following courses [SYDE 192 (Digital Logic)]": "easiness_192",
        "Compared to all the courses we took in the degree, rank the EASINESS of the following courses [SYDE 192L (Digital Logic Lab)]": "easiness_192L",
        "Compared to all the courses we took in the degree, rank the USEFULNESS of the following courses [SYDE 112 (Calc 2)]": "usefulness_112",
        "Compared to all the courses we took in the degree, rank the USEFULNESS of the following courses [SYDE 114 (Mtrix + Lin Sys)]": "usefulness_114",
        "Compared to all the courses we took in the degree, rank the USEFULNESS of the following courses [SYDE 162 (Human Factors)]": "usefulness_162",
        "Compared to all the courses we took in the degree, rank the USEFULNESS of the following courses [SYDE 182 (Dynamics)]": "usefulness_182",
        "Compared to all the courses we took in the degree, rank the USEFULNESS of the following courses [SYDE 192 (Digital Logic)]": "usefulness_192",
        "Compared to all the courses we took in the degree, rank the USEFULNESS of the following courses [SYDE 192L (Digital Logic Lab)]": "usefulness_192L",
        "What was your Term GPA in 1B (%)": "gpa_1b",
        "How often did you attend lectures 1B": "lectures_1b",
        "Where did you live in in 1B": "living_1b",
        "What was your commute time to campus in minutes 1B": "commute_1b",
        "How many hours of sleep on average did you get each night during this term 1B": "sleep_1b",
        "How many hours of schoolwork did you do on average per week 1B": "schoolwork_1b",
        "How stressful was this term? 1B": "stress_1b",
        "What was your mental health like this term 1B": "mental_health_1b",
        "When searching for co-op jobs, how many applications did you send out 1B": "apps_1b",
        "When searching for co-op jobs, how many interviews did you get 1B": "interviews_1b",
        "When searching for co-op jobs, how many WaterlooWorks Ranked statuses did you receive? 1B": "ranked_1b",
        "When searching for co-op jobs, how many offers did you receive 1B": "offers_1b",
        "How much did you pay for rent this term per month 1B": "rent_1b",
        "Were you employed at a co-op job at any point in this term C2": "employed_c2",
        "What was the title of your job C2": "job_title_c2",
        "Select the category below that best represents your co-op job C2": "coop_cat_c2",
        "In which location(s) was your job located C2": "location_c2",
        "Was this position remote? C2": "remote_c2",
        "If you worked remotely, where did you live during this co-op term? C2": "living_c2",
        "What was the size of this company C2": "company_size_c2",
        "Select the industry that best relates to your company C2": "industry_c2",
        "Assuming a 37.5 hour work week, what was your hourly wage in CAD? C2": "pay_c2",
        "How did you find this job C2": "find_job_c2",
        "Which rating did you receive on WaterlooWorks for this co-op position C2": "ww_rating_c2",
        "What was your commute time to this job in minutes C2": "commute_c2",
        "How much did you enjoy working at this co-op placement C2": "enjoy_c2",
        "At this time, how relevant was this position for your future employment plans C2": "relevance_c2",
        "What was your mental health like this term C2": "mental_health_c2",
        "How much did you pay for rent this term per month C2": "rent_c2",
        "Compared to all the courses we took in the degree, rank the EASINESS of the following courses [SYDE 211 (Calc 3)]": "easiness_211",
        "Compared to all the courses we took in the degree, rank the EASINESS of the following courses [SYDE 223 (Data Structures)]": "easiness_223",
        "Compared to all the courses we took in the degree, rank the EASINESS of the following courses [SYDE 261 (Design, Systems, and Society)]": "easiness_261",
        "Compared to all the courses we took in the degree, rank the EASINESS of the following courses [SYDE 283 (EMO)]": "easiness_283",
        "Compared to all the courses we took in the degree, rank the EASINESS of the following courses [SYDE 285 (Materials)]": "easiness_285",
        "Compared to all the courses we took in the degree, rank the USEFULNESS of the following courses [SYDE 211 (Calc 3)]": "usefulness_211",
        "Compared to all the courses we took in the degree, rank the USEFULNESS of the following courses [SYDE 223 (Data Structures)]": "usefulness_223",
        "Compared to all the courses we took in the degree, rank the USEFULNESS of the following courses [SYDE 261 (Design, Systems, and Society)]": "usefulness_261",
        "Compared to all the courses we took in the degree, rank the USEFULNESS of the following courses [SYDE 283 (EMO)]": "usefulness_283",
        "Compared to all the courses we took in the degree, rank the USEFULNESS of the following courses [SYDE 285 (Materials)]": "usefulness_285",
        "What was your Term GPA in 2A (%)": "gpa_2a",
        "How often did you attend lectures 2A": "lectures_2a",
        "Where did you live in in 2A": "living_2a",
        "What was your commute time to campus in minutes 2A": "commute_2a",
        "How many hours of sleep on average did you get each night during this term 2A": "sleep_2a",
        "How many hours of schoolwork did you do on average per week 2A": "schoolwork_2a",
        "How stressful was this term? 2A": "stress_2a",
        "What was your mental health like this term 2A": "mental_health_2a",
        "When searching for co-op jobs, how many applications did you send out 2A": "apps_2a",
        "When searching for co-op jobs, how many interviews did you get 2A": "interviews_2a",
        "When searching for co-op jobs, how many WaterlooWorks Ranked statuses did you receive? 2A": "ranked_2a",
        "When searching for co-op jobs, how many offers did you receive 2A": "offers_2a",
        "How much did you pay for rent this term per month 2A": "rent_2a",
        "Were you employed at a co-op job at any point in this term C3": "employed_c3",
        "What was the title of your job C3": "job_title_c3",
        "Select the category below that best represents your co-op job C3": "coop_cat_c3",
        "In which location(s) was your job located C3": "location_c3",
        "Was this position remote? C3": "remote_c3",
        "If you worked remotely, where did you live during this co-op term? C3": "living_c3",
        "What was the size of this company C3": "company_size_c3",
        "Select the industry that best relates to your company C3": "industry_c3",
        "Assuming a 37.5 hour work week, what was your hourly wage in CAD? C3": "pay_c3",
        "How did you find this job C3": "find_job_c3",
        "Which rating did you receive on WaterlooWorks for this co-op position C3": "ww_rating_c3",
        "What was your commute time to this job in minutes C3": "commute_c3",
        "How much did you enjoy working at this co-op placement C3": "enjoy_c3",
        "At this time, how relevant was this position for your future employment plans C3": "relevance_c3",
        "What was your mental health like this term C3": "mental_health_c3",
        "How much did you pay for rent this term per month C3": "rent_c3",
        "Compared to all the courses we took in the degree, rank the EASINESS of the following courses [SYDE 212 (Prob + Stats)]": "easiness_212",
        "Compared to all the courses we took in the degree, rank the EASINESS of the following courses [SYDE 252 (Signals)]": "easiness_252",
        "Compared to all the courses we took in the degree, rank the EASINESS of the following courses [SYDE 262 (Econ)]": "easiness_262",
        "Compared to all the courses we took in the degree, rank the EASINESS of the following courses [SYDE 286 (MODS)]": "easiness_286",
        "Compared to all the courses we took in the degree, rank the EASINESS of the following courses [SYDE 292 (Circuits)]": "easiness_292",
        "Compared to all the courses we took in the degree, rank the EASINESS of the following courses [SYDE 292L (Circuits Lab)]": "easiness_292L",
        "Compared to all the courses we took in the degree, rank the USEFULNESS of the following courses [SYDE 212 (Prob + Stats)]": "usefulness_212",
        "Compared to all the courses we took in the degree, rank the USEFULNESS of the following courses [SYDE 252 (Signals)]": "usefulness_252",
        "Compared to all the courses we took in the degree, rank the USEFULNESS of the following courses [SYDE 262 (Econ)]": "usefulness_262",
        "Compared to all the courses we took in the degree, rank the USEFULNESS of the following courses [SYDE 286 (MODS)]": "usefulness_286",
        "Compared to all the courses we took in the degree, rank the USEFULNESS of the following courses [SYDE 292 (Circuits)]": "usefulness_292",
        "Compared to all the courses we took in the degree, rank the USEFULNESS of the following courses [SYDE 292L (Circuits Lab)]": "usefulness_292L",
        "What was your Term GPA in 2B (%)": "gpa_2b",
        "How often did you attend lectures 2B": "lectures_2b",
        "Where did you live in in 2B": "living_2b",
        "What was your commute time to campus in minutes 2B": "commute_2b",
        "How many hours of sleep on average did you get each night during this term 2B": "sleep_2b",
        "How many hours of schoolwork did you do on average per week 2B": "schoolwork_2b",
        "How stressful was this term? 2B": "stress_2b",
        "What was your mental health like this term 2B": "mental_health_2b",
        "When searching for co-op jobs, how many applications did you send out 2B": "apps_2b",
        "When searching for co-op jobs, how many interviews did you get 2B": "interviews_2b",
        "When searching for co-op jobs, how many WaterlooWorks Ranked statuses did you receive? 2B": "ranked_2b",
        "When searching for co-op jobs, how many offers did you receive 2B": "offers_2b",
        "How much did you pay for rent this term per month 2B": "rent_2b",
        "Were you employed at a co-op job at any point in this term C4": "employed_c4",
        "What was the title of your job C4": "job_title_c4",
        "Select the category below that best represents your co-op job C4": "coop_cat_c4",
        "In which location(s) was your job located C4": "location_c4",
        "Was this position remote? C4": "remote_c4",
        "If you worked remotely, where did you live during this co-op term? C4": "living_c4",
        "What was the size of this company C4": "company_size_c4",
        "Select the industry that best relates to your company C4": "industry_c4",
        "Assuming a 37.5 hour work week, what was your hourly wage in CAD? C4": "pay_c4",
        "How did you find this job C4": "find_job_c4",
        "Which rating did you receive on WaterlooWorks for this co-op position C4": "ww_rating_c4",
        "What was your commute time to this job in minutes C4": "commute_c4",
        "How much did you enjoy working at this co-op placement C4": "enjoy_c4",
        "At this time, how relevant was this position for your future employment plans C4": "relevance_c4",
        "What was your mental health like this term C4": "mental_health_c4",
        "How much did you pay for rent this term per month C4": "rent_c4",
        "Compared to all the courses we took in the degree, rank the EASINESS of the following courses [SYDE 311 (Calc 4)]": "easiness_311",
        "Compared to all the courses we took in the degree, rank the EASINESS of the following courses [SYDE 351 (Systems Models)]": "easiness_351",
        "Compared to all the courses we took in the degree, rank the EASINESS of the following courses [SYDE 361 (Needs Analysis + Prototyping)]": "easiness_361",
        "Compared to all the courses we took in the degree, rank the EASINESS of the following courses [SYDE 381 (Thermo)]": "easiness_381",
        "Compared to all the courses we took in the degree, rank the EASINESS of the following courses [SYDE 383 (Fluids)]": "easiness_383",
        "Compared to all the courses we took in the degree, rank the USEFULNESS of the following courses [SYDE 311 (Calc 4)]": "usefulness_311",
        "Compared to all the courses we took in the degree, rank the USEFULNESS of the following courses [SYDE 351 (Systems Models)]": "usefulness_351",
        "Compared to all the courses we took in the degree, rank the USEFULNESS of the following courses [SYDE 361 (Needs Analysis + Prototyping)]": "usefulness_361",
        "Compared to all the courses we took in the degree, rank the USEFULNESS of the following courses [SYDE 381 (Thermo)]": "usefulness_381",
        "Compared to all the courses we took in the degree, rank the USEFULNESS of the following courses [SYDE 383 (Fluids)]": "usefulness_383",
        "What was your Term GPA in 3A (%)": "gpa_3a",
        "How often did you attend lectures 3A": "lectures_3a",
        "Did you taste the ink? 3A": "taste_ink",
        "Where did you live in in 3A": "living_3a",
        "What was your commute time to campus in minutes 3A": "commute_3a",
        "How many hours of sleep on average did you get each night during this term 3A": "sleep_3a",
        "How many hours of schoolwork did you do on average per week 3A": "schoolwork_3a",
        "How stressful was this term? 3A": "stress_3a",
        "What was your mental health like this term 3A": "mental_health_3a",
        "When searching for co-op jobs, how many applications did you send out 3A": "apps_3a",
        "When searching for co-op jobs, how many interviews did you get 3A": "interviews_3a",
        "When searching for co-op jobs, how many WaterlooWorks Ranked statuses did you receive? 3A": "ranked_3a",
        "When searching for co-op jobs, how many offers did you receive 3A": "offers_3a",
        "How much did you pay for rent this term per month 3A": "rent_3a",
        "Were you employed at a co-op job at any point in this term C5": "employed_c5",
        "What was the title of your job C5": "job_title_c5",
        "Select the category below that best represents your co-op job C5": "coop_cat_c5",
        "In which location(s) was your job located C5": "location_c5",
        "Was this position remote? C5": "remote_c5",
        "If you worked remotely, where did you live during this co-op term? C5": "living_c5",
        "What was the size of this company C5": "company_size_c5",
        "Select the industry that best relates to your company C5": "industry_c5",
        "Assuming a 37.5 hour work week, what was your hourly wage in CAD? C5": "pay_c5",
        "How did you find this job C5": "find_job_c5",
        "Which rating did you receive on WaterlooWorks for this co-op position C5": "ww_rating_c5",
        "What was your commute time to this job in minutes C5": "commute_c5",
        "How much did you enjoy working at this co-op placement C5": "enjoy_c5",
        "At this time, how relevant was this position for your future employment plans C5": "relevance_c5",
        "What was your mental health like this term C5": "mental_health_c5",
        "How much did you pay for rent this term per month C5": "rent_c5",
        "Compared to all the courses we took in the degree, rank the EASINESS of the following courses [SYDE 312 (Lin Alg 2)]": "easiness_312",
        "Compared to all the courses we took in the degree, rank the EASINESS of the following courses [SYDE 352 (Controls)]": "easiness_352",
        "Compared to all the courses we took in the degree, rank the EASINESS of the following courses [SYDE 352L (Controls Lab)]": "easiness_352L",
        "Compared to all the courses we took in the degree, rank the EASINESS of the following courses [SYDE 362 (Testing)]": "easiness_362",
        "Compared to all the courses we took in the degree, rank the USEFULNESS of the following courses [SYDE 312 (Lin Alg 2)]": "usefulness_312",
        "Compared to all the courses we took in the degree, rank the USEFULNESS of the following courses [SYDE 352 (Controls)]": "usefulness_352",
        "Compared to all the courses we took in the degree, rank the USEFULNESS of the following courses [SYDE 352L (Controls Lab)]": "usefulness_352L",
        "Compared to all the courses we took in the degree, rank the USEFULNESS of the following courses [SYDE 362 (Testing)]": "usefulness_362",
        "What was your Term GPA in 3B (%)": "gpa_3b",
        "How often did you attend lectures 3B": "lectures_3b",
        "How many Birkett lectures (SYDE 312) did you attend in person? 3B": "birkett_3b",
        "Where did you live in in 3B": "living_3b",
        "What was your commute time to campus in minutes 3B": "commute_3b",
        "How many hours of sleep on average did you get each night during this term 3B": "sleep_3b",
        "How many hours of schoolwork did you do on average per week 3B": "schoolwork_3b",
        "How stressful was this term? 3B": "stress_3b",
        "What was your mental health like this term 3B": "mental_health_3b",
        "When searching for co-op jobs, how many applications did you send out 3B": "apps_3b",
        "When searching for co-op jobs, how many interviews did you get 3B": "interviews_3b",
        "When searching for co-op jobs, how many WaterlooWorks Ranked statuses did you receive? 3B": "ranked_3b",
        "When searching for co-op jobs, how many offers did you receive 3B": "offers_3b",
        "How much did you pay for rent this term per month 3B": "rent_3b",
        "Were you employed at a co-op job at any point in this term C6": "employed_c6",
        "What was the title of your job C6": "job_title_c6",
        "Select the category below that best represents your co-op job C6": "coop_cat_c6",
        "In which location(s) was your job located C6": "location_c6",
        "Was this position remote? C6": "remote_c6",
        "If you worked remotely, where did you live during this co-op term? C6": "living_c6",
        "What was the size of this company C6": "company_size_c6",
        "Select the industry that best relates to your company C6": "industry_c6",
        "Assuming a 37.5 hour work week, what was your hourly wage in CAD? C6": "pay_c6",
        "How did you find this job C6": "find_job_c6",
        "Which rating did you receive on WaterlooWorks for this co-op position C6": "ww_rating_c6",
        "What was your commute time to this job in minutes C6": "commute_c6",
        "How much did you enjoy working at this co-op placement C6": "enjoy_c6",
        "At this time, how relevant was this position for your future employment plans C6": "relevance_c6",
        "What was your mental health like this term C6": "mental_health_c6",
        "How much did you pay for rent this term C6": "rent_c6",
        "Compared to all the courses we took in the degree, rank the EASINESS of the following courses [SYDE 411 (Optimization)]": "easiness_411",
        "Compared to all the courses we took in the degree, rank the EASINESS of the following courses [SYDE 461 (FYDP 1)]": "easiness_461",
        "Compared to all the courses we took in the degree, rank the USEFULNESS of the following courses [SYDE 411 (Optimization)]": "usefulness_411",
        "Compared to all the courses we took in the degree, rank the USEFULNESS of the following courses [SYDE 461 (FYDP 1)]": "usefulness_461",
        "What was your Term GPA in 4A (%)": "gpa_4a",
        "How often did you attend lectures 4A": "lectures_4a",
        "Where did you live in in 4A": "living_4a",
        "What was your commute time to campus in minutes 4A": "commute_4a",
        "How many hours of sleep on average did you get each night during this term 4A": "sleep_4a",
        "How many hours of schoolwork (except FYDP) did you do on average per week 4A": "schoolwork_4a",
        "How many hours of work did you spend on FYDP on average per week 4A": "fydp_4a",
        "How stressful was this term? 4A": "stress_4a",
        "What was your mental health like this term 4A": "mental_health_4a",
        "How much did you pay for rent this term per month 4A": "rent_4a",
        "Compared to all the courses we took in the degree, rank the EASINESS of the following courses [SYDE 462 (FYDP 2)]": "easiness_462",
        "Compared to all the courses we took in the degree, rank the USEFULNESS of the following courses [SYDE 462 (FYDP 2)]": "usefulness_462",
        "What was your Term GPA in 4B (%)": "gpa_4b",
        "How often did you attend lectures 4B": "lectures_4b",
        "Where did you live in in 4B": "living_4b",
        "What was your commute time to campus in minutes 4B": "commute_4b",
        "How many hours of sleep on average did you get each night during this term 4B": "sleep_4b",
        "How many hours of schoolwork (except FYDP) did you do on average per week 4B": "schoolwork_4b",
        "How many hours of work did you spend on FYDP on average per week 4B": "fydp_4b",
        "How stressful was this term? 4B": "stress_4b",
        "What was your mental health like this term 4B": "mental_health_4b",
        "How much did you pay for rent this term per month 4B": "rent_4b"
    })

    return df

def clean_course_easiness(rating):
    try:
        if(rating == '1 (Extremely Difficult)'):
            return 1
        elif(rating == '7 (Extremely Easy)'):
            return 7
        else:
            cleaned_rating = int(rating)
            return cleaned_rating
    except:
        return rating
    
def clean_course_usefulness(rating):
    try:
        if(rating == '1 (Completely Useless)'):
            return 1
        elif(rating == '7 (Extremely Useful)'):
            return 7
        else:
            cleaned_rating = int(rating)
            return cleaned_rating
    except:
        return rating

def turn_dates_into_actual_values(dates):
    if(type(dates) == float):
        if(math.isnan(dates)):
            return dates
    
    if(dates == '05-Jan'):
        return '1 - 5'
    elif(dates == '10-Jun'):
        return '6 - 10'
    elif(dates == '15-Nov'):
        return '11 - 15'
    elif(dates == '05-Apr'):
        return '4 - 5'
    elif(dates == '06-May'):
        return '5 - 6'
    elif(dates == '07-Jun'):
        return '6 - 7'
    elif(dates == '08-Jul'):
        return '7 - 8'
    elif(dates == '09-Aug'):
        return '8 - 9'
    elif(dates == '10-Sep'):
        return '9 - 10'
    elif(dates == '11-Oct'):
        return '10 - 11'
    elif(dates == '12-Nov'):
        return '11 - 12'
    elif(dates == '10-May'):
        return '5 - 10'
    elif(dates == '25-Jan'):
        return '1 - 25'
    else:
        return dates
    
def remove_nonnumeric_char(string):
    if(type(string) == float):
        if(math.isnan(string)):
            return string
        
    cleaned_string = re.sub("[^0-9.]", "", str(string))
    cleaned_string = cleaned_string.strip()
    return cleaned_string

def remove_nonnumeric_char_except(string):
    if(type(string) == float):
        if(math.isnan(string)):
            return string
        
    cleaned_string = re.sub("[^0-9+.-]", "", str(string))
    cleaned_string = cleaned_string.strip()
    return cleaned_string

def take_mean_between_dash(string):
    if(type(string) == float):
        if(math.isnan(string)):
            return string
        
    if("-" in string):
        temp = string.split("-")
        average = statistics.mean([float(temp[0].strip()), float(temp[1].strip())])
        return average
    
    return string

def format_location_columns(df, column_name):
    df[column_name].apply(parse_location_column) # shouldn't do anything to the DF, but populate the global lists
    df_location = concat_location_df(column_name) # makes the DF from the global lists
    clear_temp_global_lists()
    
    return df_location

def parse_location_column(location):
    global temp_city_list
    global temp_province_list
    global temp_state_list 
    global temp_region_list
    global temp_country_list
    
    if(type(location) == float):
        if(math.isnan(location)):
            temp_city_list.append(np.nan)
            temp_province_list.append(np.nan)
            temp_state_list.append(np.nan)
            temp_region_list.append(np.nan)
            temp_country_list.append(np.nan)
            return None
    elif(len(location) == 0 or location == ""):
        temp_city_list.append(np.nan)
        temp_province_list.append(np.nan)
        temp_state_list.append(np.nan)
        temp_region_list.append(np.nan)
        temp_country_list.append(np.nan)
        return None
        
    separated_locations = location.split(",")
    if(len(separated_locations[0].strip()) == 0):
        temp_city_list.append(np.nan)
    else:
        temp_city_list.append(separated_locations[0].strip())
    
    if(len(separated_locations[1].strip()) == 0):
        temp_province_list.append(np.nan)
    else:
        temp_province_list.append(separated_locations[1].strip())
        
    if(len(separated_locations[2].strip()) == 0):
        temp_state_list.append(np.nan)
    else:
        temp_state_list.append(separated_locations[2].strip())
        
    if(len(separated_locations[3].strip()) == 0):
        temp_region_list.append(np.nan)
    else:
        temp_region_list.append(separated_locations[3].strip())
    
    if(len(separated_locations[4].strip()) == 0):
        temp_country_list.append(np.nan)
    else:
        temp_country_list.append(separated_locations[4].strip())
    # no return
    
def concat_location_df(column_name):
    global temp_city_list
    global temp_province_list
    global temp_state_list 
    global temp_region_list
    global temp_country_list
    
    column_name_city = column_name + '_city'
    column_name_province = column_name + '_province'
    column_name_state = column_name + '_state'
    column_name_region = column_name + '_region'
    column_name_country = column_name + '_country'
    
    df_extended = pd.DataFrame({
        column_name_city: temp_city_list,
        column_name_province: temp_province_list,
        column_name_state: temp_state_list,
        column_name_region: temp_region_list,
        column_name_country: temp_country_list
    })
    
    return df_extended

def clear_temp_global_lists():
    global temp_city_list
    global temp_province_list
    global temp_state_list 
    global temp_region_list
    global temp_country_list
    
    temp_city_list = []
    temp_province_list = []
    temp_state_list = []
    temp_region_list = []
    temp_country_list = []

def main():
    df = pd.read_csv(input_csv_path)
    df = df.drop(columns = ['Timestamp', 'Acknowledgement', 'Questions Comments Concerns Suggestions Feedback for this section'])

    df_actl_clean = rename_column_headers(df)
    df_rename_column = df_actl_clean.copy()
    df_rename_column.to_csv(output_rename_column_path, index = False, encoding = 'utf-8')

    df_actl_clean[[
        'easiness_101',
        'easiness_101L',
        'easiness_111',
        'easiness_113',
        'easiness_121',
        'easiness_161',
        'easiness_181',
        'easiness_112',
        'easiness_114',
        'easiness_162',
        'easiness_182',
        'easiness_192',
        'easiness_192L',
        'easiness_211',
        'easiness_223',
        'easiness_261',
        'easiness_283',
        'easiness_285',
        'easiness_212',
        'easiness_252',
        'easiness_262',
        'easiness_286',
        'easiness_292',
        'easiness_292L',
        'easiness_311',
        'easiness_351',
        'easiness_361',
        'easiness_381',
        'easiness_383',
        'easiness_312',
        'easiness_352',
        'easiness_352L',
        'easiness_362',
        'easiness_411',
        'easiness_461',
        'easiness_462'
    ]] = df_actl_clean[[
        'easiness_101',
        'easiness_101L',
        'easiness_111',
        'easiness_113',
        'easiness_121',
        'easiness_161',
        'easiness_181',
        'easiness_112',
        'easiness_114',
        'easiness_162',
        'easiness_182',
        'easiness_192',
        'easiness_192L',
        'easiness_211',
        'easiness_223',
        'easiness_261',
        'easiness_283',
        'easiness_285',
        'easiness_212',
        'easiness_252',
        'easiness_262',
        'easiness_286',
        'easiness_292',
        'easiness_292L',
        'easiness_311',
        'easiness_351',
        'easiness_361',
        'easiness_381',
        'easiness_383',
        'easiness_312',
        'easiness_352',
        'easiness_352L',
        'easiness_362',
        'easiness_411',
        'easiness_461',
        'easiness_462'
    ]].applymap(clean_course_easiness)

    df_actl_clean[[
        'usefulness_101',
        'usefulness_101L',
        'usefulness_111',
        'usefulness_113',
        'usefulness_121',
        'usefulness_161',
        'usefulness_181',
        'usefulness_112',
        'usefulness_114',
        'usefulness_162',
        'usefulness_182',
        'usefulness_192',
        'usefulness_192L',
        'usefulness_211',
        'usefulness_223',
        'usefulness_261',
        'usefulness_283',
        'usefulness_285',
        'usefulness_212',
        'usefulness_252',
        'usefulness_262',
        'usefulness_286',
        'usefulness_292',
        'usefulness_292L',
        'usefulness_311',
        'usefulness_351',
        'usefulness_361',
        'usefulness_381',
        'usefulness_383',
        'usefulness_312',
        'usefulness_352',
        'usefulness_352L',
        'usefulness_362',
        'usefulness_411',
        'usefulness_461',
        'usefulness_462'
    ]] = df_actl_clean[[
        'usefulness_101',
        'usefulness_101L',
        'usefulness_111',
        'usefulness_113',
        'usefulness_121',
        'usefulness_161',
        'usefulness_181',
        'usefulness_112',
        'usefulness_114',
        'usefulness_162',
        'usefulness_182',
        'usefulness_192',
        'usefulness_192L',
        'usefulness_211',
        'usefulness_223',
        'usefulness_261',
        'usefulness_283',
        'usefulness_285',
        'usefulness_212',
        'usefulness_252',
        'usefulness_262',
        'usefulness_286',
        'usefulness_292',
        'usefulness_292L',
        'usefulness_311',
        'usefulness_351',
        'usefulness_361',
        'usefulness_381',
        'usefulness_383',
        'usefulness_312',
        'usefulness_352',
        'usefulness_352L',
        'usefulness_362',
        'usefulness_411',
        'usefulness_461',
        'usefulness_462'
    ]].applymap(clean_course_usefulness)

    df_actl_clean[[
        'schoolwork_1a',
        'schoolwork_1b',
        'schoolwork_2a',
        'schoolwork_2b',
        'schoolwork_3a',
        'schoolwork_3b',
        'schoolwork_4a',
        'schoolwork_4b',

        'commute_1a',
        'commute_c1',
        'commute_1b',
        'commute_c2',
        'commute_2a',
        'commute_c3',
        'commute_2b',
        'commute_c4',
        'commute_3a',
        'commute_c5',
        'commute_3b',
        'commute_c6',
        'commute_4a',
        'commute_4b',

        'sleep_1a',
        'sleep_1b',
        'sleep_2a',
        'sleep_2b',
        'sleep_3a',
        'sleep_3b',
        'sleep_4a',
        'sleep_4b',

        'fydp_4a',
        'fydp_4b'
    ]] = df_actl_clean[[
        'schoolwork_1a',
        'schoolwork_1b',
        'schoolwork_2a',
        'schoolwork_2b',
        'schoolwork_3a',
        'schoolwork_3b',
        'schoolwork_4a',
        'schoolwork_4b',

        'commute_1a',
        'commute_c1',
        'commute_1b',
        'commute_c2',
        'commute_2a',
        'commute_c3',
        'commute_2b',
        'commute_c4',
        'commute_3a',
        'commute_c5',
        'commute_3b',
        'commute_c6',
        'commute_4a',
        'commute_4b',

        'sleep_1a',
        'sleep_1b',
        'sleep_2a',
        'sleep_2b',
        'sleep_3a',
        'sleep_3b',
        'sleep_4a',
        'sleep_4b',

        'fydp_4a',
        'fydp_4b'
    ]].applymap(turn_dates_into_actual_values)

    df_actl_clean[[
        'schoolwork_1a',
        'schoolwork_1b',
        'schoolwork_2a',
        'schoolwork_2b',
        'schoolwork_3a',
        'schoolwork_3b',
        'schoolwork_4a',
        'schoolwork_4b',

        'commute_1a',
        'commute_c1',
        'commute_1b',
        'commute_c2',
        'commute_2a',
        'commute_c3',
        'commute_2b',
        'commute_c4',
        'commute_3a',
        'commute_c5',
        'commute_3b',
        'commute_c6',
        'commute_4a',
        'commute_4b',

        'sleep_1a',
        'sleep_1b',
        'sleep_2a',
        'sleep_2b',
        'sleep_3a',
        'sleep_3b',
        'sleep_4a',
        'sleep_4b',

        'fydp_4a',
        'fydp_4b',

        'gpa_1a',
        'gpa_1b',
        'gpa_2a',
        'gpa_2b',
        'gpa_3a',
        'gpa_3b',
        'gpa_4a',
        'gpa_4b',

        'pay_c1',
        'pay_c2',
        'pay_c3',
        'pay_c4',
        'pay_c5',
        'pay_c6'
    ]] = df_actl_clean[[
        'schoolwork_1a',
        'schoolwork_1b',
        'schoolwork_2a',
        'schoolwork_2b',
        'schoolwork_3a',
        'schoolwork_3b',
        'schoolwork_4a',
        'schoolwork_4b',

        'commute_1a',
        'commute_c1',
        'commute_1b',
        'commute_c2',
        'commute_2a',
        'commute_c3',
        'commute_2b',
        'commute_c4',
        'commute_3a',
        'commute_c5',
        'commute_3b',
        'commute_c6',
        'commute_4a',
        'commute_4b',

        'sleep_1a',
        'sleep_1b',
        'sleep_2a',
        'sleep_2b',
        'sleep_3a',
        'sleep_3b',
        'sleep_4a',
        'sleep_4b',

        'fydp_4a',
        'fydp_4b',

        'gpa_1a',
        'gpa_1b',
        'gpa_2a',
        'gpa_2b',
        'gpa_3a',
        'gpa_3b',
        'gpa_4a',
        'gpa_4b',

        'pay_c1',
        'pay_c2',
        'pay_c3',
        'pay_c4',
        'pay_c5',
        'pay_c6'
    ]].applymap(remove_nonnumeric_char_except)

    df_actl_clean[[
        'commute_1a',
        'commute_c1',
        'commute_1b',
        'commute_c2',
        'commute_2a',
        'commute_c3',
        'commute_2b',
        'commute_c4',
        'commute_3a',
        'commute_c5',
        'commute_3b',
        'commute_c6',
        'commute_4a',
        'commute_4b',

        'sleep_1a',
        'sleep_1b',
        'sleep_2a',
        'sleep_2b',
        'sleep_3a',
        'sleep_3b',
        'sleep_4a',
        'sleep_4b'
    ]] = df_actl_clean[[
        'commute_1a',
        'commute_c1',
        'commute_1b',
        'commute_c2',
        'commute_2a',
        'commute_c3',
        'commute_2b',
        'commute_c4',
        'commute_3a',
        'commute_c5',
        'commute_3b',
        'commute_c6',
        'commute_4a',
        'commute_4b',

        'sleep_1a',
        'sleep_1b',
        'sleep_2a',
        'sleep_2b',
        'sleep_3a',
        'sleep_3b',
        'sleep_4a',
        'sleep_4b'
    ]].applymap(take_mean_between_dash)

    location_living_list = [
        'location_c1',
        'living_c1',
        'location_c2',
    #     'living_c2', # living_c2 is entirely null
        'location_c3',
        'living_c3',
        'location_c4',
        'living_c4',
        'location_c5',
        'living_c5',
        'location_c6',
        'living_c6'
    ]

    for i in location_living_list:
        df_actl_clean[i] = df_actl_clean[i].apply(standardize_coop_locations)
        df_temp = format_location_columns(df_actl_clean, i)
        df_actl_clean = pd.concat([df_actl_clean, df_temp], axis = 1, join = "inner")

    df_actl_clean.to_csv(output_standard_path, index = False, encoding = 'utf-8')

    df_gpa = df_actl_clean[['uid','gpa_1a','gpa_1b','gpa_2a','gpa_2b','gpa_3a','gpa_3b','gpa_4a','gpa_4b']]
    df_lectures = df_actl_clean[['uid','lectures_1a','lectures_1b','lectures_2a','lectures_2b','lectures_3a','lectures_3b','lectures_4a','lectures_4b']]
    df_living = df_actl_clean[['uid','living_1a','living_c1','living_1b','living_c2','living_2a','living_c3','living_2b','living_c4','living_3a','living_c5','living_3b','living_c6','living_4a','living_4b']]
    df_commute = df_actl_clean[['uid','commute_1a','commute_c1','commute_1b','commute_c2','commute_2a','commute_c3','commute_2b','commute_c4','commute_3a','commute_c5','commute_3b','commute_c6','commute_4a','commute_4b']]
    df_sleep = df_actl_clean[['uid','sleep_1a','sleep_1b','sleep_2a','sleep_2b','sleep_3a','sleep_3b','sleep_4a','sleep_4b']]
    df_schoolwork = df_actl_clean[['uid','schoolwork_1a','schoolwork_1b','schoolwork_2a','schoolwork_2b','schoolwork_3a','schoolwork_3b','schoolwork_4a','fydp_4a','schoolwork_4b','fydp_4b',]]
    df_stress = df_actl_clean[['uid','stress_1a','stress_1b','stress_2a','stress_2b','stress_3a','stress_3b','stress_4a','stress_4b']]
    df_mental_health = df_actl_clean[['uid','mental_health_1a','mental_health_c1','mental_health_1b','mental_health_c2','mental_health_2a','mental_health_c3','mental_health_2b','mental_health_c4','mental_health_3a','mental_health_c5','mental_health_3b','mental_health_c6','mental_health_4a','mental_health_4b']]
    df_apps = df_actl_clean[['uid','apps_1a','apps_1b','apps_2a','apps_2b','apps_3a','apps_3b']]
    df_interviews = df_actl_clean[['uid','interviews_1a','interviews_1b','interviews_2a','interviews_2b','interviews_3a','interviews_3b']]
    df_ranked = df_actl_clean[['uid','ranked_1a','ranked_1b','ranked_2a','ranked_2b','ranked_3a','ranked_3b']]
    df_offers = df_actl_clean[['uid','offers_1a','offers_1b','offers_2a','offers_2b','offers_3a','offers_3b']]
    df_rent = df_actl_clean[['uid','rent_1a','rent_c1','rent_1b','rent_c2','rent_2a','rent_c3','rent_2b','rent_c4','rent_3a','rent_c5','rent_3b','rent_c6','rent_4a','rent_4b']]
    df_employed = df_actl_clean[['uid','employed_c1','employed_c2','employed_c3','employed_c4','employed_c5','employed_c6']]
    df_job_title = df_actl_clean[['uid','job_title_c1','job_title_c2','job_title_c3','job_title_c4','job_title_c5','job_title_c6']]
    df_coop_cat = df_actl_clean[['uid','coop_cat_c1','coop_cat_c2','coop_cat_c3','coop_cat_c4','coop_cat_c5','coop_cat_c6']]
    df_location = df_actl_clean[['uid','location_c1','location_c2','location_c3','location_c4','location_c5','location_c6']]
    df_remote = df_actl_clean[['uid','remote_c1','remote_c2','remote_c3','remote_c4','remote_c5','remote_c6']]
    df_company_size = df_actl_clean[['uid','company_size_c1','company_size_c2','company_size_c3','company_size_c4','company_size_c5','company_size_c6']]
    df_industry = df_actl_clean[['uid','industry_c1','industry_c2','industry_c3','industry_c4','industry_c5','industry_c6']]
    df_pay = df_actl_clean[['uid','pay_c1','pay_c2','pay_c3','pay_c4','pay_c5','pay_c6']]
    df_find_job = df_actl_clean[['uid','find_job_c1','find_job_c2','find_job_c3','find_job_c4','find_job_c5','find_job_c6']]
    df_ww_rating = df_actl_clean[['uid','ww_rating_c1','ww_rating_c2','ww_rating_c3','ww_rating_c4','ww_rating_c5','ww_rating_c6']]
    df_enjoy = df_actl_clean[['uid','enjoy_c1','enjoy_c2','enjoy_c3','enjoy_c4','enjoy_c5','enjoy_c6']]
    df_relevance = df_actl_clean[['uid','relevance_c1','relevance_c2','relevance_c3','relevance_c4','relevance_c5','relevance_c6']]
    df_1a = df_actl_clean[['uid','easiness_101','easiness_101L','easiness_111','easiness_113','easiness_121','easiness_161','easiness_181','usefulness_101','usefulness_101L','usefulness_111','usefulness_113','usefulness_121','usefulness_161','usefulness_181','gpa_1a','lectures_1a','living_1a','commute_1a','sleep_1a','schoolwork_1a','stress_1a','mental_health_1a','apps_1a','interviews_1a','ranked_1a','offers_1a','rent_1a']]
    df_c1 = df_actl_clean[['uid','employed_c1','job_title_c1','coop_cat_c1','location_c1','remote_c1','living_c1','company_size_c1','industry_c1','pay_c1','find_job_c1','ww_rating_c1','commute_c1','enjoy_c1','relevance_c1','mental_health_c1','rent_c1']]
    df_1b = df_actl_clean[['uid','easiness_112','easiness_114','easiness_162','easiness_182','easiness_192','easiness_192L','usefulness_112','usefulness_114','usefulness_162','usefulness_182','usefulness_192','usefulness_192L','gpa_1b','lectures_1b','living_1b','commute_1b','sleep_1b','schoolwork_1b','stress_1b','mental_health_1b','apps_1b','interviews_1b','ranked_1b','offers_1b','rent_1b']]
    df_c2 = df_actl_clean[['uid','employed_c2','job_title_c2','coop_cat_c2','location_c2','remote_c2','living_c2','company_size_c2','industry_c2','pay_c2','find_job_c2','ww_rating_c2','commute_c2','enjoy_c2','relevance_c2','mental_health_c2','rent_c2']]
    df_2a = df_actl_clean[['uid','easiness_211','easiness_223','easiness_261','easiness_283','easiness_285','usefulness_211','usefulness_223','usefulness_261','usefulness_283','usefulness_285','gpa_2a','lectures_2a','living_2a','commute_2a','sleep_2a','schoolwork_2a','stress_2a','mental_health_2a','apps_2a','interviews_2a','ranked_2a','offers_2a','rent_2a']]
    df_c3 = df_actl_clean[['uid','employed_c3','job_title_c3','coop_cat_c3','location_c3','remote_c3','living_c3','company_size_c3','industry_c3','pay_c3','find_job_c3','ww_rating_c3','commute_c3','enjoy_c3','relevance_c3','mental_health_c3','rent_c3']]
    df_2b = df_actl_clean[['uid','easiness_212','easiness_252','easiness_262','easiness_286','easiness_292','easiness_292L','usefulness_212','usefulness_252','usefulness_262','usefulness_286','usefulness_292','usefulness_292L','gpa_2b','lectures_2b','living_2b','commute_2b','sleep_2b','schoolwork_2b','stress_2b','mental_health_2b','apps_2b','interviews_2b','ranked_2b','offers_2b','rent_2b']]
    df_c4 = df_actl_clean[['uid','employed_c4','job_title_c4','coop_cat_c4','location_c4','remote_c4','living_c4','company_size_c4','industry_c4','pay_c4','find_job_c4','ww_rating_c4','commute_c4','enjoy_c4','relevance_c4','mental_health_c4','rent_c4']]
    df_3a = df_actl_clean[['uid','easiness_311','easiness_351','easiness_361','easiness_381','easiness_383','usefulness_311','usefulness_351','usefulness_361','usefulness_381','usefulness_383','gpa_3a','lectures_3a','taste_ink','living_3a','commute_3a','sleep_3a','schoolwork_3a','stress_3a','mental_health_3a','apps_3a','interviews_3a','ranked_3a','offers_3a','rent_3a']]
    df_c5 = df_actl_clean[['uid','employed_c5','job_title_c5','coop_cat_c5','location_c5','remote_c5','living_c5','company_size_c5','industry_c5','pay_c5','find_job_c5','ww_rating_c5','commute_c5','enjoy_c5','relevance_c5','mental_health_c5','rent_c5']]
    df_3b = df_actl_clean[['uid','easiness_312','easiness_352','easiness_352L','easiness_362','usefulness_312','usefulness_352','usefulness_352L','usefulness_362','gpa_3b','lectures_3b','birkett_3b','living_3b','commute_3b','sleep_3b','schoolwork_3b','stress_3b','mental_health_3b','apps_3b','interviews_3b','ranked_3b','offers_3b','rent_3b']]
    df_c6 = df_actl_clean[['uid','employed_c6','job_title_c6','coop_cat_c6','location_c6','remote_c6','living_c6','company_size_c6','industry_c6','pay_c6','find_job_c6','ww_rating_c6','commute_c6','enjoy_c6','relevance_c6','mental_health_c6','rent_c6']]
    df_4a = df_actl_clean[['uid','easiness_411','easiness_461','usefulness_411','usefulness_461','gpa_4a','lectures_4a','living_4a','commute_4a','sleep_4a','schoolwork_4a','fydp_4a','stress_4a','mental_health_4a','rent_4a']]
    df_4b = df_actl_clean[['uid','easiness_462','usefulness_462','gpa_4b','lectures_4b','living_4b','commute_4b','sleep_4b','schoolwork_4b','fydp_4b','stress_4b','mental_health_4b','rent_4b']]
    df_easy_useful = df_actl_clean[['uid','easiness_101','easiness_101L','easiness_111','easiness_113','easiness_121','easiness_161','easiness_181','usefulness_101','usefulness_101L','usefulness_111','usefulness_113','usefulness_121','usefulness_161','usefulness_181','easiness_112','easiness_114','easiness_162','easiness_182','easiness_192','easiness_192L','usefulness_112','usefulness_114','usefulness_162','usefulness_182','usefulness_192','usefulness_192L','easiness_211','easiness_223','easiness_261','easiness_283','easiness_285','usefulness_211','usefulness_223','usefulness_261','usefulness_283','usefulness_285','easiness_212','easiness_252','easiness_262','easiness_286','easiness_292','easiness_292L','usefulness_212','usefulness_252','usefulness_262','usefulness_286','usefulness_292','usefulness_292L','easiness_311','easiness_351','easiness_361','easiness_381','easiness_383','usefulness_311','usefulness_351','usefulness_361','usefulness_381','usefulness_383','easiness_312','easiness_352','easiness_352L','easiness_362','usefulness_312','usefulness_352','usefulness_352L','usefulness_362','easiness_411','easiness_461','usefulness_411','usefulness_461','easiness_462','usefulness_462']]



    df_gpa.to_csv(output_split_path + 'gpa.csv', index = False, encoding='utf-8')
    df_lectures.to_csv(output_split_path + 'lectures.csv', index = False, encoding='utf-8')
    df_living.to_csv(output_split_path + 'living.csv', index = False, encoding='utf-8')
    df_commute.to_csv(output_split_path + 'commute.csv', index = False, encoding='utf-8')
    df_sleep.to_csv(output_split_path + 'sleep.csv', index = False, encoding='utf-8')
    df_schoolwork.to_csv(output_split_path + 'schoolwork.csv', index = False, encoding='utf-8')
    df_stress.to_csv(output_split_path + 'stress.csv', index = False, encoding='utf-8')
    df_mental_health.to_csv(output_split_path + 'mental_health.csv', index = False, encoding='utf-8')
    df_apps.to_csv(output_split_path + 'applications_sent.csv', index = False, encoding='utf-8')
    df_interviews.to_csv(output_split_path + 'interviews.csv', index = False, encoding='utf-8')
    df_ranked.to_csv(output_split_path + 'ranked.csv', index = False, encoding='utf-8')
    df_offers.to_csv(output_split_path + 'offers.csv', index = False, encoding='utf-8')
    df_rent.to_csv(output_split_path + 'rent.csv', index = False, encoding='utf-8')
    df_employed.to_csv(output_split_path + 'employed.csv', index = False, encoding='utf-8')
    df_job_title.to_csv(output_split_path + 'job_title.csv', index = False, encoding='utf-8')
    df_coop_cat.to_csv(output_split_path + 'coop_category.csv', index = False, encoding='utf-8')
    df_location.to_csv(output_split_path + 'location.csv', index = False, encoding='utf-8')
    df_remote.to_csv(output_split_path + 'remote.csv', index = False, encoding='utf-8')
    df_company_size.to_csv(output_split_path + 'company_size.csv', index = False, encoding='utf-8')
    df_industry.to_csv(output_split_path + 'industry.csv', index = False, encoding='utf-8')
    df_pay.to_csv(output_split_path + 'pay.csv', index = False, encoding='utf-8')
    df_find_job.to_csv(output_split_path + 'find_job.csv', index = False, encoding='utf-8')
    df_ww_rating.to_csv(output_split_path + 'ww_rating.csv', index = False, encoding='utf-8')
    df_enjoy.to_csv(output_split_path + 'enjoy_coop.csv', index = False, encoding='utf-8')
    df_relevance.to_csv(output_split_path + 'relevance.csv', index = False, encoding='utf-8')
    df_1a.to_csv(output_split_path + '1a.csv', index = False, encoding='utf-8')
    df_c1.to_csv(output_split_path + 'c1.csv', index = False, encoding='utf-8')
    df_1b.to_csv(output_split_path + '1b.csv', index = False, encoding='utf-8')
    df_c2.to_csv(output_split_path + 'c2.csv', index = False, encoding='utf-8')
    df_2a.to_csv(output_split_path + '2a.csv', index = False, encoding='utf-8')
    df_c3.to_csv(output_split_path + 'c3.csv', index = False, encoding='utf-8')
    df_2b.to_csv(output_split_path + '2b.csv', index = False, encoding='utf-8')
    df_c4.to_csv(output_split_path + 'c4.csv', index = False, encoding='utf-8')
    df_3a.to_csv(output_split_path + '3a.csv', index = False, encoding='utf-8')
    df_c5.to_csv(output_split_path + 'c5.csv', index = False, encoding='utf-8')
    df_3b.to_csv(output_split_path + '3b.csv', index = False, encoding='utf-8')
    df_c6.to_csv(output_split_path + 'c6.csv', index = False, encoding='utf-8')
    df_4a.to_csv(output_split_path + '4a.csv', index = False, encoding='utf-8')
    df_4b.to_csv(output_split_path + '4b.csv', index = False, encoding='utf-8')
    df_easy_useful.to_csv(output_split_path + 'easy_useful_courses.csv', index = False, encoding='utf-8')

if __name__ == "__main__":
    main()