import csv

from csv_processing.src.aggregation import aggregate_data
from csv_processing.src.filtering import filter_the_data


def get_file_data(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except FileNotFoundError:
        return None

def process_the_file(parameters):
    data = get_file_data(parameters.file_path)
    if data is None:
        return 'Файл не найден'
    if parameters.where and parameters.aggregate:
        filtered_data = filter_the_data(data, parameters.where)
        aggregation_result = aggregate_data(filtered_data, parameters.aggregate)
        return aggregation_result
    elif parameters.where:
        filtered_data = filter_the_data(data, parameters.where)
        return filtered_data
    elif parameters.aggregate:
        aggregation_result = aggregate_data(data, parameters.aggregate)
        return aggregation_result
    else:
        return data
