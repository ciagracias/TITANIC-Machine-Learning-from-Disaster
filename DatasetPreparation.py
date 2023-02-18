# Import Library 
import pandas as pd

# Import Training Data
dt_train = pd.read_csv("Dataset/train.csv") # With label data
# Import Test Data
dt_test = pd.read_csv("Dataset/test.csv") # Without label data

# Show the dataset
dt_train.head()
dt_test.head()

# Separates the data set into feature and label data in Training Data
x_train = dt_train.iloc[:, 0:8] # Feature
y_train = dt_train.iloc[:, -1] # Label
# Separates the data set into feature data in  Test Data
x_test = dt_test.iloc[:, 0:8] # Feature

# Show the Training Data
x_train
# Show the Test Data
x_test

# Missing values in Training Data
x_train.isnull().sum()
y_train.isnull().sum()
# Missing values in  Test Data
x_test.isnull().sum()

# Handling missing values in Training Data
# Age column
age = x_train['Age'].mean() 
x_train['Age'] = x_train['Age'].fillna(age) 
# Embarked column
x_train['Embarked'] = x_train['Embarked'].fillna('N')
# Survived column
y_train['Survived'] = y_Train['Survived'].fillna(0)

# Handling missing values in  Test Data
# Age column
age = x_train['Age'].mean() 
x_train['Age'] = x_train['Age'].fillna(age) 
# Embarked column
x_train['Embarked'] = x_train['Embarked'].fillna('N')

# Double check missing value in Training Data
x_train.isnull().sum()
# Double check missing value in  Test Data
x_test.isnull().sum()
