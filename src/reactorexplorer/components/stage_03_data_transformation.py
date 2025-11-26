import os
import sys
import ast
import pandas as pd
import pickle

from reactorexplorer.logger.log import logging
from reactorexplorer.exception.exception_handler import AppException
from reactorexplorer.utils.utils import read_yaml, create_directories
from reactorexplorer.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config = DataTransformationConfig):
        try:
            # Store the transformation configuration containing paths and file names
            self.config = config 
          
        except Exception as e:
            raise AppException(e, sys) from e


    def transform_data(self):
        """
        Performs data cleaning, filtering, pivoting and saves outputs 
        in both CSV and serialized pickle formats.
        """
        try:
            # Read the raw dataset
            raw_data = pd.read_csv(self.config.data_path, on_bad_lines='skip', encoding='latin-1')

            logging.info(f"shape of raw_data: {raw_data.shape}")

            # perform requisite data transformations
            # Select only the required columns
            raw_data = raw_data[['country','country_long','name','capacity_mw', 'latitude', 'longitude', 'primary_fuel']]
            # Filter only nuclear power plants
            raw_data = raw_data[raw_data['primary_fuel'].isin(['Nuclear']) ]
            # Remove duplicated plant names
            clean_data = raw_data.drop_duplicates(['name'])

            logging.info(f"shape of clean data: {clean_data.shape}")
            
            # Create a pivot table: rows=plant name, column=primary fuel, values=capacity
            data_pivot = clean_data.pivot(columns = 'primary_fuel', index = 'name', values = 'capacity_mw')
            # Replace NaN values with 0
            data_pivot.fillna(0, inplace= True)
            # Extract nuclear plant names list
            data_names = data_pivot.index
   
            # save the transformed dataset to csv format
            os.makedirs(self.config.clean_data_dir, exist_ok = True)
            clean_data.to_csv(os.path.join(self.config.clean_data_dir, 'clean_data.csv'), index = True)
            data_pivot.to_csv(os.path.join(self.config.clean_data_dir, 'data_pivot.csv'), index = True)

            logging.info(f"clean data saved to : {self.config.clean_data_dir}")

            # save the clean data as a serialized object useful for fast loading in ML pipelines
            os.makedirs(self.config.serialized_objects_dir, exist_ok=True)
            pickle.dump(clean_data, open(os.path.join(self.config.serialized_objects_dir, self.config.clean_data_name), 'wb'))
            pickle.dump(data_pivot, open(os.path.join(self.config.serialized_objects_dir, self.config.data_pivot_name), 'wb'))
            pickle.dump(data_names, open(os.path.join(self.config.serialized_objects_dir, self.config.data_names_name), 'wb'))
            logging.info(f"saved clean data serialized object to {self.config.serialized_objects_dir}")

          
        except Exception as e:
            raise AppException(e, sys) from e