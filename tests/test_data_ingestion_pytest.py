import pytest
from unittest.mock import patch, MagicMock
from reactorexplorer.components.stage_01_data_ingestion import DataIngestion
from reactorexplorer.entity.config_entity import DataIngestionConfig
from reactorexplorer.exception.exception_handler import AppException
import os

@pytest.fixture
def data_ingestion_config():
    return DataIngestionConfig(
        local_data_file="test_file.zip",
        source_url="http://example.com/test_file.zip",
        unzip_dir="test_unzip_dir"
    )

@pytest.fixture
def data_ingestion(data_ingestion_config):
    return DataIngestion(config=data_ingestion_config)

@patch("os.path.exists")
@patch("urllib.request.urlretrieve")
def test_download_file(mock_urlretrieve, mock_path_exists, data_ingestion):
    # Test when file does not exist
    mock_path_exists.return_value = False
    mock_urlretrieve.return_value = ("test_file.zip", None)

    data_ingestion.download_file()
    mock_urlretrieve.assert_called_once_with(
        url=data_ingestion.config.source_url, filename=data_ingestion.config.local_data_file
    )

    # Test when file already exists
    mock_path_exists.return_value = True
    data_ingestion.download_file()
    mock_urlretrieve.assert_called_once()  # Should not call urlretrieve again

@patch("os.makedirs")
@patch("zipfile.ZipFile")
def test_extract_zip_file(mock_zipfile, mock_makedirs, data_ingestion):
    # Mock zipfile behavior
    mock_zip_instance = MagicMock()
    mock_zipfile.return_value.__enter__.return_value = mock_zip_instance

    # Call extract_zip_file
    data_ingestion.extract_zip_file()

    # Assertions
    mock_makedirs.assert_called_once_with(data_ingestion.config.unzip_dir, exist_ok=True)
    mock_zipfile.assert_called_once_with(data_ingestion.config.local_data_file, 'r')
    mock_zip_instance.extractall.assert_called_once_with(data_ingestion.config.unzip_dir)

def test_init_with_invalid_config():
    with pytest.raises(AppException):
        DataIngestion(config=None)