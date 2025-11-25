import sys
from reactorexplorer.constants import *
from reactorexplorer.utils.utils import read_yaml, create_directories
from reactorexplorer.exception.exception_handler import AppException
from reactorexplorer.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig

class ConfigurationManager:
    def __init__ (
            self,
            config_file_path = CONFIG_FILE_PATH,
            params_file_path = PARAMS_FILE_PATH,
            schema_file_path = SCHEMA_FILE_PATH):
        try:
            self.config = read_yaml(CONFIG_FILE_PATH)
            self.paramls = read_yaml(PARAMS_FILE_PATH)
            self.schema = read_yaml(SCHEMA_FILE_PATH)

            create_directories([self.config.artifacts_root])

        except Exception as e:
            raise AppException(e, sys) from e 
        
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        try:
            config = self.config.data_ingestion
            create_directories([config.root_dir])

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
        try:
            config = self.config.data_validation
            schema = self.schema.COLUMNS

            create_directories([config.root_dir])

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
        try:
            config = self.config.data_transformation

            create_directories([config.root_dir])

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
        try:
            config = self.config.model_trainer

            create_directories([config.root_dir])

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
        