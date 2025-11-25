import sys 
from reactorexplorer.components.stage_01_data_ingestion import DataIngestion
from reactorexplorer.config.configuration import ConfigurationManager
from reactorexplorer.logger.log import logging
from reactorexplorer.exception.exception_handler import AppException

STAGE_NAME = "Data Ingestion Stage"

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
