import sys
from reactorexplorer.logger.log import logging
from reactorexplorer.pipeline.training_pipeline import DataIngestionTrainingPipeline
from reactorexplorer.exception.exception_handler import AppException

STAGE_NAME = "Data Ingestion Stage"

try:
    logging.info(f">>> State {STAGE_NAME} started <<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logging.info(f">>> State {STAGE_NAME} completed <<<\n")
    
except Exception as e:
    logging.exception(e)
    raise AppException(e, sys) from e
