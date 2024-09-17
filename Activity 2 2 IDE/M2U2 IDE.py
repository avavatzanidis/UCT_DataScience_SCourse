import pandas as pd
from sklearn.tree import DecisionTreeRegressor, plot_tree  
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('Boston.csv', delimiter = ",")
# Explore the size of the data set.
df.shape
