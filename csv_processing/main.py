#!/usr/bin/env python3


from csv_processing.cli import accept_input_parameters
from csv_processing.src.parser import read_csv


def main():
    parameters = accept_input_parameters()
    print(
        parameters.file_path,
        parameters.where,
        parameters.aggregate
    )
    print(read_csv(parameters.file_path))


if __name__ == "__main__":
    main()
