import argparse


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
