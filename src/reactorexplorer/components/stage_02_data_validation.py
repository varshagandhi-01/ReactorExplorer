import os
import sys
import pandas as pd

from reactorexplorer.logger.log import logging
from reactorexplorer.exception.exception_handler import AppException
from reactorexplorer.entity.config_entity import DataValidationConfig

class DataValidation:
    def __init__(self, config = DataValidationConfig):
        try:
            # Store the configuration object which contains schema, file paths, etc
            self.config = config
        except Exception as e:
            raise AppException(e, sys) from e

    def validate_all_columns(self) -> bool:
        """
        Validate whether all columns defined in the schema are present in the dataset.
        Returns True if valid, otherwise False.
        """
            
        try:
            data = pd.read_csv(self.config.unzip_data_dir)
            # Get actual column names from dataset
            all_cols = list(data.columns)
            # Get expected column names from schema configuration
            all_schema = self.config.all_schema.keys()
            # Validate each required column
            for col in all_schema:
                if col not in all_cols:
                    # Log missing column and return validation failure
                    logging.info(f"missing column: {col}")
                    return False
            
            # If all columns exist, log success and return True    
            logging.info(f"all columns present")
            return True
        
        except Exception as e:
           raise AppException(e, sys) from e
        
    def validate_status(self):
        """
        Write validation result to an output file.
        """
        try:
            # Perform schema validation
            is_valid = self.validate_all_columns()
            
            # Record validation status in status output file
            with open(self.config.status_file, "w") as f:
                f.write(f"validation status: {is_valid}\n")

        except Exception as e:
            raise AppException(e, sys) from e