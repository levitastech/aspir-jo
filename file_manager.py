# file_manager.py
import os
from pathlib import Path


def create_directories(base_dir, use_directories):
    """
    Create directories for each year if the `use_directories` option is enabled.

    Args:
        base_dir (str): The base directory path.
        use_directories (bool): Whether to create separate directories for each year.

    Returns:
        str: The directory path to be used for saving files.
    """
    if use_directories:
        base_dir = Path(base_dir)
        base_dir.mkdir(parents=True, exist_ok=True)
        return str(base_dir)
    else:
        return base_dir


def get_destination_dir(base_dir, year, use_directories):
    """
    Get the destination directory path for a specific year.

    Args:
        base_dir (str): The base directory path.
        year (int): The year for which to get the destination directory.
        use_directories (bool): Whether to create separate directories for each year.

    Returns:
        str: The destination directory path.
    """
    base_dir = create_directories(base_dir, use_directories)

    if use_directories:
        year_dir = os.path.join(base_dir, str(year))
        os.makedirs(year_dir, exist_ok=True)
        return year_dir
    else:
        return base_dir
