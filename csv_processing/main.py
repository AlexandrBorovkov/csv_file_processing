#!/usr/bin/env python3


from tabulate import tabulate

from csv_processing.src.cli import accept_input_parameters
from csv_processing.src.core import process_the_file


def main():
    parameters = accept_input_parameters()
    result = process_the_file(
        parameters.file_path,
        parameters.where,
        parameters.aggregate
    )
    if isinstance(result, dict):
        print(tabulate([result], headers="keys", tablefmt="grid"))
    elif isinstance(result, list):
        print(tabulate(result, headers="keys", tablefmt="grid"))
    else:
        print('Данные не найдены')


if __name__ == "__main__":
    main()
