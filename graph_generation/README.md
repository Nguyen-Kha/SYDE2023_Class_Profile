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