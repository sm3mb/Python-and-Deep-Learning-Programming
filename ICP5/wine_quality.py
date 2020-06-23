import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

train = pd.read_csv('winequality-red.csv')

##handling missing value
data = train.select_dtypes(include=[np.number]).interpolate().dropna()

# Top 3 correlation
data_correlation = data.corr()['quality'][:11]
sorted_data = data_correlation.sort_values(ascending=False)
print("Descending order")
print(sorted_data[0:3])


target_data = train.quality
features_data = data.drop(['quality'], axis=1)

features_train, features_test, target_train, target_test = train_test_split(features_data, target_data, random_state=42, test_size=.33)


lr = linear_model.LinearRegression()
# Train the model using the training sets
model = lr.fit(features_train, target_train)

# Evaluate the performance
predictions = model.predict(features_test) # Predict the response for test dataset
print("R^2 is: \n", r2_score(target_test, predictions))

print('RMSE is: \n', mean_squared_error(target_test, predictions))