import datetime
import re

import requests


def get_years_list():
    """
    Fetch the list of available years from the JORADP website.

    Returns:
        list: List of years (as integers)
    """

    url = "https://www.joradp.dz/JRN/ZF1962.htm"
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code != 200:
        raise Exception(f"Failed to fetch years list (status code: {response.status_code})")

    html_content = response.text

    # Find all <option> tags within <select> tags and extract the years

    # Extract years using regex pattern matching
    year_pattern = r'<option[^>]*>(\d{4})'  # r'<option[^>]*>(\d{4})</option>'
    year_options = re.findall(year_pattern, html_content)

    # Check if the year_options list is empty
    if year_options:
        # Convert extracted years to integers
        years = [int(year) for year in year_options]
        years = list(reversed(years))
    else:
        years = list(range(1962, datetime.datetime.now().year + 1))

    return years


def get_indices_list(year):
    """
    Fetch the list of available indices for a given year from the JORADP website.

    Args:
        year (int): The year for which to fetch the indices list.

    Returns:
        list: List of indices (as integers)
    """
    url = f"https://www.joradp.dz/JRN/ZF{year}.htm"
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code != 200:
        raise Exception(f"Failed to fetch indices list for year {year} (status code: {response.status_code})")

    html_content = response.text

    # Extract indices using regex pattern matching
    index_pattern = r'\">([0-9]{2,3})'
    indices = re.findall(index_pattern, html_content)

    # reverse order
    indices = list(reversed(indices))

    # ++++++ unnecessary step  , formatted in download_file()
    # Format indices as strings with 3-character format (e.g., '001', '002', ..., '099', '100', ...)
    # indices = [index.zfill(3) for index in indices]

    # Convert extracted indices to integers
    indices = [int(index) for index in indices]

    return indices
