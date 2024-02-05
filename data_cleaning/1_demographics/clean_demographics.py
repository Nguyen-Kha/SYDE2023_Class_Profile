import pandas as pd
import numpy as np
import math

###### DEV VARIABLES ########
input_csv_path = 'C:\\Users\\Kha\\Documents\\Programming\\SYDE2023_Class_Profile\\csv\\raw\\1_DHP.csv'
output_rename_column_path = 'C:\\Users\\Kha\\Documents\\Programming\\SYDE2023_Class_Profile\\csv\\renamed_columns\\1_DHP_renamed.csv'
output_pii_path = 'C:\\Users\\Kha\\Documents\\Programming\\SYDE2023_Class_Profile\\csv\\final\\1_DHP_PII_final.csv'
output_standard_path = 'C:\\Users\\Kha\\Documents\\Programming\\SYDE2023_Class_Profile\\csv\\final\\1_DHP_final.csv'
output_split_path = 'C:\\Users\\Kha\\Documents\\Programming\\SYDE2023_Class_Profile\\csv\\final\\split\\'

##### GLOBAL (For university and parsing to work) #######
individual_other_unis = []
individual_other_programs = []

###### MAPPINGS #########

alt_choice_dict = {
    'Architectural Engineering': 'Architectural Engineering',
    'Architecture Engineering': 'Architectural Engineering',
    'Biomedical Engineering': 'Biomedical Engineering',
    'Chemical Engineering' : 'Chemical Engineering',
    'Civil' : 'Civil Engineering',
    'Civil Engineering' : 'Civil Engineering',
    'Computer' : 'Computer Engineering',
    'Computer Engineering' : 'Computer Engineering',
    'Computer engineering' : 'Computer Engineering',
    'Electrical Engineering' : 'Electrical Engineering',
    'Environmental': 'Environmental Engineering',
    'Management' : 'Management Engineering',
    'Management Engineering' : 'Management Engineering',
    'Mechanical' : 'Mechanical Engineering',
    'Mechanical Engineering' : 'Mechanical Engineering',
    'Mechatronics' : 'Mechatronics Engineering',
    'Mechatronics Engineering' : 'Mechatronics Engineering',
    'Mgmt' : 'Management Engineering',
    'Nano' : 'Nanotechnology Engineering',
    'Nanotechnology Engineering' : 'Nanotechnology Engineering'
}

standardized_universities_dict = {
    "University of Alberta" : "University of Alberta",
    "University of Ottawa" : "University of Ottawa",
    "OCAD University" : "OCAD University",
    "Carleton University" : "Carleton University",
    "Northwestern University" : "Northwestern University",
    "University of Victoria" : "University of Victoria",
    "Toronto Metropolitan University" : "Toronto Metropolitan University",
    "Ryerson" : "Toronto Metropolitan University",
    "Ryerson University" : "Toronto Metropolitan University",
    "TMU" : "Toronto Metropolitan University",
    "University of Toronto" : "University of Toronto",
    "University of Toronto (St. George)" : "University of Toronto",
    "UTM" : "University of Toronto",
    "UTSC" : "University of Toronto",
    "UofT" : "University of Toronto",
    "toronto" : "University of Toronto",
    "U of T" : "University of Toronto",
    "Univeristy of Toronto" : "University of Toronto",
    "uoft" : "University of Toronto",
    "York" : "York University",
    "McMaster University" : "McMaster University",
    "McMaster's" : "McMaster University",
    "mcmaster" : "McMaster University",
    "McMaster" : "McMaster University",
    "Mcmaster" : "McMaster University",
    "Mcmaster University" : "McMaster University",
    "Queen's University" : "Queen's University",
    "Queens University" : "Queen's University",
    "Queens" : "Queen's University",
    "Queen's" : "Queen's University",
    "queens" : "Queen's University",
    "Guelph" : "University of Guelph",
    "guelph" : "University of Guelph",
    "University of Western Ontario" : "University of Western Ontario",
    "western" : "University of Western Ontario",
    "University  of Western Ontario" : "University of Western Ontario",
    "Western University" : "University of Western Ontario",
    "western university" : "University of Western Ontario",
    "Western" : "University of Western Ontario",
    "University of Waterloo & Laurier" : "UW / WLU",
    "McGill University" : "McGill University",
    "McGill" : "McGill University",
    "University of Waterloo" : "University of Waterloo",
    "Waterloo" : "University of Waterloo",
    "university of waterloo" : "University of Waterloo",
    "University of British Columbia" : "University of British Columbia",
    "UBC" : "University of British Columbia",
    "Laurier" : "Wilfrid Laurier University"
}

