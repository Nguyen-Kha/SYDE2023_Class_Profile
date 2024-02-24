# necessary imports
import numpy as np  # use for array and matrix stuff
import pandas as pd  # use for dataframes, think of it as excel
import math
import matplotlib.pyplot as plt  # use to make graphs
import seaborn as sns
from collections import Counter

# import helpers
import graphs
import functools

df_school = pd.read_csv("csv/school.csv")

graphs.create_bar(
    df_school,
    "fav_core",
    "Core Course",
    "Percentage of Respondents",
    "What was your favourite core course?",
    False,
    display_as_percentage=True,
    values_increment=5,
)

graphs.create_bar(
    df_school,
    "fav_profs",
    "Professor",
    "Percentage of Respondents",
    "Who were your favourite profs?",
    False,
    display_as_percentage=True,
    splice_required=True,
)

graphs.create_bar(
    df_school,
    "fav_te",
    "Technical Elective",
    "Percentage of Respondents",
    "What was your favourite TE?",
    False,
    display_as_percentage=True,
    splice_required=True,
    max_label_length=40,
)

graphs.create_bar(
    df_school,
    "fav_cse",
    "Complementary Studies Elective",
    "Percentage of Respondents",
    "What was your favourite CSE?",
    False,
    display_as_percentage=True,
    splice_required=True,
)

graphs.create_bar(
    df_school,
    "cr_ncr",
    "Number of Courses",
    "Percentage of Respondents",
    "How many courses did you CR/NCR?",
    True,
    display_as_percentage=True,
)

graphs.create_bar(
    df_school,
    "failed",
    "Options",
    "Percentage of Respondents",
    "From the options below, what have you failed?",
    False,
    display_as_percentage=True,
    splice_required=True,
    labels=[
        "I have not failed any of the above",
        "A course",
        "A work report",
        "An exam",
        "An assignment",
        "A quiz / test",
    ],
)
