import sys
from reactorexplorer.logger.log import logging
from reactorexplorer.pipeline.training_pipeline import DataIngestionTrainingPipeline, DataValidationTrainingPipeline, DataTransformationTrainingPipeline, ModelTrainerTrainingPipeline
from reactorexplorer.exception.exception_handler import AppException



try:
    STAGE_NAME = "Data Ingestion Stage"
    # Step 01 Data Ingestion
    logging.info(f">>> State {STAGE_NAME} started <<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logging.info(f">>> State {STAGE_NAME} completed <<<\n")

    STAGE_NAME = "Data Validation Stage"
    # Step 02 Data Validation
    logging.info(f">>> State {STAGE_NAME} started <<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logging.info(f">>> State {STAGE_NAME} completed <<<\n")

    STAGE_NAME = "Data Transformation Stage"
    # Step 03 Data Transformation
    logging.info(f">>> State {STAGE_NAME} started <<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logging.info(f">>> State {STAGE_NAME} completed <<<\n")

    STAGE_NAME = "Model Training Stage"
    # Step 04 Model Training
    logging.info(f">>> State {STAGE_NAME} started <<<")
    model_training = ModelTrainerTrainingPipeline()
    model_training.main()
    logging.info(f">>> State {STAGE_NAME} completed <<<\n")
    
except Exception as e:
    logging.exception(e)
    raise AppException(e, sys) from e
