import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import numpy as np

df = pd.read_csv('/Users/rishiahuja/Downloads/weight-height.csv')

# selecting the weight index from all the rows of the df dataframe

x2 = df.iloc[:,1:2].values/12  # height
y2 = df.iloc[:,2].values*.45 # weight

# creating a scatter plot for the two data weight on y axis and height on the x axis

plt.scatter(x2,y2,label="height",color="Orange",s=5)
plt.xlabel("Height(in ft.)")
plt.ylabel("Weight(in kgs)")
plt.title("Weight vs Height")
plt.legend(loc = "lower right")
plt.show()

# training and testing the model

x_train, x_test, y_train, y_test = train_test_split(x2,y2,test_size=0.35,random_state=123)
regressor = LinearRegression()
regressor.fit(x_train, y_train)
y_prediction=regressor.predict(x_test)
c = regressor.intercept_
m = regressor.coef_
print('intercept =', c)
print('slope=', m)

x = float(input('enter height: '))

y_pred = m * x + c

print('predicted weight: ', y_pred)

print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))