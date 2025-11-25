import os
import sys
import pandas as pd

from reactorexplorer.logger.log import logging
from reactorexplorer.exception.exception_handler import AppException
from reactorexplorer.entity.config_entity import DataValidationConfig

class DataValidation:
    def __init__(self, config = DataValidationConfig):
        try:
            self.config = config
        except Exception as e:
            raise AppException(e, sys) from e

    def validate_all_columns(self) -> bool:
        try:

            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            all_schema = self.config.all_schema.keys()

            for col in all_schema:
                if col not in all_cols:
                    logging.info(f"missing column: {col}")
                    return False
                
            logging.info(f"all columns present")
            return True
        
        except Exception as e:
           raise AppException(e, sys) from e
        
    def validate_status(self):
        try:

            is_valid = self.validate_all_columns()
            
            with open(self.config.status_file, "w") as f:
                f.write(f"validation status: {is_valid}\n")

        except Exception as e:
            raise AppException(e, sys) from e