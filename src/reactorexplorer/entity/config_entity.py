from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen = True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    status_file: str
    unzip_data_dir: Path
    all_schema: str

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    clean_data_dir: Path
    serialized_objects_dir: Path
    data_pivot_name: str
    data_names_name: str
    clean_data_name: str
