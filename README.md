# TITANIC - Machine Learning from Disaster
<b><h3>PREDICTING SURVIVAL ON THE TITANIC USING NAÏVE BAYES</h3></b>

Naive bayes 
🚢 The sinking of the Titanic is one of the most famous shipwrecks in history. 
<br/> 📆 On April 15, 1912, during its maiden voyage, the widely considered "unsinkable" RMS Titanic sank after colliding with an iceberg. 
<br/> 😧 Unfortunately, there were not enough lifeboats for everyone on board, resulting in the deaths of 1502 of the 2224 passengers and crew. 
<br/> 🏊 While there is an element of luck involved in survival, it seems that some groups of people are more likely to survive than others. 
<br/> --------------------------------------------------------------------------------------------------------------------------------------------------------- <br/>
This program contains a predictive model that answers the question: <b>"which kind of person is more likely to survive?"</b> using passenger data (i.e. name, age, gender, socioeconomic class, etc.). The data is divided into two parts, namely training set and test set. <br/>
The training set should be used to build your machine learning models. For the training set, we provide the outcome (also known as the "ground truth") for each passenger. Your model will be based on "features" like passengers' gender and class. You can also use feature engineering to create new features. The test set should be used to see how well your model performs on unseen data.
<table>
  <tr>
    <td colspan="10" align="center"> Feature Data </td>
    <td align="center"> Label Data </td>
  </tr>
  <tr>
    <td>PassengerId</td>
    <td>Pclass</td>
    <td>Name</td>
    <td>Sex</td>
    <td>Age</td>
    <td>SibsP</td>
    <td>Ticket</td>
    <td>Fare</td>
    <td>Cabin</td>
    <td>Embarked</td>
    <td>Survived</td>
  </tr>
 </table>

<h4> ✏️ MISSING VALUE ✏️</h4>
<li> There are 2 missing values in the ‘Embarked’ column. Embarked implies where the traveler mounted from. There are three possible values for Embark : Southampton, Cherbourg, and Queenstown. Because the missing value in the column is of type str, we’ll fill it in by adding a new value 'N' which means Nothing.<br/>
<li> There are 177 missing values in the ‘Age’ column. Because the missing value in the column is of type int, we’ll fill it in by mean.<br/>
<li> Thre are 687 missing values in the ‘Cabin’ column. Since the missing data in the 'Cabin' column exceeds 50% of the dataset, we recommend that this column be omitted.
