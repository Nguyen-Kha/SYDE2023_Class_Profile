from collections import Counter
import pandas as pd
import math

def splice_cells_with_commas(df, column_name): # TODO: TEST
    """
    If a column value has commas in it, turns it into an array of strings to be parsed
    +---------------------+---------------------------+
    |     column_name     | spliced_cells_with_commas |
    +---------------------+---------------------------+
    | text                | [text]                    |
    | text1, text2, text3 | [text1, text2, text3]     |
    | text                | [text]                    |
    +---------------------+---------------------------+
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
    This is used to construct the stacked bar graph, where the categories themselves are the number of occurences of that in the column/group
    Once all of these are completed, it will be UNIONed together to make the df to make the stacked bar
    Transforms pandas Series to 1 x n DataFrame of occurences of each value
    Turns:
    +------------+
    |  column_A  |
    +------------+
    | category 1 |
    | category 2 |
    | category 4 |
    | category 1 |
    | category 3 |
    | category 4 |
    | category 1 |
    +------------+
    into 
    +-------------+------------+------------+------------+------------+
    | column_name | category 1 | category 2 | category 3 | category 4 |
    +-------------+------------+------------+------------+------------+
    | column_A    |          3 |          1 |          1 |          2 |
    +-------------+------------+------------+------------+------------+
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

def turn_dates_into_actual_values(dates):
    """
    Some of the values displayed as dates are meant to represent a range. This happens if the data is from Google Sheets or Excel
    To use this, do the following on your dataframe before generating a graph:
    df['column_name'] = df['column_name'].apply(turn_dates_into_actual_values)
    """
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
    
def transform_df_for_boxplot(
    df_working,                 # Pandas Dataframe, format shown below
    column_name: str,           # column to plot on box plot
    comparison_column = None,   # OPTIONAL: to splice the boxplot into groups to compare
    comparison_labels = [],     # OPTIONAL: order in which the comparison values are arranged
    drop_values = {}            # {str(column_name): number, ...} values to remove from the boxplot (aka outliers)
):
    """
    For both single column and multi column dataframes
    Turns this DataFrame
    +---------------+------------------------------+
    | column_name_a | comparison_column (optional) |
    +---------------+------------------------------+
    | number_a1     | Class A                      |
    | number_a2     | Class B                      |
    | number_a3     | Class B                      |
    +---------------+------------------------------+
    into
    +---------------+----------------+-----------------------+
    | boxplot_title | boxplot_values | comparison (optional) |
    +---------------+----------------+-----------------------+
    | column_name_a | number_a1      | Class A               |
    | column_name_a | number_a2      | Class B               |
    | column_name_a | number_a3      | Class B               |
    +---------------+----------------+-----------------------+
    """
    df = df_working.copy()
            
    if(comparison_column):
        df = df[[column_name, comparison_column]]
        df = df.rename(columns = {comparison_column: 'comparison_column'})
    else:
        df = df[[column_name]]
        
    if(drop_values):
        for key, value in drop_values.items():
            if(key == column_name):
                df = df.drop(df[df[key] == value].index)
    
    if(df.isnull().values.any()):
        df = df.dropna(axis = 0)
    
    df['column_name'] = column_name
    df = df.rename(columns = {column_name: 'boxplot_value'})
    
    if(comparison_labels and comparison_column):
        df['comparison_column'] = pd.Categorical(df['comparison_column'], comparison_labels)
        df = df.sort_values('comparison_column')

    return df

def transform_df_for_line_unnamed_rows(
    df,
    column_name_list,
    row_object_name = 'row_object'
):
    """
    Transforms the following dataframe
    +--------------+-----+--------------+
    | row_object_a | ... | row_object_n |
    +--------------+-----+--------------+
    | number a1    |     | number n1    |
    | number a2    |     | number n2    |
    | number a3    |     | number n3    |
    +--------------+-----+--------------+
    into 
    +--------------+------------+-----------+
    |    index     | row_object |   value   |
    +--------------+------------+-----------+
    | row_object_a |          0 | number a1 |
    | row_object_n |          0 | number n1 |
    | row_object_a |          1 | number a2 |
    | row_object_n |          1 | number n2 |
    | row_object_a |          2 | number a3 |
    | row_object_n |          2 | number n3 |
    +--------------+------------+-----------+
    which makes as many lines as the number of values in a row_object_n column
    
    This assumes the data has already been cleaned, and null values are already accounted for
    Use this if the line graph does not need a legend, where there is no particular meaning to each row, or each row can be unlabelled. 
    """
    df = df.transpose().reset_index().drop(columns = 'index')
    df['index'] = column_name_list
    df = pd.melt(df, id_vars = ['index'], var_name = row_object_name)
    return df