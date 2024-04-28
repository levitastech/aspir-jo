# core_module.py
import os

import requests

from web_scraper import get_years_list, get_indices_list


def fetch_years():
    """
    Fetch the list of available years from the JORADP website.

    Returns:
        list: List of years (as integers)
    """
    return get_years_list()


def fetch_indices(year):
    """
    Fetch the list of available indices for a given year from the JORADP website.

    Args:
        year (int): The year for which to fetch the indices list.

    Returns:
        list: List of indices (as integers)
    """
    return get_indices_list(year)


def download_file(year, index, directory):
    """
    Download a specific PDF file from the JORADP website.

    Args:
        year (int): The year of the publication.
        index (int): The index of the publication.
        directory (str): The directory path where the file will be saved.
    """
    # Construct the URL for the PDF file
    url = f"https://www.joradp.dz/FTP/jo-francais/{year}/F{year}{index:03d}.pdf"
    filename = os.path.basename(url)
    filepath = os.path.join(directory, filename)

    # Check if the file already exists
    if os.path.exists(filepath):
        print(f"{filename} already exists. Skipping download.")
        return

    # Create the directory if it doesn't exist
    os.makedirs(directory, exist_ok=True)

    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        with open(filepath, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f"Downloaded {filename} successfully!")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading {filename}: {e}")
