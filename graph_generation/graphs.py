from collections import Counter
import math
from textwrap import wrap

import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np
import pandas as pd
import seaborn as sns

import helpers

def create_bar(
    df,                                 # pandas Series or pandas DataFrame. (Non aggregate cleaned values)
    column_name: str,                   # name of column in dataframe
    title_label: str,                   # x axis label (vertical)
    values_label : str,                 # y axis label (vertical)
    title: str,                         # title of graph
    vertical: bool,                     # True for vertical bars, False for horizontal bars

    file_name = None,                   # name of file to save as 
    values_increment: float = None,     # default 1/10 of the max value in the y axis / count of dataframe
    values_max: float = None,           # the max value in the dataframe
    splice_required: bool = False,      # Use True if the values in the cells have commas that need to be split
    labels: list = [],                  # list of strings, order in which the x axis / title labels should be arranged
    colours = [],                       # list of strings of hexcodes ['#0000FF', '#eb884a'] for bar colours
    display_as_percentage = False,      # display the y axis as a percentage rather than the count occurence
    display_legend = False,             # show the legend if necessary
    title_label_rotation_angle = 0,     # the angle where the x axis labels is skewed. Use 45 if title labels are too long
    drop_values = [],                   # list of strings. Use when you need to quickly drop title values from a dataframe to hide it from the bar graph
    convert_to_string = False,          # used if your DataFrame column are not strings
    max_label_length = 20,              # max number of characters to use for a label before wrapping it
    num_decimals = 0,                   # number of decimal places to display; only used if display_as_percentage=True
):    
    # Set default colour palette
    if (not colours):
        colours = sns.color_palette('muted')
    
    # drop nulls (technically you should have already dropped them)
    if(df[column_name].isnull().values.any()):
        df = df.dropna(subset = [column_name], axis=0)
        # df = df.dropna(axis=0)
    
    if(convert_to_string):
        df[column_name] = df[column_name].astype(str)
        
    ######################
    ## Count the amount of instances of each occurence in the dataset
    count = Counter()
    if(splice_required):
        column_values = helpers.splice_cells_with_commas(df, column_name)
        for i in column_values:
            count[i] += 1
    else:
        for value in df[column_name]:
            count[value] += 1 

    if(drop_values):
        for i in drop_values:
            if(i in count):
                del count[i]
        
     ######################
    ## Put the counted values into a new dataframe
    
    if(labels):
        title_temp = list(count.keys())
        values_temp = list(count.values())
        dictionary = {title_temp[i] : values_temp[i] for i in range(0, len(title_temp))}

        df_temp = pd.DataFrame()
        df_temp['title'] = labels
        df_temp['values'] = 0

        for key, value in dictionary.items():
            df_temp.loc[df_temp.title == key, 'values'] = value
        x = np.arange(len(labels))  # the label locations
    
    else:
        df_temp = pd.DataFrame({'title': list(count.keys()), 'values': list(count.values())})
        df_temp = df_temp.sort_values(by=['values'], ascending = False)
        
        if(not vertical):
            reverse_title_order = df_temp['title'].tolist()
            reverse_title_order.reverse()
            df_temp['title'] = pd.Categorical(df_temp['title'], reverse_title_order)
            df_temp = df_temp.sort_values('title')

        x = df_temp['title'] # the label locations
        if type(x[0]) == str:
            x = [ '\n'.join(wrap(label, max_label_length)) for label in x ]
        
    ######################
    ## Convert amount of people responded into percentages
    if(display_as_percentage):
        number_of_answers = len(df.index)
        df_temp['values'] = df_temp['values'] / number_of_answers * 100
    
    ###################
    ## Set axis interval increments
    
    if(not values_max):
        values_max = max(df_temp['values'])
        
    if(not values_increment):
        values_increment = math.ceil(values_max / 10)

    fig, ax = plt.subplots(figsize = (11,9))
    
    if(vertical):
        ax.bar(
            x = x,
            height = df_temp['values'],
            align = 'center',
            zorder = 3,
            color = colours,
            label = column_name,
            alpha = 0.75,
        )
        ax.set_xlabel(title_label)
        ax.set_ylabel(values_label)
        ax.yaxis.set_ticks(np.arange(0, values_max + values_increment, values_increment))
        if(labels):
            ax.set_xticks(x)
            ax.set_xticklabels(labels)
        if(display_as_percentage):
            ax.yaxis.set_major_formatter(mtick.PercentFormatter(decimals=num_decimals))
        if(title_label_rotation_angle == 0):
            plt.xticks(rotation=title_label_rotation_angle)
        else:
            plt.xticks(rotation=title_label_rotation_angle, ha='right')            
        
    else:
        ax.barh(
            y = x,
            width = df_temp['values'],
            align = 'center',
            zorder = 3,
            color = colours,
            label = column_name,
            alpha = 0.75,
        )
        ax.set_xlabel(values_label)
        ax.set_ylabel(title_label)
        ax.xaxis.set_ticks(np.arange(0, values_max + values_increment, values_increment))
        if(labels):
            ax.set_yticks(x)
            ax.set_yticklabels(labels)
        if(display_as_percentage):
            ax.xaxis.set_major_formatter(mtick.PercentFormatter(decimals=num_decimals))
        if(title_label_rotation_angle == 0):
            plt.yticks(rotation=title_label_rotation_angle)
        else:
            plt.yticks(rotation=title_label_rotation_angle, ha='right')
        
    plt.rcParams['axes.facecolor'] = '#F0F0F0'
    ax.grid(color='w', linestyle='solid', zorder=0)
    if(display_legend):
        plt.legend(title="Legend", facecolor='white')

    plt.title(title)

    if(not file_name):
        file_name = str(column_name)
    plt.savefig('./graphs/' + file_name + '.png', bbox_inches='tight')

    plt.close()

