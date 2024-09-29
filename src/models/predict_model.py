import joblib
import pandas as pd
import numpy as np
import pandas as pd
import json
import os
from sklearn.metrics import r2_score, mean_squared_error

#--Load model
loaded_model = joblib.load("models/trained_model.joblib")

#--Load test data
X_test_scaled = pd.read_csv('data/processed_data/X_test_scaled.csv')
y_test = pd.read_csv('data/processed_data/y_test.csv')
y_test = np.ravel(y_test)

#--Predict
y_pred = loaded_model.predict(X_test_scaled)

#--Save predictions
output_folderpath = "data/predictions/"
pd.DataFrame(y_pred, columns=['silica_concentrate']).to_csv(output_folderpath + "/prediction.csv",index=None)
print("Predictions saved.")

#--Compute metrics
scores = {
    "r2": r2_score(y_test, y_pred),
    "mse" : mean_squared_error(y_test, y_pred)
}

#--Save metrics
output_metrics_folder = "metrics"
with open(output_metrics_folder + "/scores.json", 'w') as f:
    json.dump(scores, f)
    print("Metrics saved successfully.")