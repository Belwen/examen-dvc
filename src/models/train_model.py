import sklearn
import pandas as pd 
from sklearn.linear_model import ElasticNet
import joblib
import numpy as np
import pickle

#--Load the best parameters
filename = 'models/best_params.pkl'
with open(filename, "rb") as f:
    params = pickle.load(f)
    print("Parameters loaded successfully.")

#--Load data
X_train_scaled = pd.read_csv('data/processed_data/X_train_scaled.csv')
y_train = pd.read_csv('data/processed_data/y_train.csv')
y_train = np.ravel(y_train)


#--Instanciate with the parameters fond with GridSearch
elastic_net = ElasticNet(alpha=params['alpha'], l1_ratio=params['l1_ratio'], max_iter=params['max_iter'])

#--Train the model
elastic_net.fit(X_train_scaled, y_train)

#--Save the trained model
model_filename = 'models/trained_model.joblib'
joblib.dump(elastic_net, model_filename)
print("Model trained and saved successfully.")


elastic_net.predict(X_train_scaled)