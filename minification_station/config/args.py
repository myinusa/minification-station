import argparse
import sys


def get_parsed_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Process files in a directory and combine them into a single output file.",
    )
    parser.add_argument("-d", "--directory", required=True, help="Directory to traverse")
    parser.add_argument("-o", "--output", required=True, help="Output file path")

    return parser.parse_args()
