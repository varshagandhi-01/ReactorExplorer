import os
import sys
import pickle
import streamlit as st
import numpy as np
from reactorexplorer.logger.log import logging
from reactorexplorer.exception.exception_handler import AppException
from reactorexplorer.config.configuration import ConfigurationManager
from reactorexplorer.pipeline.training_pipeline import TrainingPipeline

class Recommendation:

    def __init__(self, config = ConfigurationManager()):
        """
        Initialize Recommendation class with configuration values.
        Loads the recommendation configuration using ConfigurationManager.
        """
        try:
            self.config = config.get_recommendation_config()

        except Exception as e:
            raise AppException(e, sys) from e 
        
    def train_engine(self):
        """
        Runs the full training pipeline and displays success message.
        executed via Streamlit 'Train' button.
        """
        try:
            obj = TrainingPipeline()
            obj.start_training_pipeline()
            st.text("Training completed")
            logging.info(f"Model Trained")

        except Exception as e:
            raise AppException(e, sys) from e            
        
    def match_reactor(self, reactor_name):
        """
        Finds similar reactors using the trained NearestNeighbors model.
        
        Args:
            reactor_name (str): selected reactor name from dropdown
            
        Returns:
            list: List of recommended similar reactors
        """
        try:
            reactor_list = []
            # Load trained model from pickle file
            model = pickle.load(open(os.path.join(self.config.root_dir, self.config.trained_model_name), 'rb'))
             # Load pivot table used during training
            data_pivot = pickle.load(open(os.path.join(self.config.serialized_objects_dir, self.config.data_pivot_name), 'rb'))
            # Locate the row index of selected reactor
            data_id = np.where(data_pivot.index == reactor_name)[0][0]

            # Get nearest neighbors (first one will always be itself)
            distance, suggestion = model.kneighbors(data_pivot.iloc[data_id,:].values.reshape(1, -1), n_neighbors = 10)

            reactor_list = []
            # Extract matched reactor names from row indices
            for i in range(len(suggestion)):
                reactor_matches = data_pivot.index[suggestion[i]]
                for j in reactor_matches:
                    reactor_list.append(j)

            return reactor_list
        
        except Exception as e:
            raise AppException(e, sys) from e 
        
    def recommender_engine(self, selected_reactor):
        """
        Displays the top 5 recommended reactors in a row of Streamlit columns.
        """
        try:
            matched_reactors = self.match_reactor(selected_reactor)
            match1, match2, match3, match4, match5 = st.columns(5)

            with match1:
                st.text(matched_reactors[1])
            with match2:
                st.text(matched_reactors[2])
            with match3:
                st.text(matched_reactors[3])
            with match4:
                st.text(matched_reactors[4])
            with match5:
                st.text(matched_reactors[5])

        except Exception as e:
            raise AppException(e, sys) from e

# Streamlit app entry point
if __name__ == "__main__":
    st.header("Find reactors with similar capacity")
    obj = Recommendation() 
    
    # Button to initiate model training
    if st.button("Train"):
        obj.train_engine()

    # Load reactor names for dropdown selection
    reactor_names = pickle.load(open(os.path.join(obj.config.serialized_objects_dir, obj.config.data_names_name), 'rb'))
    # Dropdown selector for choosing reactor name
    selected_reactor = st.selectbox(
    "Type or select a reactor from the dropdown to see your recommendations", reactor_names)

    # Get recommendations on button press
    if st.button("Find matches"):
        obj.recommender_engine(selected_reactor)

                            
    
