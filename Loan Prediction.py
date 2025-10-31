ewfgjy
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree

#Loading data file
fullFileName= 'C:/Users/Fredrich Bernard/Desktop/AI Engineering/Decision Tree/Decision_Tree_ Dataset.csv'
balance_data = pd.read_csv(fullFileName, sep=',', header=0)
print("Data Length:: ", len(balance_data))
print("Data Shape:: ", balance_data.shape)
print("Dataset:: ")
balance_data.head()


#Separating Target variable
X = balance_data.values[:, 1:5]
Y = balance_data.values[:, 0]


#Spliting Dataset into Test and Train
X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size = 0.3, random_state = 100)
#Function to perform training with Entropy
clf_entropy = DecisionTreeClassifier(criterion = "entropy", random_state = 100,
 max_depth=3, min_samples_leaf=5)
clf_entropy.fit(X_train, y_train)






