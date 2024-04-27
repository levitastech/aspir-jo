import sys

from cli_module import parse_arguments
from downloader import *
from file_manager import *
from web_scraper import get_years_list, get_indices_list

__version__ = ""


def main():
    """
    Main entry point of the application.
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
    print(f"Python joradp Downloader Ver {__version__} Copyright 2023-2024")
    # print(" Python joradp Downloader Ver 2.6.1 Copyright 2023-2024")


if __name__ == "__main__":
    with open('VERSION') as version_file:
        __version__ = version_file.read().strip()
    main()
