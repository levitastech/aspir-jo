# cli_module.py
import argparse
import sys

from downloader import *
from file_manager import *
# from main import __version__
from web_scraper import get_years_list, get_indices_list

#__version__ = ""


def parse_arguments():
    """
    Parse command-line arguments using the argparse module.

    Returns:
        argparse.Namespace: Parsed arguments
    """
    parser = argparse.ArgumentParser(
        description="Download PDF files from the JORADP website."
    )

    # Mutually exclusive group for the main actions
    parser.add_argument(
        "-y",
        "--year",
        type=int,
        help="Download all publications for the given year (valid years: 1962-current year)",
    )

    # Index argument (requires --year)
    parser.add_argument(
        "-i",
        "--index",
        type=int,
        help="Download a specific publication index for the given year (requires --year)",
    )
    # Optional arguments
    parser.add_argument(
        "-d",
        "--directories",
        action="store_true",
        help="Create separate directories for each year",
    )

    parser.add_argument(
        "-v",
        "--version",
        action="store_true",
        help="Display script name, version, and copyright",
    )

    args = parser.parse_args()

    # Validate the combination of --year and --index arguments
    if args.index and not args.year:
        parser.error("The --index argument requires the --year argument.")

    return args


def main():
    """
    Main entry point of the application for the command-line interface.
    """

    print_ver()
    args = parse_arguments()

    # Handle the --version argument
    if args.version:
        sys.exit(0)

    # Set the base directory for downloads
    base_dir = Path.home() / "Documents" / "joradp"

    # Handle the --directories argument
    use_directories = args.directories

    try:
        # Fetch the list of available years
        years = get_years_list()

        # Check if the years list is empty
        if not years:
            print("Error: No years found on the website.")
            sys.exit(1)

        if args.year:
            # Download publications for a specific year
            year = args.year
            if year not in years:
                print(f"Error: {year} is not a valid year (valid years: {min(years)}-{max(years)})")
                sys.exit(1)

            indices = get_indices_list(year)
            destination_dir = get_destination_dir(str(base_dir), year, use_directories)

            if args.index:
                # Download a specific publication index
                index = args.index
                if index not in indices:
                    print(f"Error: Index {index} is not valid for year {year}")
                    sys.exit(1)

                print(f"Download directory ... {destination_dir}")
                download_file(year, index, destination_dir)
            else:
                # Download all publications for the specified year
                print(f"Download directory ... {destination_dir}")
                for index in indices:
                    download_file(year, index, destination_dir)

        else:
            # Download all publications for all available years
            for year in years:
                indices = get_indices_list(year)
                destination_dir = get_destination_dir(str(base_dir), year, use_directories)
                print(f"Download directory ... {destination_dir}")
                for index in indices:
                    download_file(year, index, destination_dir)

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


def print_ver():
    with open('VERSION') as version_file:
        __version__ = version_file.read().strip()
    print(f"Python joradp Downloader Ver {__version__} Copyright 2023-2024")
