# Import library
from sklearn.naive_bayes import GaussianNB 
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt 
import seaborn as sns 

# Classification with GaussianNB
classifier = GaussianNB
classifier.fit(x_train, y_train) # Train a classification models
classifier.score(x_train, y_train) # Accuracy

# Accuracy with Confusion Matrix
f, ax = plt.subplots(figsize=(5,5))
sns.heatmap(
    confusion_matrix(y_train, y_pred), 
    annot=True, 
    fmt=".0f", 
    ax=ax, 
    cmap="Blues"
)
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.show()

# Predicting the Test Set result
y_pred = classifier.predict(x_test) 
y_pred # Show the result

# Predictin the Test Set result one by one
y_pred = classifier.predict([x_test[12]]) # indexing to 12
y_pred # Show the result
