import pandas as pd

import numpy as np

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier

from sklearn import metrics

from sklearn.metrics import confusion_matrix

import matplotlib.pyplot as plt

import seaborn as sns


df = pd.read_csv('csv_result-Training Dataset.csv')
confusion_matrix_file = 'confusion_matrix.png'

print(df.head())

X = df.iloc[:, :-1]

y = df.iloc[:, -1]

Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, random_state=0)

model = DecisionTreeClassifier()
model.fit(Xtrain, ytrain)

ypred = model.predict(Xtest)
print(metrics.classification_report(ypred, ytest))
print("\n\nAccuracy Score:", metrics.accuracy_score(ytest, ypred).round(2)*100, "%")

mat = confusion_matrix(ytest, ypred)

sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=True)

plt.xlabel('true label')

plt.ylabel('predicted label');
print(Xtest)
user = input('Enter URL to check: ')

prediction = model.predict(user)

