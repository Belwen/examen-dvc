from sklearn.linear_model import ElasticNet
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score
import pandas as pd
import numpy as np
import pickle

#--Load data
X_train_scaled = pd.read_csv('data/processed_data/X_train_scaled.csv')
y_train = pd.read_csv('data/processed_data/y_train.csv')
y_train = np.ravel(y_train)

#--Create ElasticNet instance
elastic = ElasticNet()

#--Parameters to test
param_grid = {
    "alpha": [0.01, 0.1, 1.],
    "l1_ratio": [.1, .3, .5, .7, .9],
    "max_iter": [10, 100, 1000, 10000]
}

#--Fit the model and print scores
gridsearch = GridSearchCV(estimator=elastic, param_grid=param_grid, cv=10, scoring="r2")
gridsearch.fit(X_train_scaled, y_train)
print(gridsearch.best_score_)


#--Save the best parameters
filename = 'models/best_params.pkl'
with open(filename, "wb") as f:
    pickle.dump(gridsearch.best_params_, f)
    print("Parameters saved successfully.")

