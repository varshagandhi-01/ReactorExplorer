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
            self.config = config
        except Exception as e:
            raise AppException(e, sys) from e
    
    def download_file(self):
        try:
            if not os.path.exists(self.config.local_data_file):
                filename, headers = request.urlretrieve(
                    url = self.config.source_url,
                    filename = self.config.local_data_file
                )

                logging.info(f"file downloaded: {self.config.local_data_file}")
            else:
                logging.info(f"file already exists")

        except Exception as e:
            raise AppException(e, sys) from e 

    def extract_zip_file(self):
        try:
            unzip_path = self.config.unzip_dir
            os.makedirs(unzip_path, exist_ok=True)
            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
          
        except Exception as e:
            raise AppException(e, sys) from e 