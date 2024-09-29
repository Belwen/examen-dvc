# Examen DVC et Dagshub
Dans ce dépôt vous trouverez l'architecture proposé pour mettre en place la solution de l'examen. 

```bash       
├── examen_dvc          
│   ├── data
│   │   ├── predictions       <-  Predictions made by predict_model.py
│   │   ├── processed_data    <-  Split and scaled datasets made by split_data.py
│   │   └── raw_data          <-  Original data
│   │     
│   ├── metrics               <-  Model score computed by preidct_model.py (R2 and MSE)  
│   │
│   ├── models                <-  Pickled best parameters and joblib model trained and saved
│   │
│   ├── src                    
│   │   ├── data              <-  Scripts to split data
│   │   │   ├── check_structure.py
│   │   │   └── split_data.py
│   │   └── models            <-  Scripts to find the best parameters, train models and make predictions
│   │       ├── gridsearch.py
│   │       ├── train_model.py
│   │       └── predict_model.py
│   └── README.md       
```
## Steps to follow

### 0. Clone repository
```
git clone https://github.com/Belwen/examen-dvc.git
```

### 1. Create a virtual environment and activate it
```
python -m venv my_env
source my_env/bin/activate
```

### 2. Install required packages
```
cd examen-dvc
pip install -r requirements.txt
```

### 3. Setup dvc credentials
```
dvc remote modify origin --local access_key_id YOUR_ACCESS_KEY
dvc remote modify origin --local secret_access_key YOUR_ACCESS_KEY
```
### 4. Reproduce pipeline
```
rm -rf data/raw_data
rm -rf .dvc/cache
dvc fetch data/raw_data.dvc
dvc pull
dvc checkout
dvc repro
```

