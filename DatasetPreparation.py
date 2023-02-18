# Import Library 
import pandas as pd

# Import data train
dt_train = pd.read_csv("Dataset/train.csv") # With label data
dt_test = pd.read_csv("Dataset/test.csv") # Withou label data

# Show the dataset
dt_train.head()
dt_test.head()