standardized_program_dict = {
    "CS & BBA" : "CS / BBA",
    "Computer Science and Business" : "CS / BBA",
    "Computer Science / BBA" : "CS / BBA",
    "Double Degree CS and BBA" : "CS / BBA",
    "Computer Science/BBA" : "CS / BBA",
    "Business and Computer Science" : "CS / BBA",
    "Integrated Biomedical Engineering & Health Sciences" : "Integrated Biomedical Engineering & Health Sciences",
    "Integrated Health Sciences & Engineering" : "Integrated Biomedical Engineering & Health Sciences",
    "ibehs" : "Integrated Biomedical Engineering & Health Sciences",
    "Rotman Commerce" : "Commerce",
    "commerce" : "Commerce",
    "Rotman" : "Commerce",
    "Commerce" : "Commerce",
    "Track One" : "Track One Engineering",
    "Track 1 Engineering" : "Track One Engineering",
    "Engineering TrackOne" : "Track One Engineering",
    "Track One Engineering" : "Track One Engineering",
    "TrackOne" : "Track One Engineering",
    "Track one" : "Track One Engineering",
    "Engineering (Track One)" : "Track One Engineering",
    "Mathematics" : "Mathematics",
    "Math" : "Mathematics",
    "Maths" : "Mathematics",
    "Engineering Science" : "Engineering Science",
    "Engineering Sciences" : "Engineering Science",
    "engineering science" : "Engineering Science",
    "General Engineering" : "General Engineering",
    "Engineering (General)" : "General Engineering",
    "engineering" : "General Engineering",
    "Engineering" : "General Engineering",
    "Engineering I" : "General Engineering",
    "Undeclared Engineering" : "General Engineering",
    "Undeclared engineering" : "General Engineering",
    "Computing and Financial Management" : "Computing and Financial Management",
    "CFM" : "Computing and Financial Management",
    "Health Science" : "Health Sciences",
    "health sci" : "Health Sciences",
    "Honours Health Sciences I" : "Health Sciences",
    "Computer Science" : "Computer Science",
    "computer science" : "Computer Science",
    "Integrated Science" : "Integrated Science",
    "isci" : "Integrated Science",
    "Industrial Engineering" : "Industrial Engineering",
    "Industrial Engineeing" : "Industrial Engineering",
    "Biomedical Engineering" : "Biomedical Engineering",
    "biomed engineering" : "Biomedical Engineering",
    "Computer Engineering" : "Computer Engineering",
    "computer engineering" : "Computer Engineering",
    "Electrical Engineering" : "Electrical Engineering",
    "Electrical engineering" : "Electrical Engineering",
    "Engineering + Ivey AEO Dual Degree" : "Ivey & Engineering",
    "Ivey & Engineering" : "Ivey & Engineering",
    "Aerospace Engineering" : "Aerospace Engineering",
    "Applied Math" : "Applied Mathematics",
    "Biomedical and Mechanical Engineering" : "Biomedical and Mechanical Engineering",
    "Biomedical Mechanical Engineering & Computing Technology" : "Biomedical Mechanical Engineering & Computing Technology",
    "Biomedical Science" : "Biomedical Sciences",
    "Biotechnology/Chartered Professional Accountancy" : "Biotechnology / Chartered Professional Accountancy",
    "Chemical Engineering" : "Chemical Engineering",
    "Chemistry" : "Chemistry",
    "Civil Engineering" : "Civil Engineering",
    "Environmental Engineering" : "Environmental Engineering",
    "Financial Analysis and Risk Management" : "Financial Analysis and Risk Management",
    "Graphics Communication Management" : "Graphics Communication Management",
    "Ivey" : "Ivey",
    "Ivey/Med sci" : "Ivey & Medical Sciences",
    "Industrial Design" : "Industrial Design",
    "Integrated Engineering" : "Integrated Engineering",
    "kinesiology" : "Kinesiology",
    "Knowledge Integration" : "Knowledge Integration",
    "Life Science" : "Life Sciences",
    "Management Coop" : "Management",
    "Manufacturing and Design Engineering" : "Manufacturing and Design Engineering",
    "Math and Physics" : "Math and Physics",
    "Mathematical Physics" : "Mathematical Physics",
    "Mechanical Engineering" : "Mechanical Engineering",
    "Mechatronics Engineering" : "Mechatronics Engineering",
    "Medical Sciences" : "Medical Sciences",
    "Philosophy" : "Philosophy",
    "Physiology Honors" : "Physiology",
    "Science and Business" : "Science and Business",
    "Science" : "Science",
    "Software Engineering" : "Software Engineering"
}

######## FUNCTIONS #############

