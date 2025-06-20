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

def process_the_file(file_path, filter_condition, aggregate_condition):
    data = get_file_data(file_path)
    if data is None:
        return None
    if filter_condition and aggregate_condition:
        filtered_data = filter_the_data(data, filter_condition)
        aggregation_result = aggregate_data(filtered_data, aggregate_condition)
        return aggregation_result
    elif filter_condition:
        filtered_data = filter_the_data(data, filter_condition)
        return filtered_data
    elif aggregate_condition:
        aggregation_result = aggregate_data(data, aggregate_condition)
        return aggregation_result
    else:
        return data
