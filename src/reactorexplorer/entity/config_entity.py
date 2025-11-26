from dataclasses import dataclass
from pathlib import Path

# -------------------------------
# Configuration entity for data ingestion stage
# Stores folder paths and source URL used during dataset download/extraction
# -------------------------------
@dataclass(frozen = True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str # URL to download raw dataset
    local_data_file: Path # Path where downloaded raw file will be stored locally
    unzip_dir: Path # Directory to extract downloaded file contents

# -------------------------------
# Configuration entity for data validation stage
# Stores schema and directories used to validate ingested dataset
# -------------------------------
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    status_file: str # File to store validation status (True/False)
    unzip_data_dir: Path # Path to extracted ingested data
    all_schema: str # Name of schema file used to validate column structure

# -------------------------------
# Configuration entity for data transformation stage
# Handles cleaning, pivot table creation, and serialization of outputs used for training
# -------------------------------
@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    clean_data_dir: Path # Directory where cleaned dataset will be stored 
    serialized_objects_dir: Path # Folder to store serialized objects (pivot, names list)
    data_pivot_name: str
    data_names_name: str
    clean_data_name: str

# -------------------------------
# Configuration entity for model training stage
# Stores paths to pivot data & model files required for model training
# -------------------------------
@dataclass(frozen = True)
class ModelTrainerConfig:
    root_dir: Path
    trained_model_name: str  # File name for storing trained model pickle file
    serialized_objects_dir: Path # Directory containing serialized objects
    data_pivot_name: str # Pivot data filename
    data_names_name: str # Reactor names list filename

# -------------------------------
# Configuration entity for recommendation engine
# Used by Streamlit UI to load trained model and predictor artifacts
# -------------------------------
@dataclass(frozen = True)
class ModelRecommenderConfig:
    root_dir: Path
    trained_model_name: str  # File name of stored trained model pickle file
    serialized_objects_dir: Path # Directory containing serialized objects
    data_pivot_name: str # Pivot data filename
    data_names_name: str # Reactor names list filename