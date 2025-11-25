import sys 
from reactorexplorer.components.stage_01_data_ingestion import DataIngestion
from reactorexplorer.components.stage_02_data_validation import DataValidation
from reactorexplorer.components.stage_03_data_transformation import DataTransformation
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