def create_bar_stacked(
    df,                             # pandas DataFrame, non aggregate cleaned columns
    column_name_list: list,         # list of dataframe column names you want to compare and have values stacked
    title_label,                    # title axis labels
    values_label,                   # value axis labels
    title,                          # title of graph
    file_name,                      # name to save the file to

    vertical = False,               # True for vertical bar graph, False for horizontal bar graph
    values_increment = None,        # value to increment y axis by. If display_as_percentage = True, this value is 10
    values_max = None,              # The maximum y axis value of the graph. If display_as_percentage = True, this value is 100
    labels = [],                    # List of strings, specific order to arrange bars by. if passing multiple values in column_name_list, labels will be the same for all of them
    colours = [],                   # list of hex code strings for column_name colours
    display_as_percentage = False,  # Display the y axis values as a percentage instead of a count
    title_label_rotation_angle = 0, # angle of the x axis labels. If overlapping, use 45
    convert_to_string = False,      # convert title labels to string
    legend_title = None             # Name of the legend title
):
    """
    DataFrame format:
    +---------------+----------------+-----+---------------+
    | column_name_A | column_name_B  | ... | column_name_n |
    +---------------+----------------+-----+---------------+
    | val 1         | val 4          |     | val 2         |
    | val 2         | val 2          |     | val 2         |
    | val 3         | val 1          |     | val 3         |
    | val 4         | val 1          |     | val 1         |
    +---------------+----------------+-----+---------------+
    
    The values in all the columns must be a part of the same set. AKA they should all be the same. Ex, ['Yes', 'No']: all columns have these values
    """
    if (not colours):
        colours = sns.color_palette('muted')
    
    list_df = []
    for column_name in column_name_list:
        list_df.append(helpers.transform_stacked_bar_df(df, column_name, labels, display_as_percentage, convert_to_string))
    working_df = pd.concat(list_df) # combine the individual dataframes together via UNION
    working_df = working_df.fillna(0) # if no labels provided, turn all np.nan values for offset calculation
    
    if(not values_max):
        values_max = working_df['Total'].max(0)
    if(not values_increment):
        values_increment = math.ceil(values_max / 10)
    
    if(display_as_percentage):
        values_max = 100
        values_increment = 10
    
    list_df_columns = working_df.columns.tolist()
    list_df_columns.pop(0) # remove column_name from list
    list_df_columns.remove("Total")
    
    offset = pd.Series(0) # this allows for bar stacking
    fig, ax = plt.subplots(figsize = (11, 9))
    if(vertical):
        for i in range (0, len(list_df_columns)):
            ax.bar(
                working_df['column_name'],
                working_df[list_df_columns[i]],
                zorder = 3,
                bottom = offset,
                # color = colours[i]
            )
            offset = offset + working_df[list_df_columns[i]]
            
        ax.set_ylabel(values_label)
        ax.set_xlabel(title_label)
        ax.yaxis.set_ticks(np.arange(0, values_max + values_increment, values_increment))
        if(title_label_rotation_angle != 0):
            plt.xticks(rotation = title_label_rotation_angle, ha = 'right')
    else:
        # Horizontal graphs have ascending top to bottom display. Reverse this to keep it consistent with bar graph
        reverse_column_name = working_df['column_name'].tolist() # You could theoretically sort it by total, but that doesn't keep order
        reverse_column_name.reverse() # Have to make this its own call cause otherwise it will return None
        working_df['column_name'] = pd.Categorical(working_df['column_name'], reverse_column_name)
        working_df = working_df.sort_values('column_name')
        for i in range (0, len(list_df_columns)):
            ax.barh(
                working_df['column_name'],
                working_df[list_df_columns[i]],
                zorder = 3,
                left = offset,
                # color = colours[i]
            )
            offset = offset + working_df[list_df_columns[i]]

        ax.set_xlabel(values_label)
        ax.set_ylabel(title_label)
        ax.xaxis.set_ticks(np.arange(0, values_max + values_increment, values_increment))
        
    if(not legend_title):
        legend_title = 'Legend'
    plt.legend(list_df_columns, title=legend_title, facecolor='white')
    plt.title(title)
    plt.savefig('./graphs/' + str(file_name) + '.png', bbox_inches='tight')
    plt.close()

