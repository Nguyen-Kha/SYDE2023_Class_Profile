# Graph Generation

Add python scripts to generate your graphs here. 

In this directory, you have access to the following files:
- graphs.py - These are where the graph functions are located to generate standard graphs in matplotlib or seaborn
- helpers.py - These contain helper functions that graphs.py uses to generate graphs

## Generating Graphs

To generate graphs do the following

Choose which graphs you want to generate in the notion, and assign it to yourself
You may need to know what the values in the graph actually mean. Use this spreadsheet to get a mapping of the values. This spreadsheet is organized to match the CSVs in Google Cloud Storage
https://docs.google.com/spreadsheets/d/1-94ugrPMWif4J0ziSc2-xgccZcz3a5b9YqfNJL_eJus/edit#gid=0

1. Create a new branch
`git checkout -b YOUR_BRANCH_NAME`
2. Create a python file in this directory, or use the default ones given above
OPTIONAL: also create a jupyter notebook file. You can also create graphs here to test stuff out
3. Follow the template, or have a look at the other graph generation python files to understand how to use graphs.py
4. Use the libraries to create the graph

Once you have finished above, do the following to output your graph
5. go into your terminal / command line
6. navigate to this directory.
- `pwd`
- `cd (whatever it takes to get here)`
- `cd SYDE2023_Class_Profile/graph_generation`
7. run the following
- `python <YOUR_PYTHON_FILE_NAME_WITH_GRAPHS>.py`
8. Graphs should be found in the ./graphs/ folder
9. Push your changes, Open a Pull Request on github and merge
```
git add "FILES_THAT_YOU_HAVE_CHANGED.py" "ANOTHER_FILE_THAT_YOU_CHANGED.py"
git commit -m "YOUR COMMIT MESSAGE"
git push
```
10. Go into Google Cloud Storage, and upload your graph .png file into the appropriate folder in ./_completed_graphs/...

## HELP! Something is wrong with the graph generation
Honestly a mood. There are some known issues with the template graph functions and we have zero time to iron them out considering we are like 4 months overdue at the time I'm writing this, but here are some quick fixes

#### There are some values in the dataframe that shouldn't be there and it's breaking the graph aesthetic
Sometimes data cleaning doesn't remove all the bad data. Sometimes there are outliers, or extra whitespace, or a spelling mistake. Looking at tens of thousands of cells really burns your eyes. There's a few things you can do
1. If the graph you are using has a `drop_values` parameter, pass the bad value in there to remove it from the graph generation. This removes the data point completely and treats it as a null
`drop_values = ['string_of_data_to_drop', 73, 'another_string', 324.35]`
2. If drop_values doesn't exist, with your dataframe / subset dataframe, drop that row from it (treat is as a null). You can follow these steps down below:
https://stackoverflow.com/questions/43136137/drop-a-specific-row-in-pandas
3. If you still want to use that value in generating the graph, change that specific value in the dataframe. If you're well versed in python or coding, this step might be good
- Find the column name in the dataframe
- Create a function to replace the value with the value you want. have a look at ./data_cleaning/2_accf/clean_accf.py functions clean_coop_position_rating() and clean_exchange_unis(). Or helpers turn_dates_into_actual_values()
- Then do `df['column_name'] = df['column_name'].apply(clean_column_value)` to change it
You can use your dataframe afterwards to generate the graph
- You should also save that function you made somewhere 
4. Modifying the value itself in the CSV, and then reimporting the csv to generate the graph

If you do any of the above steps, let Kha know and he will apply those changes into the master data_cleaning functions, then replace the CSVs in Google Cloud Storage to the correct ones. You can open up an issue in github
- Or if you're well versed with python, you can probably add those changes yourself to the data_cleaning folder

#### I can't set the colours on the graph
Choosing colours is a known issue: We're looking for a way to incorporate colours into the boilerplate code. Currently for some of the graphs, dynamically choosing a colour and choosing the default seaborn colour palette conflicts with each other.
If you have a set number of colours you want to use:
- pass in `colours = ['#hexcode', 'black', 'whatever_colour_you_want] ` in the parameters
- uncomment the `color = colours[i]` in graphs.py where your graph is being generated
- generate the graph
This should be a work around, but you'll have to enable and disable it for the time being if you want specific colours on your graph

#### Numbers are missing on the x axis / title axis
This is also a known issue. The x axis values are dynamically generated from what is given in the dataset. There are ways to get around it, but it's difficult to incorporate into the boilerplate
The rationale is that we can leave these for the time being, and then remake the graphs in Figma or something to make it prettier, cause there is no way matplotlib or seaborn is an aesthetic way to publish graphs

#### The graph generating things are unironically broken
Create an issue in github, give details on which CSV you are using, which columns are you using, and which graph you are trying to make with its parameters. Kha will have a look at it