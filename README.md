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



