#!/usr/bin/env python3


from csv_processing.src.cli import accept_input_parameters
from csv_processing.src.core import process_the_file


def main():
    parameters = accept_input_parameters()
    result = process_the_file(parameters)
    if not result:
        print('Данные не найдены')
    else:
        print(result)


if __name__ == "__main__":
    main()
