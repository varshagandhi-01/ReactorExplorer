import os
import sys
from box.exceptions import BoxValueError
import yaml
from reactorexplorer.logger.log import logging
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from reactorexplorer.exception.exception_handler import AppException

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a YAML file and returns its contents as a ConfigBox object.

    Args:
        path_to_yaml (Path): The path to the YAML file.
    Returns:
        ConfigBox: The contents of the YAML file as a ConfigBox object.
    Raises:
        BoxValueError: If there is an error reading the YAML file.
    """

    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logging.info(f"YAML file {path_to_yaml} read successfully.")
            return ConfigBox(content)
    except BoxValueError as e:
        raise ValueError(f"Error reading YAML file at {path_to_yaml}: {e}")
    except Exception as e:
        raise AppException(e, sys) from e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose = True):
    """Creates directories if they do not exist.
    Args:
        path_to_directories (list): List of directory paths to create.
        verbose (bool, optional): If True, logs the creation of directories. Defaults to True.
    """
    
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logging.info(f"created directory at {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data
    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file

    """
    with open(path, "w") as f:
        json.dump(data, f, indent = 4)

    logging.info(f"json file saved at : {path}")

@ensure_annotations
def open_json(path: Path) -> ConfigBox:
    """load json file data
    Args: 
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)
    
    logging.info(f"json file loaded successfully from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file
    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value = data, filename = path)
    logging.info(f"binary file saved at : {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data
    Args:
        path (Path): path to binary file
    Returns:
        Any: object stored in the file
    """

    data = joblib.load(path)
    logging.info("binary file loaded from : {path}")
    return data


@ensure_annotations
def get_size(path:Path) -> str:
    """get size in KB
    Arges: 
        path (Path): path of the file
    Returns:
        str: file size in KB
    """

    size_in_kb = round(os.path.getsize(path)/1024)

    return f"{size_in_kb} KB"


    