def rename_column_headers(df):
    df = df.rename(columns = {
        "What is your unique ID" : "uid",
        "When did you join the cohort" : "join_year",
        "How many years did it take you to complete the degree" : "years_complete_degree",
        "If you transferred into SYDE, which program did you transfer in from" : "transferred_program",
        "What is your race/ethnic origins? Select all that apply." : "race",
        "Which of the following describes your Indigenous background? Do not answer this question if you do not identify as an Indigenous person." : "indigenous",
        "In which year were you born" : "birth_year",
        "What is your gender identity" : "gender",
        "What is your sexual identity" : "sex",
        "In which city and country were you born in" : "birth_location",
        "In which city and country do you consider to be your hometown" : "hometown_location",
        "Which of the following best describes your political views" : "politics",
        "Which of the following best describes your PARENTS' political views" : "politics_parents",
        "If the federal election happened today, you would vote ___" : "election",
        "Which of the following most closely describes your religious school of thought?" : "religion",
        "Which of the following most closely describes your FAMILY'S religious school of thought?" : "religion_parents",
        "Which languages do you speak?" : "number_languages",
        "Which languages are spoken at home?" : "languages",
        "What is your citizenship status" : "citizenship",
        "What is your generational immigration status?" : "gen_immigration",
        "What was your family's annual household income in 2018" : "household_income",
        "What is the highest level of education of any of your parents / guardians" : "edu_parents",
        "Do any of your parents/guardians have a STEM education?" : "stem_edu_parents",
        "Do any of your parents/guardians work in engineering?" : "eng_parents",
        "How many siblings do you have" : "siblings",
        "Where did you go to high school?" : "hs_location",
        "If you selected Ontario, outside of KW and GTA, please specify" : "hs_ont",
        "If you selected Canada, outside of Ontario, please specify" : "hs_canada",
        "Select the following type of high school that best represents the high school you attended in your final year" : "hs_type",
        "What was your admission average" : "admission_average",
        "Were you enrolled in any special high school programs/curriculum?" : "hs_spec_programs",
        "What kind of extracurricular activities were you involved with in high school?" : "hs_ec",
        "How many hours a week did you spend on extracurricular activities in high school?" : "hs_ec_time",
        "Did you participate in any of the following while in high school" : "hs_spec_ec",
        "How did you hear about SYDE" : "hear_about_syde",
        "Which other universities and programs did you apply to?" : "uni_programs_applied",
        "Was SYDE your first choice when choosing engineering at UW?" : "syde_first_choice",
        "If not, what was your first choice for engineering at UW?" : "uw_first_choice",
        "If SYDE was your first choice when choosing engineering at UW, what was your backup / alternate choice?" : "syde_backup_choice",
        "For which of the following reasons did you choose SYDE at UW" : "why_syde",
        "What type of career did you see yourself working as prior to entering SYDE?" : "hs_career",
        "Did you take a gap year after high school" : "gap_year",
        "Which of these 1A / 1B personas do you identify with the most in first year?" : "persona_1",
        "Which of these 2A - 3B personas do you identify with the most in second year?" : "persona_2",
        "Which of these 2A - 3B personas do you identify with the most in third year?" : "persona_3",
        "Which of these 4A / 4B personas do you identify with the most in fourth year?" : "persona_4"
    })

    return df

def clean_alt_choice(choice):
    try:
        return alt_choice_dict[choice.strip()]
    except:
        return np.nan

def clean_uni_programs(uni_program_string):
    if(type(uni_program_string) == float):
        if(math.isnan(uni_program_string)):
            individual_other_unis.append(np.nan)
            individual_other_programs.append(np.nan)
            return np.nan
    
    try:
        uni_program_string = uni_program_string.replace("Co-op", "")
        uni_program_string = uni_program_string.replace("Track-One", "Track One")
        
        cleaned_uni_program_string = ""
        individual_other_uni_string = ""
        individual_other_program_string = ""
        
        individual_uni_programs = uni_program_string.split(",")
        for i in individual_uni_programs:
            temp = i.split("-")
            
            cleaned_uni = standardized_universities_dict[temp[0].strip()]
            if (individual_other_uni_string == ""):
                individual_other_uni_string = individual_other_uni_string + cleaned_uni
            else:
                individual_other_uni_string = individual_other_uni_string + ", " + cleaned_uni
            
            cleaned_program = standardized_program_dict[temp[1].strip()]
            if (individual_other_program_string == ""):
                individual_other_program_string = individual_other_program_string + cleaned_program
            else:
                individual_other_program_string = individual_other_program_string + ", "  + cleaned_program
            
            if (cleaned_uni_program_string == ""):
                cleaned_uni_program_string = cleaned_uni_program_string + cleaned_uni + " - " + cleaned_program
            else:
                cleaned_uni_program_string = cleaned_uni_program_string + ", " + cleaned_uni + " - " + cleaned_program
            
        individual_other_unis.append(individual_other_uni_string)
        individual_other_programs.append(individual_other_program_string)

        return cleaned_uni_program_string
    except:
        individual_other_unis.append(np.nan)
        individual_other_programs.append(np.nan)
        return np.nan

