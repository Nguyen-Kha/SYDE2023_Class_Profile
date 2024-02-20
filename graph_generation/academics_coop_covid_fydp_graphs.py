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

df_school = pd.read_csv('csv/school.csv')

graphs.create_bar(
  df_school,
  "fav_core",
  'Core Course', 
  'Percentage of Respondents', 
  'Which core course was your favorite?',
  False,
  display_as_percentage=True,
  values_increment=5,
)

graphs.create_bar(
  df_school,
  "fav_profs",
  'Professor', 
  'Percentage of Respondents', 
  'Which prof was your favorite?',
  False,
  display_as_percentage=True,
  splice_required=True,
)
