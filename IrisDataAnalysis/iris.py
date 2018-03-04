"""
Owen Sullivan
iris.py
A program to make sense of and predict data for 
    Iris Flowers
"""

# Imports
import sys
import numpy
import scipy
# Matplotlib Utils
import matplotlib
import matplotlib.pyplot as plt
# Pandas Utils
import pandas
from pandas.plotting import scatter_matrix

# sklearn Utils
import sklearn
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

# Grab our data
dataURL = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# These are the keys to our values in the data set
data_names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']

#create our dataset object to work with
dataset = pandas.read_csv(dataURL , names = data_names)


# Print out some univariate plots to understand each attribute
dataset.hist()
plt.show()
dataset.plot(kind="box",subplots=True,layout=(2,2), sharex=False, sharey=False)
plt.show()

# Print out some Multivariate plots to see data relation
scatter_matrix(dataset)
plt.show()

