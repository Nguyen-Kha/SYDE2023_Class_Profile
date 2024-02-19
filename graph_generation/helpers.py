from collections import Counter
import pandas as pd

def splice_cells_with_commas(df, column_name): # TODO: TEST
    """
    RETURNS: ARRAY of values to be counted with COUNTER
    # TODO: Do some dictionary work instead
    """
    spliced_array = []
    for item in df[column_name]:
        if(type(item) != float):
            potential_list = item.split(', ')
            for single in potential_list:
                spliced_array.append(single)
    
    return spliced_array

def transform_stacked_bar_df(
    df_working,
    column_name,
    labels = [],
    display_as_percentage = False,
    convert_to_string = False
):
    """
    Transforms pandas Series to 1 x n DataFrame of occurences of each value
    Creates df columns:
     column_name  | Category 1 | Category 2 |    ...   | Category n |   Total
    <column_name> |     num    |    num     |          |    num     |    num
    """
    df = df_working.copy()
    if(df[column_name].isnull().values.any()):
        df[column_name] = df[column_name].dropna(axis=0)

    if(convert_to_string):
        df[column_name] = df[column_name].astype(str)
        
    count = Counter()
    
    column_values = splice_cells_with_commas(df, column_name)
    for i in column_values:
        count[i] += 1
    
    number_of_answers = sum(count.values())
    
    dict_df = {'column_name': [column_name]}
    working_dict = {}
    if(labels):
        for i in labels:
            if(i in count):
                working_dict[i] = [count[i]]
            else:
                working_dict[i] = [0]
                
        working_dict = display_as_percentage_transform_stacked_bar_df(display_as_percentage, working_dict, number_of_answers)
    else:
        title_temp = list(count.keys())
        values_temp = list(count.values())
        
        for i in range(0, len(title_temp)):
            working_dict[title_temp[i]] = [values_temp[i]]
            
        working_dict= dict(sorted(working_dict.items(), key=lambda item: item[1], reverse=True))
        working_dict = display_as_percentage_transform_stacked_bar_df(display_as_percentage, working_dict, number_of_answers)
        
    dict_df = {**dict_df, **working_dict} # merge the two dictionaries
    df_temp = pd.DataFrame(dict_df)
    
    return df_temp

def display_as_percentage_transform_stacked_bar_df(display_as_percentage, working_dict, number_of_answers):
    if(display_as_percentage):
        for k, v in working_dict.items():
            working_dict[k] = [v[0] / number_of_answers * 100] # take the key value pair of working_dict with Counter values, replace it with percentage as 'category': [count] for the dataframe
        working_dict['Total'] = [100]
    else:
        working_dict['Total'] = [number_of_answers]
    return working_dict
