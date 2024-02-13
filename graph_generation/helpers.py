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