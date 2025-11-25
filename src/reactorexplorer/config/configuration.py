import sys
from reactorexplorer.constants import *
from reactorexplorer.utils.utils import read_yaml, create_directories
from reactorexplorer.exception.exception_handler import AppException
from reactorexplorer.entity.config_entity import DataIngestionConfig

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