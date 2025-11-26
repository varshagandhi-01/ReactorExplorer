import os 
import sys
from reactorexplorer.constants import *
from reactorexplorer.utils.utils import read_yaml, create_directories
from reactorexplorer.logger.log import logging
from reactorexplorer.exception.exception_handler import AppException
from reactorexplorer.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig, ModelRecommenderConfig

class ConfigurationManager:
    def __init__ (
            self,
            config_file_path = CONFIG_FILE_PATH,
            params_file_path = PARAMS_FILE_PATH,
            schema_file_path = SCHEMA_FILE_PATH):
        try:
            # Load YAML configuration files
            self.config = read_yaml(CONFIG_FILE_PATH)
            self.paramls = read_yaml(PARAMS_FILE_PATH)
            self.schema = read_yaml(SCHEMA_FILE_PATH)
            # Create root directory for storing all data artifacts and models
            create_directories([self.config.artifacts_root])
            logging.info(f"Artifacts created")
        except Exception as e:
            raise AppException(e, sys) from e 
        
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """
        Construct and return DataIngestionConfig using settings from config file
        """
        try:
            config = self.config.data_ingestion

            # create ingestion root directory 
            create_directories([config.root_dir])

            # Create configuration entity object for ingestion stage
            data_ingestion_config = DataIngestionConfig(
                root_dir = config.root_dir,
                source_url = config.source_url,
                local_data_file = config.local_data_file,
                unzip_dir = config.unzip_dir
            )

            return data_ingestion_config
        
        except Exception as e:
            raise AppException(e, sys) from e 
        
    def get_data_validation_config(self) -> DataValidationConfig:
        """
        Construct and return DataValidationConfig from config file
        """
        try:
            config = self.config.data_validation
            schema = self.schema.COLUMNS # Expected column schema

            create_directories([config.root_dir])
           
           # Create configuration entity object for validation stage
            data_validation_config = DataValidationConfig(
                root_dir = config.root_dir,
                status_file = config.status_file,
                unzip_data_dir = config.unzip_data_dir,
                all_schema = schema
            )

            return data_validation_config

        except Exception as e:
            raise AppException(e, sys) from e
        
    def get_data_transformation_config(self) -> DataTransformationConfig:
        """
        Build configuration for generating cleaned and pivot-transformed datasets
        """
        try:
            config = self.config.data_transformation

            create_directories([config.root_dir])

            # Create configuration entity object for transformation stage
            data_transformation_config = DataTransformationConfig(
                root_dir = config.root_dir,
                data_path = config.data_path,
                clean_data_dir = config.clean_data_dir,
                serialized_objects_dir = config.serialized_objects_dir,
                data_pivot_name = config.data_pivot_name,
                data_names_name = config.data_names_name,
                clean_data_name = config.clean_data_name
            )

            return data_transformation_config
        
        except Exception as e:
            raise AppException(e, sys) from e         
        
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        """
        Build model training configuration object
        """
        try:
            config = self.config.model_trainer

            create_directories([config.root_dir])

            # Create configuration entity object for model trianing stage
            model_trainer_config = ModelTrainerConfig(
                root_dir = config.root_dir,
                trained_model_name = config.trained_model_name,
                serialized_objects_dir = config.serialized_objects_dir,
                data_pivot_name = config.data_pivot_name,
                data_names_name = config.data_names_name
            )

            return model_trainer_config
        
        except Exception as e:
            raise AppException(e, sys) from e         
        
    def get_recommendation_config(self) -> ModelRecommenderConfig:
        """
        Build recommendation engine/ reactor matching configuration object
        """
        try:
            config = self.config.model_recommender

            # Create configuration entity object for recommendation stage
            model_recommender_config = ModelRecommenderConfig(
                root_dir = config.root_dir,
                trained_model_name = config.trained_model_name,
                serialized_objects_dir = config.serialized_objects_dir,
                data_pivot_name = config.data_pivot_name,
                data_names_name = config.data_names_name
            )
  
            return model_recommender_config

        except Exception as e:
            raise AppException(e, sys) from e 