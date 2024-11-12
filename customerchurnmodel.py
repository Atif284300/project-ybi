# -*- coding: utf-8 -*-
"""Customer_Churn_Prediction_Model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dupMgICf1-WfKP16XH4tSUQSud8Kpp9T
"""

from google.colab import drive
drive.mount('/content/drive')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Datasets/Churn_Modelling.csv')

dataset.head()

dataset.info()

dataset.describe()

dataset= dataset.drop(columns = ['RowNumber','CustomerId','Surname'])

dataset.info()

dataset['Gender'].unique()

"""#fyi : One-hot encoding is a popular technique used in machine learning and data processing to represent categorical variables or features as binary vectors."""

dataset= pd.get_dummies(data=dataset,drop_first=True)

"""#fyi : If two or more independent variables have an exact linear relationship between them then it is perfect multicollinearity"""

dataset

dataset.Exited.plot.hist()

(dataset.Exited==1).sum()

dataset_2=dataset.drop(columns='Exited')

dataset_2.corrwith(dataset['Exited']).plot.bar(figsize=(16,9), title='Correlated with Exited Column', rot = 45,grid = True)

corr=dataset.corr()

plt.figure(figsize=(16,9))
sns.heatmap(corr,annot=True)

X= dataset.drop(columns='Exited')
y= dataset['Exited']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

X_test.shape

"""fyi : StandardScaler is a commonly used technique in machine learning for standardizing or scaling numerical features before fitting a model. It transforms the data by subtracting the mean and dividing by the standard deviation, resulting in a distribution with a mean of 0 and a standard deviation of 1."""

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train= scaler.fit_transform(X_train)
X_test= scaler.transform(X_test)

X_train

"""fyi : Logistic regression is used for predicting the categorical dependent variable using a given set of independent variables."""

from sklearn.linear_model import LogisticRegression
clf = LogisticRegression(random_state=0).fit(X_train, y_train)

y_pred= clf.predict(X_test)

from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, precision_score, recall_score

acc=accuracy_score(y_test,y_pred)
f1=f1_score(y_test,y_pred)
prec=precision_score(y_test,y_pred)
rec=recall_score(y_test,y_pred)

results=pd.DataFrame([['Logistic regression',acc,f1,prec,rec]],columns=['Model','Accuracy','F1','Precision','Recall'])
results

print(confusion_matrix(y_test,y_pred))

"""fyi : Random Forest is a classifier that contains a number of decision trees on various subsets of the given dataset and it takes the average to improve the predictive accuracy of that dataset."""

from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(random_state=0).fit(X_train, y_train)
y_pred= clf.predict(X_test)
acc=accuracy_score(y_test,y_pred)
f1=f1_score(y_test,y_pred)
prec=precision_score(y_test,y_pred)
rec=recall_score(y_test,y_pred)
RF_results=pd.DataFrame([['Random Forest Classifier',acc,f1,prec,rec]],columns=['Model','Accuracy','F1','Precision','Recall'])
results.append(RF_results,ignore_index=True)

print(confusion_matrix(y_test,y_pred))

dataset.head()

single_obs=[[647,40,3,85000.45,2,0,0,92012.45,0,1,1]]
clf.predict(scaler.fit_transform(single_obs))
