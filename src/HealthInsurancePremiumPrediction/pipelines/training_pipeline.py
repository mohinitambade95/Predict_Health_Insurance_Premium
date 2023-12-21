from src.HealthInsurancePremiumPrediction.components.data_ingestion import DataIngestion
from src.HealthInsurancePremiumPrediction.logger import logging
from src.HealthInsurancePremiumPrediction.exception import customexception
import pandas as pd
import os
import sys

obj=DataIngestion()
obj.initiate_data_ingestion()