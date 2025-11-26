import os
import sys
import pickle
from sklearn.neighbors import NearestNeighbors
from scipy.sparse import csc_matrix

from reactorexplorer.logger.log import logging
from reactorexplorer.exception.exception_handler import AppException
from reactorexplorer.utils.utils import read_yaml, create_directories
from reactorexplorer.entity.config_entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self, config = ModelTrainerConfig):
        try:
            # Store model training configuration with model & data paths
            self.config = config
            self.config = config
        except Exception as e:
            raise AppException(e, sys) from e
        
    def train(self):
        """
        Train a Nearest Neighbors model on sparse pivot data using csc matrix and save the trained model.
        """
        try:
            # load pivot data
            data_pivot = pickle.load(open(os.path.join(self.config.serialized_objects_dir, self.config.data_pivot_name), "rb"))
            # Convert dataset into sparse matrix format for efficient similarity search
            data_sparse = csc_matrix(data_pivot)
            
            # Initialize Nearest Neighbors model using brute-force search
            model = NearestNeighbors(algorithm='brute')
            # Fit the model to sparse feature matrix
            model.fit(data_sparse)

            # save the trained model
            os.makedirs(self.config.root_dir, exist_ok=True)
            file_name = os.path.join(self.config.serialized_objects_dir, self.config.trained_model_name)
            pickle.dump(model, open(file_name, 'wb'))
            logging.info(f"saved model to {file_name}")
        except Exception as e:
            raise AppException(e, sys) from e 
