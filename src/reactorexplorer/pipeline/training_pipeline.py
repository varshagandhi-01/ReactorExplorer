import os
import sys 
import numpy as np
import pickle
from reactorexplorer.components.stage_01_data_ingestion import DataIngestion
from reactorexplorer.components.stage_02_data_validation import DataValidation
from reactorexplorer.components.stage_03_data_transformation import DataTransformation
from reactorexplorer.components.stage_04_model_trainer import ModelTrainer
from reactorexplorer.config.configuration import ConfigurationManager
from reactorexplorer.logger.log import logging
from reactorexplorer.exception.exception_handler import AppException

# Data Ingestion Stage 
# Fetch the data from the website. Extract csv file from the downloaded zip file

class DataIngestionTrainingPipeline:
    def __init__ (self):
        pass

    def main (self):
        try:
            logging.info(f"Data ingestion initiated\n")
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config = data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
            logging.info(f"Data ingestion completed\n")
        except Exception as e:
            raise AppException(e, sys) from e

# Data Validation Stage 
# Validate the csv file is as per the expected schema

class DataValidationTrainingPipeline:
    def __init__ (self):
        pass

    def main (self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(config = data_validation_config)
            data_validation.validate_status()

        except Exception as e:
            raise AppException(e, sys) from e 
        
# Data Transformation Stage 
# Prepare the datasets for model training. Data Pivot and Data names
class DataTransformationTrainingPipeline:
    def __init__ (self):
        pass

    def main (self):
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(config = data_transformation_config)
            data_transformation.transform_data()

        except Exception as e:
            raise AppException(e, sys) from e
        
class ModelTrainerTrainingPipeline:
    def __init__ (self):
        pass

    def main (self):
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer = ModelTrainer(config = model_trainer_config)
            model_trainer.train()

            model = pickle.load(open(os.path.join(model_trainer_config.serialized_objects_dir, model_trainer_config.trained_model_name), 'rb'))
            book_pivot = pickle.load(open(os.path.join(model_trainer_config.serialized_objects_dir, model_trainer_config.data_pivot_name), 'rb'))
            book_id = np.where(book_pivot.index == 'Kanupp')[0][0]
            distance, suggestion = model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1, -1), n_neighbors = 10)

        except Exception as e:
            raise AppException(e, sys) from e 