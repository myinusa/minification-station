import logging
from typing import TYPE_CHECKING

from minification_station.config.args import get_parsed_args
from minification_station.config.enviornment_setup import initialize_application
from minification_station.processing.file_processor import FileProcessor
from minification_station.traversal.directory_traversal import DirectoryTraversal

if TYPE_CHECKING:
    from argparse import Namespace


def log_progress(index: int, total: int, message: str) -> None:
    """Log progress with index and total count."""
    logging.info(f"[{index}/{total}] {message}")


def main() -> None:
    args: Namespace = get_parsed_args()
    initialize_application()

    directory = args.directory
    output_file = args.output

    logging.info(
        f"Starting the script with directory: {directory} and output file: {output_file}",
    )

    try:
        traversal = DirectoryTraversal(directory=directory)
        file_paths = traversal.get_files()
        total_files = len(file_paths)
        logging.info(f"Total number of files to process: {total_files}")

        processor = FileProcessor(output_file=output_file)
        for index, file_path in enumerate(iterable=file_paths, start=1):
            processor.process_file(file_path)
            log_progress(index, total_files, message=f"Processed file: {file_path}")

        logging.info(f"Combined file written to {output_file}")
    except Exception:
        logging.exception("An error occurred")


if __name__ == "__main__":
    main()
