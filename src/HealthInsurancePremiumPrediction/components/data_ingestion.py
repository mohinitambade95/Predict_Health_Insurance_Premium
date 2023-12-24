import pandas as pd 
import numpy as np 
from src.HealthInsurancePremiumPrediction.logger import logging
from src.HealthInsurancePremiumPrediction.exception import customexception
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path
import os
import sys


class DataIngestionConfig:
    raw_data_path:str=os.path.join("artifacts","raw.csv")
    train_data_path:str=os.path.join("artifacts","train.csv")
    test_data_path:str=os.path.join("artifacts","test.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("data ingestion started")

        try:
            data = pd.read_csv(Path(os.path.join("notebooks/data", "data_preprocessed.csv")))
            logging.info('data stored in dataframe')
            os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data_path)),exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info("Raw data saved")

            logging.info('performing train test split')

            train_data,test_data = train_test_split(data,test_size=0.3)
            logging.info('train test split completed')

            train_data.to_csv(self.ingestion_config.train_data_path,index=False)
            test_data.to_csv(self.ingestion_config.test_data_path,index=False)
            
            logging.info("data ingestion part completed")

            return (

                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
            


        except Exception as e:
           logging.info("exception occured during data ingestion")
           raise customexception(e,sys)

