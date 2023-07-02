import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn.svm import SVC

iris = datasets.load_iris()
X = iris.data[:, [2, 3]]
y = iris.target
df = pd.DataFrame(iris.data[:,[2,3]], columns=iris.feature_names[2:])
print(df.head())

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.40, random_state=123)
print(x_train.shape[0], x_test.shape[0])

svc = SVC(kernel='rbf',random_state=0,gamma=0.1,C=1.0)
svc.fit(x_train, y_train)
print(svc.score(x_test, y_test))

