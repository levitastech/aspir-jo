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
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "-y",
        "--year",
        type=int,
        help="Download all publications for the given year (valid years: 1962-current year)",
    )
    group.add_argument(
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

    return parser.parse_args()
