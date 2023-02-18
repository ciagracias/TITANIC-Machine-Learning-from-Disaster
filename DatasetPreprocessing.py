# Import Library
from sklearn.preprocessing import LabelEncoder # Encode data
from sklearn.preprocessing import StandarScaler # Scalling data

# Encode Data
le = LabelEncoder()
# Training data encoding
le.fit(x_train['Sex'])
x_train['Sex'] = le.transform(x_train['Sex'])
le.fit(x_train['Embarked'])
x_train['Embarked'] = le.transform(x_train['Embarked'])
# Test data encoding
le.fit(x_test['Sex'])
x_test['Sex'] = le.transform(x_test['Sex'])
le.fit(x_test['Embarked'])
x_test['Embarked'] = le.transform(x_test['Embarked'])
# Displays the data after it has been encoded
x_train
x_test

# StandarScaler
sc = StandardScaler()  
# Scalling data
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)  
