from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.pipeline import make_pipeline
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import numpy as np
import pandas as pd

df = pd.read_csv('melb_data.csv')
#print(df)

df=df.dropna(axis=0)
#print(df)

cols_to_use=['Rooms', 'Distance', 'Landsize', 'BuildingArea', 'YearBuilt','Price']

#defining the dependent and independent variables
X=df[cols_to_use]
print(X.describe())# describe : to view a few top values

print(X.head())

y=df.Price

# Decision Tree Classifier
pipeline = make_pipeline(SimpleImputer(), DecisionTreeClassifier())
score = cross_val_score(pipeline, X, y, scoring="neg_mean_absolute_error")
regressor = DecisionTreeRegressor(random_state=1)
regressor.fit(X, y)
print(regressor.predict(X.head()))