def clean_gen_immigration(answer):
    if(type(answer) == float):
        if(math.isnan(answer)):
            return np.nan
        
    if(answer == 'First Generation (You moved to Canada recently)'):
        answer = 'First Generation'
    elif(answer == '1.5 Generation (You moved to Canada at a young age)'):
        answer = '1.5 Generation'
    elif(answer == 'Second Generation (Your parents moved to Canada and you were born in Canada)'):
        answer = 'Second Generation'
    elif(answer == 'Third Generation or more'):
        answer = 'Third Generation or more'
    else:
        answer = np.nan
    
    return answer
    

def main():
    global individual_other_unis
    global individual_other_programs
    
    # Load CSV
    df = pd.read_csv(input_csv_path)
    df = df.drop(columns = ['Timestamp', 'Questions Comments Concerns Suggestions Feedback for this section'])

    # Rename column headers
    df_demographics_clean = rename_column_headers(df)
    df_demographics_clean.to_csv(output_rename_column_path, index=False, encoding='utf-8')

    # Clean alternate choice if you didn't get SYDE
    df_demographics_clean['syde_backup_choice'] = df_demographics_clean['syde_backup_choice'].apply(clean_alt_choice)

    # Clean other unis and programs applied to
    df_demographics_clean['uni_programs_applied'] = df_demographics_clean['uni_programs_applied'].apply(clean_uni_programs)
    df_uni_programs = pd.DataFrame({
        'other_unis_applied': individual_other_unis,
        'other_programs_applied': individual_other_programs
    })
    df_demographics_clean = pd.concat([df_demographics_clean, df_uni_programs], axis = 1, join = 'inner')

    df_demographics_clean['gen_immigration'] = df_demographics_clean['gen_immigration'].apply(clean_gen_immigration)

    df_pii = df_demographics_clean[['join_year', 'years_complete_degree', 'transferred_program', 'race', 'indigenous', 'birth_year', 'gender', 'sex', 'birth_location', 'hometown_location', 'politics', 'politics_parents', 'election', 'religion', 'religion_parents', 'number_languages', 'languages', 'citizenship', 'hs_location', 'hs_ont', 'hs_canada']]
    df_pii = df_pii.sample(frac = 1)
    df_no_pii = df_demographics_clean.drop(columns = ['join_year', 'years_complete_degree', 'transferred_program', 'race', 'indigenous', 'birth_year', 'gender', 'sex', 'birth_location', 'hometown_location', 'politics', 'politics_parents', 'election', 'religion', 'religion_parents', 'number_languages', 'languages', 'citizenship', 'hs_location', 'hs_ont', 'hs_canada'])

    # Export CSVs
    df_no_pii.to_csv(output_standard_path, index=False, encoding='utf-8')
    df_pii.to_csv(output_pii_path, index=False, encoding='utf-8')


    df_household = df_demographics_clean[[
        'uid', 
        'gen_immigration',
        'household_income',
        'edu_parents',
        'stem_edu_parents',
        'eng_parents',
        'siblings'
    ]]

    df_high_school = df_demographics_clean[[
        'uid',
        'hs_type',
        'admission_average',
        'hs_spec_programs',
        'hs_ec',
        'hs_ec_time',
        'hs_spec_ec',
        'hs_career',
        'gap_year'
    ]]

    df_before_syde = df_demographics_clean[[
        'uid',
        'hear_about_syde',
        'syde_first_choice',
        'uw_first_choice',
        'syde_backup_choice',
        'why_syde',
        'uni_programs_applied',
        'other_unis_applied',
        'other_programs_applied'
    ]]

    df_syde_personas = df_demographics_clean[[
        'uid',
        'persona_1',
        'persona_2',
        'persona_3',
        'persona_4'
    ]]

    df_household.to_csv(output_split_path + 'household.csv', index = False, encoding='utf-8')
    df_high_school.to_csv(output_split_path + 'high_school.csv', index = False, encoding='utf-8')
    df_before_syde.to_csv(output_split_path + 'before_syde.csv', index = False, encoding='utf-8')
    df_syde_personas.to_csv(output_split_path + 'syde_personas.csv', index = False, encoding='utf-8')

if __name__ == "__main__":
    main()