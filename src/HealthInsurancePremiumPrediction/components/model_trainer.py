
import pandas as pd
import numpy as np
import os
import sys
from src.HealthInsurancePremiumPrediction.logger import logging
from src.HealthInsurancePremiumPrediction.exception import customexception
from dataclasses import dataclass
from src.HealthInsurancePremiumPrediction.utils.utils import save_object
from src.HealthInsurancePremiumPrediction.utils.utils import evaluate_model
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LinearRegression, Ridge,Lasso,ElasticNet
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score


@dataclass 
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts','model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_training(self,train_arr,test_arr):
        try:
            logging.info("Splitting independent and dependent variables from train and test data")
            x_train, y_train, x_test, y_test = (
                train_arr[:,:-1],
                train_arr[:,-1],
                test_arr[:,:-1],
                test_arr[:,-1]
            )

            models={
            'Linear Regression':LinearRegression(),
            'Lasso':Lasso(),
            'Ridge':Ridge(),
            #'Elasticnet':ElasticNet(),
            'DecisionTree Regressor':DecisionTreeRegressor(),
            'RandomForest Regressor':RandomForestRegressor(),
            'GradientBoosting Regressor': GradientBoostingRegressor()

        }
            params={
                "Linear Regression":{},
                "Lasso":{
                    'alpha': [0.1,0.5,1,1.5,2]
                },
                "Ridge" : {
                    'alpha': [0.1,0.5,1,1.5,2]
                },
                "DecisionTree Regressor" : {
                    'max_depth' : [4,6,8,9,10,12],
                    
                },
                "RandomForest Regressor" : {
                    'n_estimators': [10,20,30,50,80,100],
                     'max_depth' : [8,9,10,12]
                },
                "GradientBoosting Regressor" : {
                    'n_estimators': [10,20,30,50,100],
                    'learning_rate' : [0.01,0.05,0.1,0.5,1]
                }

            }

            model_report:dict = evaluate_model(x_train, y_train, x_test, y_test, models, params)
            best_model_label = max(model_report,key = lambda x : model_report[x])
            best_model_score = model_report[best_model_label]
            best_model = models[best_model_label]

            if best_model_score<0.6:
                raise CustomException("No best model found")
            logging.info(f"Best found model on both training and testing dataset")

            print(f'Best Model Found , Model Name : {best_model}, R2 Score : {best_model_score}')
            print('\n====================================================================================\n')
            logging.info(f'Best Model Found , Model Name : {best_model} , R2 Score : {best_model_score}')

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

        except Exception as e:
            logging.info("Exception occured during model training")
            raise customexception(e,sys)
