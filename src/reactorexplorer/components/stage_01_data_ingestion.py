import os
import sys 
import urllib.request as request
import zipfile
from reactorexplorer.logger.log import logging
from reactorexplorer.exception.exception_handler import AppException
from reactorexplorer.utils.utils import get_size
from reactorexplorer.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config = DataIngestionConfig):
        try:
            # Store the configuration object, which contains paths & URLs
            self.config = config
        except Exception as e:
            raise AppException(e, sys) from e
    
    def download_file(self):
        try:
            if not os.path.exists(self.config.local_data_file):   # Check if dataset file is already downloaded to local path
                # Download file from the source URL to specified local file path
                filename, headers = request.urlretrieve(
                    url = self.config.source_url,
                    filename = self.config.local_data_file
                )

                logging.info(f"file downloaded: {self.config.local_data_file}")
            else:
                # Log if file already exists to avoid unnecessary download
                logging.info(f"file already exists")

        except Exception as e:
            raise AppException(e, sys) from e 

    def extract_zip_file(self):
        try:
            unzip_path = self.config.unzip_dir  # Directory where the zip contents will be extracted
            # Create directory - do not raise error if it already exists
            os.makedirs(unzip_path, exist_ok=True)
            # Extract zip file into the directory
            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
          
        except Exception as e:
            # Handle errors such as invalid zip or file not found
            raise AppException(e, sys) from e 