# necessary imports
import numpy as np                # use for array and matrix stuff
import pandas as pd               # use for dataframes, think of it as excel
import math
import matplotlib.pyplot as plt   # use to make graphs
import seaborn as sns
from collections import Counter
# import helpers
import graphs
import functools

df = pd.read_csv('csv/before_syde.csv')

## HOW DID YOU HEAR ABOUT SYDE
graphs.create_bar(
    df, 
    'hear_about_syde', 
    'Option', 
    'Percentage of Respondents', 
    'How did you hear about SYDE?',
    False,
    display_as_percentage=True,
    convert_to_string=True,
)