def create_boxplot(
    df,                                 # pandas input dataframe (see below for format)
    column_name_list: list,             # list of column names to display in boxplot, in order
    title_label: str,                   # title label of graph (x axis label for vertical graph) 
    values_label: str,                  # values label of graph (y axis label for horizontal graph)
    title,                              # title of graph
    file_name,                          # file name to save graph as

    vertical: bool = True,              # orientation of boxplots
    comparison_column: str = None,      # use to compare values within the column_names (ex: split boxplot values by gender)
    comparison_labels = [],             # order of the comparison labels
    values_increment = None,            # values to increment by on the values axis
    values_min = None,                  # smallest value to display on graph
    values_max = None,                  # largest value to display on graph
#     colours = [],                     # list of hex code strings
    convert_to_string = False,          # use if need to convert column_values to string
    drop_values = {}                    # {str(column_name): number, ...} , drop certain values or outliers if necessary
):
    """
    Input Dataframe format: 
    +---------------+-----+---------------+
    | column_name_a | ... | column_name_n |
    +---------------+-----+---------------+
    | number_a1     |     | number_n1     |
    | number_a2     |     | number_n2     |
    | number_a3     |     | number_n3     |
    | number_a4     |     | number_n4     |
    +---------------+-----+---------------+
    """
    if(convert_to_string):
        for i in range(0, len(column_name_list)):
            column_name_list[i] = str(column_name_list[i])
    
    # construct dataframe to be used for boxplot
    if(len(column_name_list) == 1):            
        df_boxplot = helpers.transform_df_for_boxplot(df, column_name_list[0], comparison_column, comparison_labels, drop_values)
    else:
        list_df = []
        for column_name in column_name_list:
            working_df = helpers.transform_df_for_boxplot(df, column_name, comparison_column, comparison_labels, drop_values)
            list_df.append(working_df)
        df_boxplot = pd.concat(list_df)
    df_boxplot = df_boxplot.reset_index().drop(columns='index')
    
    if(values_min == None):
        values_min = min(df_boxplot['boxplot_value'])
    
    if(values_max == None):
        values_max = max(df_boxplot['boxplot_value'])
    
    if(values_increment == None):
        values_increment = math.ceil(values_max / 10)
    
    fig, ax = plt.subplots(figsize = (11,9))
    
    if(vertical and comparison_column):
        ax = sns.boxplot(
            x = df_boxplot['column_name'],
            y = df_boxplot['boxplot_value'],
            orient = 'v',
            hue = df_boxplot['comparison_column'],
    #         color = colours,
        )
        ax.set_xlabel(title_label)
        ax.set_ylabel(values_label)
        ax.yaxis.set_ticks(np.arange(values_min, values_max + values_increment, values_increment))
    elif(vertical and not comparison_column):
        ax = sns.boxplot(
            x = df_boxplot['column_name'],
            y = df_boxplot['boxplot_value'],
            orient = 'v',
    #         color = colours,
        )
        ax.set_xlabel(title_label)
        ax.set_ylabel(values_label)
        ax.yaxis.set_ticks(np.arange(values_min, values_max + values_increment, values_increment))
    elif(not vertical and comparison_column):
        ax = sns.boxplot(
            x = df_boxplot['boxplot_value'],
            y = df_boxplot['column_name'],
            orient = 'h',
            hue = df_boxplot['comparison_column']
    #         color = colours,
        )
        ax.set_xlabel(values_label)
        ax.set_ylabel(title_label)
        ax.xaxis.set_ticks(np.arange(values_min, values_max + values_increment, values_increment))
    elif(not vertical and not comparison_column):
        ax = sns.boxplot(
            x = df_boxplot['boxplot_value'],
            y = df_boxplot['column_name'],
            orient = 'h',
    #         color = colours,
        )
        ax.set_xlabel(values_label)
        ax.set_ylabel(title_label)
        ax.xaxis.set_ticks(np.arange(values_min, values_max + values_increment, values_increment))
        
    plt.rcParams['axes.facecolor'] = '#F0F0F0'
    sns.set() # Gridlines
    plt.title(title)
    
    if(comparison_column):
        plt.legend(title=comparison_column)

    if(not file_name):
        file_name = str(column_name_list[0]) + "_boxplot"
    plt.savefig('./graphs/' + file_name + '.png', bbox_inches='tight')

