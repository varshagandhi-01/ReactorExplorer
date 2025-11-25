import pytest
from reactorexplorer.components.stage_01_data_ingestion import DataIngestion
from reactorexplorer.components.stage_02_data_validation import DataValidation
from reactorexplorer.components.stage_03_data_transformation import DataTransformation
from reactorexplorer.components.stage_04_model_trainer import ModelTrainer
import pandas as pd


def test_data_ingestion_loads_file(tmp_path):
    # Create dummy CSV
    file = tmp_path / "reactors.csv"
    df = pd.DataFrame({"name": ["R1", "R2"], "country": ["A", "B"], "capacity": [100, 200]})
    df.to_csv(file, index=False)

    ingestor = DataIngestion(str(file))
    loaded = ingestor.load_data()

    assert isinstance(loaded, pd.DataFrame)
    assert len(loaded) == 2


def test_validation_schema_passes():
    df = pd.DataFrame({"name": ["R1"], "country": ["A"], "capacity": [100]})
    schema = {"name": "object", "country": "object", "capacity": "int64"}

    validator = DataValidation(schema)
    assert validator.validate(df) is True


def test_transformation_scaling():
    df = pd.DataFrame({"capacity": [100, 200, 300]})
    transformer = DataTransformation()

    scaled = transformer.scale_features(df)
    assert scaled.shape == df.shape


def test_model_trainer_trains_knn():
    df = pd.DataFrame({"capacity": [1, 2, 3, 4, 5]})
    trainer = ModelTrainer(n_neighbors=2)

    model = trainer.train(df)
    assert hasattr(model, "kneighbors")  # Basic KNN behavior
