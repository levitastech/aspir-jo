import requests
from bs4 import BeautifulSoup


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

    soup = BeautifulSoup(response.content, "html.parser")

    # Find all <option> tags within <select> tags and extract the years
    year_options = soup.select("select > option")
    years = [int(option.text) for option in year_options if option.text.isdigit()]

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

    soup = BeautifulSoup(response.content, "html.parser")

    # Find all indices within <a> tags and extract the indices
    index_links = soup.select("a[href^='FTP/jo-francais/']")
    indices = [int(link.text.split("F")[1][:3]) for link in index_links]

    return indices
