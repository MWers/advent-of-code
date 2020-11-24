import argparse

parser = argparse.ArgumentParser(description='Run an Advent of Code program')
parser.add_argument(
    'input_file', type=str, help='the file containing input data'
)
args = parser.parse_args()

with open(args.input_file) as f:
    input_data = f.read()
