import pandas
from keras.models import Sequential
from keras.layers.core import Dense, Activation

# load dataset
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

dataset = pd.read_csv("breastcancer.csv")
# dataset.info()

X = dataset.iloc[:,2:31].values

Y = dataset.iloc[:,1].values

from sklearn.preprocessing import LabelEncoder

# Encoding the Dependent Variable
labelencoder_Y = LabelEncoder()

Y = labelencoder_Y.fit_transform(Y)

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.25, random_state=87)

from sklearn.preprocessing import StandardScaler

sc =StandardScaler()

X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)
# Create model
my_first_nn = Sequential()

# Input Layer
my_first_nn.add(Dense(150, input_dim=29, activation='relu'))
# Hidden Layer
my_first_nn.add(Dense(10, activation='relu'))
my_first_nn.add(Dense(8, activation='relu'))
my_first_nn.add(Dense(25, activation='relu'))
# Output layer
my_first_nn.add(Dense(1, activation='sigmoid'))

# Compiling the Model
my_first_nn.compile(loss='mean_squared_error', optimizer='adam', metrics=['acc'])

# Training the Model
my_first_nn_fitted = my_first_nn.fit(X_train, Y_train, epochs=100,initial_epoch=0)

# Model Summary
print(my_first_nn.summary())

score = my_first_nn.evaluate(X_test, Y_test)
print("Loss ", score[0] * 100)
print("Accuracy ", score[1] * 100)
# print(my_first_nn.evaluate(X_test, Y_test))
