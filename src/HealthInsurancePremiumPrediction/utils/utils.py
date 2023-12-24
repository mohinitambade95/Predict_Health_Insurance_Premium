import os
import sys
import pickle
import numpy as np
import pandas as pd
from src.HealthInsurancePremiumPrediction.logger import logging
from src.HealthInsurancePremiumPrediction.exception import customexception
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score

from sklearn.metrics import r2_score, mean_absolute_error,mean_squared_error

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise customexception(e, sys)
    
def evaluate_model(X_train,y_train,X_test,y_test,models,params):
    try:
        report = {}
        for i in range(len(models)):
            model = list(models.values())[i]
            param = params[list(models.keys())[i]]
            
            logging.info(f'Grid search cv to find best parameter for {model}')
            gs = GridSearchCV(model,param,cv=5)
            gs.fit(X_train,y_train)
            
            logging.info(f'Model fit with {model}')
            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)

            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            rmse_train = mean_squared_error(y_train,y_train_pred,squared=False)
            rmse_test = mean_squared_error(y_test,y_test_pred,squared=False)
            logging.info(f'RMSE  with {model} on train data is {rmse_train}')
            logging.info(f'RMSE  with {model} on test data is {rmse_test}')
            
            r2_score_train = r2_score(y_train,y_train_pred)
            r2_score_test = r2_score(y_test,y_test_pred)

            logging.info(f'R square  with {model} on train data is {r2_score_train}')
            logging.info(f'R square  with {model} on test data is {r2_score_test}')

            
            
            # Get R2 scores for train and test data
            #train_model_score = r2_score(ytrain,y_train_pred)
            test_model_score = r2_score_test

            report[list(models.keys())[i]] =  test_model_score

        return report

    except Exception as e:
        logging.info('Exception occured during model training')
        raise customexception(e,sys)
    
def load_object(file_path):
    try:
        with open(file_path,'rb') as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        logging.info('Exception Occured in load_object function utils')
        raise customexception(e,sys)

    