def create_histogram(
    df,
    column_name,
    title
):
    pass
    # Still working on it
    # Low priority - use create_bar with predefined labels and custom df

def create_line(
    df,
    column_name_list,
    sequential_label,
    values_label,
    title,
    file_name, 
    values_min = None,
    values_max = None,
    values_increment = None,
    handle_null_by: str = 'interpolation', # Options: ('interpolation', 'drop_row', 'mean', 'median'),
    row_object_name = None,
    row_object_list = [],
    only_show_average = False, # Only available for no row_object_name and no row_object_list,
    sequential_label_rotation_angle = 0
):
    """
    will interpolate values as default since this is seaborn based. If you are looking for discontinuity for np.nan values, use matplotlib
    """
    # Clean dataset with nulls
    df = df[column_name_list]
    
    if(handle_null_by == 'drop_row'):
        df = df.dropna(axis = 0)
    elif(handle_null_by == 'mean'):
        df = df.fillna(df.mean())
        pass
    elif(handle_null_by == 'median'):
        df = df.fillna(df.median())
        pass
    elif(handle_null_by == 'interpolation'):
        # This is seaborn, it will automatically interpret np.nan to be interpolated. Don't need to do anything
        pass
    else:
        print("handle_null_by invalid. Interpolating")
        pass
    
    # Transform dataset
    if(row_object_name):
        df_line = helpers.transform_df_for_line_named_rows(df, column_name_list, row_object_name, row_object_list)
    elif(row_object_list and row_object_name == None):
        df_line = helpers.transform_df_for_line_named_rows(df, column_name_list, 'row_object', row_object_list)
    else:
        df_line = helpers.transform_df_for_line_unnamed_rows(df, column_name_list)
    
    fig, ax = plt.subplots(figsize = (11,9))
    
    if(row_object_name):
        sns.lineplot(
            data=df_line, 
            x='index', 
            y='value', 
            hue=row_object_name, 
            marker='o',
            sort = False
        )
    elif(row_object_list and row_object_name == None):
        sns.lineplot(
            data=df_line, 
            x='index', 
            y='value', 
            hue='row_object', 
            marker='o',
            sort = False
        )
    elif((not row_object_list and row_object_name == None) and only_show_average):
        sns.lineplot(
            data=df_line, 
            x='index', 
            y='value', 
            marker='o',
            legend = False,
            sort = False
        )
    else:
        sns.lineplot(
            data=df_line, 
            x='index', 
            y='value', 
            hue = 'row_object',
            marker='o',
            legend = False,
            sort = False
        )
    
    ax.set_xlabel(sequential_label)
    ax.set_ylabel(values_label)
    plt.title(title)
    
    values_max_was_automatically_set = False
    values_min_was_automatically_set = False
    if(values_max == None):
        values_max = max(df_line['value'])
        values_max_was_automatically_set = True
    if(values_min == None):
        values_min = min(df_line['value'])
        values_min_was_automatically_set = True
    if(values_increment == None):
        values_increment = math.ceil(values_max / 10)
        
    if(values_max_was_automatically_set):
        values_max = values_max + values_increment
    else:
        values_max = values_max + (values_increment / 100) # np.arange for set_ticks is not inclusive
    if(values_min_was_automatically_set):
        values_min = values_min - values_increment
        
    ax.yaxis.set_ticks(np.arange(values_min, values_max, values_increment))

    if(sequential_label_rotation_angle == 0):
        plt.xticks(rotation=sequential_label_rotation_angle)
    else:
        plt.xticks(rotation=sequential_label_rotation_angle, ha='right')
    
    plt.savefig('./graphs/' + str(file_name) + '.png', bbox_inches='tight')
    plt.close()

