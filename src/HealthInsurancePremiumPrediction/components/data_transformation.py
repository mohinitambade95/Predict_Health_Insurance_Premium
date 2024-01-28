import os
import sys
import pandas as pd
import numpy as np

from dataclasses import dataclass
from src.HealthInsurancePremiumPrediction.exception import customexception
from src.HealthInsurancePremiumPrediction.logger import logging
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder,StandardScaler

from src.HealthInsurancePremiumPrediction.utils.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts','preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transformation(self):
        try:
            logging.info('Data Transformation initiated')
            cat_cols = ['sex', 'smoker', 'region']
            num_cols = ['age', 'bmi','children']

            logging.info('Data Transformation pipeline initiated')

            
            ## Numerical Pipeline
            num_pipeline=Pipeline(
                steps=[
                ('scaler',StandardScaler())
                ]
            )

            ## categorical Pipeline
            cat_pipeline=Pipeline(
                steps=[
                    ('onehot',OneHotEncoder(drop='first') ),
                    ('scaler',StandardScaler(with_mean=False))
                ]
            )

            preprocessor=ColumnTransformer([
            ('num_pipeline',num_pipeline,num_cols),
            ('cat_pipeline',cat_pipeline,cat_cols)
            ])

            return preprocessor

        except Exception as e:
            logging.info("Exception occured while creating datatransformation pipeline")

            raise customexception(e,sys)
        
    def initialize_data_transformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            
            logging.info("Reading tran and test data for data transformation")
            logging.info(f'Train Dataframe Head : \n{train_df.head().to_string()}')
            logging.info(f'Test Dataframe Head : \n{test_df.head().to_string()}')
            
            preprocessing_obj = self.get_data_transformation()
            
            target_column_name = 'expenses'
            drop_columns = [target_column_name]
            
            input_feature_train_df = train_df.drop(columns=drop_columns,axis=1)
            target_feature_train_df=train_df[target_column_name]
            
            
            input_feature_test_df=test_df.drop(columns=drop_columns,axis=1)
            target_feature_test_df=test_df[target_column_name]
            
            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)
            
            logging.info("Applying preprocessing object on training and testing datasets.")
            
            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )
            
            logging.info("preprocessing pickle file saved")
            
            return (
                train_arr,
                test_arr
            )
            
        except Exception as e:
            logging.info("Exception occured in the initiate_datatransformation")

            raise customexception(e,sys)
            
    