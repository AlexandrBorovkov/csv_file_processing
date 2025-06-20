import argparse


def accept_input_parameters():
    parser = argparse.ArgumentParser(description='CSV file processing.')
    parser.add_argument('file_path')
    parser.add_argument(
        '--where',
        help='Filter condition "rating>4.7"',
        default=None
    )
    parser.add_argument(
        '--aggregate',
        help='Aggregation condition "rating=avg"',
        default=None
    )
    return parser.parse_args()
