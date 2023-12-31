from src.HealthInsurancePremiumPrediction.logger import logging
from src.HealthInsurancePremiumPrediction.exception import customexception
import sys

from pymongo import MongoClient
import pandas as pd

def initiate_db_connection():
        "function to initiate mongo db connection"
        try:
            uri = "mongodb+srv://mohinitambade95:Mona123@cluster0.clgpzho.mongodb.net/?retryWrites=true&w=majority"
            client = MongoClient(uri)
            client.admin.command('ping')
            logging.info("Successfully connected to MongoDB")
            return client
        except Exception as e:
            logging.info("Error connecting to MongoDB")
            raise customexception(e,sys)
    

def get_data_from_db(database_name,collection_name):
        try:
            client = initiate_db_connection()
            collection = client[database_name][collection_name]
            data = list(collection.find())
            logging.info("Successfully fetched the data from DB")
            client.close()
            return pd.DataFrame(data)
        except Exception as e:
            logging.info("Error fetching data")
            raise customexception(e,sys)


