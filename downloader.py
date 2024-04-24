import os

import requests


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
