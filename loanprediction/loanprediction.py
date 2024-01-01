import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm

data=pd.read_csv("C:/Users/hitesh/Documents/gptAi/python/frauddetection/loanprediction/loan.csv")
data.head()
data.info()
data.isnull().sum()