def create_line_no_interpolation(
    df,
    column_name,
    title
):
    """
    Use this line graph for datasets that contain np.nan and you DON'T want drop them.
    This will create non continous graphs
    Uses matplotlib
    """
    pass
    # Still working on it
    # Low priority - use create_line with null handling for the time being

def create_line_category_traversal(
    df,
    column_name_list,
    sequential_label,
    categorical_label,
    title,
    # file_name,
    categorical_order: list, # sorted 0 to n
    show_individual_lines = True,
    show_average_confidence_line = False,
):
    # encode the categorical variables
    pass

def create_pie( 
    df,                     # pandas DataFrame, Non Aggregate and cleaned
    column_name,            # column name in the dataframe
    title,                  # title of the pie chart

    labels = [],            # labels for the legend to follow in specific order,
    drop_values = [],       # list of strings. If need to drop column value quickly, use this
    colours = [],           # list of strings. Hex colours for pie chart 
    file_name = None,       # Name of file to save bar graph to,
    legend_title = None     # Name to be displayed on legend
):
    """
    DataFrame format:
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
    """
    count = Counter()

    if (not colours):
        colours = sns.color_palette('muted')
    
    if(df[column_name].isnull().values.any()):
        df = df.dropna(axis=0)

    for value in df[column_name]:
        count[value] += 1
    
    if(drop_values):
        for i in drop_values:
            if(i in count):
                del count[i]
        
    if(labels):
        title_temp = list(count.keys())
        values_temp = list(count.values())
        dictionary = {title_temp[i] : values_temp[i] for i in range(0, len(title_temp))}

        df_temp = pd.DataFrame()
        df_temp['title'] = labels
        df_temp['values'] = 0

        for key, value in dictionary.items():
            df_temp.loc[df_temp.title == key, 'values'] = value
    else:
        df_temp = pd.DataFrame({'title': list(count.keys()), 'values': list(count.values())})
        df_temp = df_temp.sort_values(by=['values'], ascending = False)
    
    fig, ax = plt.subplots(figsize = (11,9))
    plt.pie(
        x = df_temp['values'],
        labels = df_temp['title'],
        autopct = '%1.1f%%',
        startangle = 90,
        pctdistance = 1.05,
        labeldistance = None,
        colors = colours
       )
    
    plt.title(label = title)
    
    if(legend_title == None):
        legend_title = "Legend"
    plt.legend(df_temp['title'], title=legend_title)
    plt.axis('equal')

    if(not file_name):
        file_name = str(column_name)
    plt.savefig('./graphs/' + file_name + '.png', bbox_inches='tight')

    plt.close()

def create_scatter(
    df,                         # pandas Dataframe. Non Aggregate cleaned values
    x_column_name,              # x axis column values
    y_column_name,              # y axis column values
    title,                      # title of graph

    file_name = None,           # name of the file to save the bar graph to
    x_axis_label = None,        # label of the x axis
    y_axis_label = None,        # label of the y axis
    x_axis_values: list = []    # Order of x axis labels to follow - TODO: CHECK IF ACTUALLY WORKS
):
    """
    DataFrame format:
    +------------------+---------------+
    |  column_name_X   | column_name_Y |
    +------------------+---------------+
    | number string 1  | number 1      |
    | number string 2  | number 2      |
    | number string 3  | number 3      |
    | number string 4  | number 4      |
    +------------------+---------------+
    """
    df_temp = pd.DataFrame({x_column_name: df[x_column_name], y_column_name: df[y_column_name]})

    if(df_temp.isnull().values.any()):
        df_temp = df_temp.dropna(axis=0)

    if(x_axis_values):
        df_temp = df_temp.sort_values(by=[x_axis_values])
    else:
        df_temp = df_temp.sort_values(by=[x_column_name], ascending=True)
    
    plt.figure(figsize = (11,9))
    plt.scatter(
        x = df_temp[x_column_name],
        y = df_temp[y_column_name],
    )
    plt.title(label = title)
    plt.grid()
    if(not x_axis_label):
        plt.xlabel(x_column_name)
    else:
        plt.xlabel(x_axis_label)
        
    if(not y_axis_label):
        plt.ylabel(y_column_name)
    else:
        plt.ylabel(y_axis_label)

    if(not file_name):
        file_name = str(x_column_name) + " vs " + str(y_column_name)
    plt.savefig('./graphs/' + file_name + '.png', bbox_inches='tight')

    plt.close()