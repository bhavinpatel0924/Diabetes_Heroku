## Diabetes Prediction: Project Overview

* Created a model to help predict if an individual has diabetes or not using Random Forest and the evaluation metric as Recall Score (recall_score = .9883).
* Cleaned the dataset and handled missing values with custom techniques.
* Optimized Random Forest model with hyperparameter tuning using RandomSearchCV to obtain the best parametes.
* Create an API with the help of the Streamlit library and deployed the model to Heroku.

### Resources Used 

* **Kaggle Dataset/Github url:** 'https://raw.githubusercontent.com/anujvyas/Diabetes-Prediction-Deployment/master/kaggle_diabetes.csv'
* **Python:** Version 3.7
* **Libraries:** pandas, seaborn, matplotlib, sklearn, numpy, pickle, streamlit.
* **Streamlit Tutorial:** https://www.youtube.com/watch?v=5XnHlluw-Eo&t=334s
* **Heroku Deployment Tutorial:** https://www.youtube.com/watch?v=zK4Ch6e1zq8&list=PLtqF5YXg7GLmCvTswG32NqQypOuYkPRUE&index=5

### Data Cleaning and Feature Engineering

* Imputed missng values using a custom function that used the Outcome variable to find a median value.
* Transformed data using MinMaxScale and StandardScaler to compare performance

### Model Building, Performance, and Evaluation

Compared Random Forest, XGBoost, and KNearestNeighbors using the recall metric. I created a custom stratifiedkfold function and used a combination of train_test_split and cross_val_score to compare the scores and to avoid overfitting. I used the recall metric for this dataset because the purpose of the dataset is predict if an individual has diabetes or not. It's very important that we try to minimize our type 2 error (False Negatives) because it's potentially harmful if we tell someone that they do not have diabetes when in actuality they do.

* **RandomForestClassifier Recall Score:** .9883 (Performed the best)

### Productionization and Deployment

Created an API using the streamlit library in the Spyder editor and predicted if someone has diabetes using Pregnancy, Insulin, BMI, Age, Diabetes Pedigree, BloodPressure, Glucose as my independent features and deployed the app to the Heroku Platform. 



 
