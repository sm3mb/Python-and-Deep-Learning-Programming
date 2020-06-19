import pandas as pd
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import  classification_report

df = pd.read_csv('./datasets/glass.csv')
x_train = df.drop("Type", axis=1)
y_train = df["Type"]
x_train, x_test, y_train, y_test = train_test_split(x_train, y_train, test_size=0.2, random_state=0)

 #SVM
svc = SVC()

# Train the model using the training sets
svc.fit(x_train, y_train)

# Predict the response for test dataset
y_pred = svc.predict(x_test)

#Evaluating Model
acc_svc = accuracy_score(y_test, y_pred)*100
print (classification_report(y_test,y_pred))
print("svm accuracy is:", acc_svc)