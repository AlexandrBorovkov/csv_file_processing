import json

from csv_processing.src.core import process_the_file


def test_process_the_file_incorrect_input():
    assert process_the_file(
        'tests/fixtures/no_name.csv',
        'price>500',
        'price=avg'
    ) is None
    assert process_the_file(
        'tests/fixtures/products.csv',
        'price>>500',
        'price=avg'
    ) is None
    assert process_the_file(
        'tests/fixtures/products.csv',
        'price>500',
        'price==avg'
    ) is None

def test_filter_aggregate_data():
    with open('tests/fixtures/products1.json') as file:
        data = json.load(file)
    assert process_the_file(
        'tests/fixtures/products.csv',
        'price>500',
        'price=avg'
    ) == data

def test_filter_the_data():
    with open('tests/fixtures/products2.json') as file:
        data = json.load(file)
    assert process_the_file(
        'tests/fixtures/products.csv',
        'brand=apple',
        None
    ) == data

def test_aggregate_data():
    with open('tests/fixtures/products3.json') as file:
        data = json.load(file)
    assert process_the_file(
        'tests/fixtures/products.csv',
        None,
        'price=max'
    ) == data
