from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation,DataValidationConfig
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
import sys

if __name__ == "__main__":
    try:
        logging.info('data ingestion initiated')
        trainingpiplelineconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpiplelineconfig)
        data_ingestion = DataIngestion(dataingestionconfig)
        dataingestionartifact = data_ingestion.initiate_data_ingestion()
        logging.info('data validation initiated')
        datavalidationconfig = DataValidationConfig(trainingpiplelineconfig)
        data_validation = DataValidation(dataingestionartifact,datavalidationconfig)
        datavalidationartifact = data_validation.initiate_data_validation()
        print(dataingestionartifact)
        print(datavalidationartifact)
    except Exception as e:
        raise NetworkSecurityException(e,sys)
