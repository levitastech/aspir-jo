import sys

from cli_module import parse_arguments
from downloader import *
from file_manager import *
from web_scraper import *


def main():
    """
    Main entry point of the application.
    """
    args = parse_arguments()

    # Handle the --version argument
    if args.version:
        print("joradp Downloader Ver 2.5.1 Copyright 2023")
        sys.exit(0)

    # Set the base directory for downloads
    base_dir = Path.home() / "joradp"

    # Handle the --directories argument
    use_directories = args.directories

    try:
        # Fetch the list of available years
        years = get_years_list()

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

                download_file(year, index, destination_dir)
            else:
                # Download all publications for the specified year
                for index in indices:
                    download_file(year, index, destination_dir)

        else:
            # Download all publications for all available years
            for year in years:
                indices = get_indices_list(year)
                destination_dir = get_destination_dir(str(base_dir), year, use_directories)
                for index in indices:
                    download_file(year, index, destination_dir)

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
