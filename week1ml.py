# -*- coding: utf-8 -*-
"""week1ml.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x_C-H3PiKi3LHdC9BnuT8iEYJ7mO7KDW
"""

import pandas as pd

# Webpage URL

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# Define the column names

col_names = ["sepal_length_in_cm",

"sepal_width_in_cm",

"petal_length_in_cm",

"petal_width_in_cm",

"class"]

# Read data from URL

iris_data = pd.read_csv(url, names=col_names)

iris_data.head()

iris_data.to_csv("cleaned_iris_data.csv")