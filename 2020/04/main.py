import argparse
import re
from typing import List

parser = argparse.ArgumentParser(description='Run an Advent of Code program')
parser.add_argument(
    'input_file', type=str, help='the file containing input data'
)
args = parser.parse_args()

input_data: List = []
with open(args.input_file) as f:
    input_data = [line for line in f.read().splitlines()]


def parse_passports(input_data):
    record = {}
    records = []
    for line in input_data:
        # New record?
        if line == '' and record:
            records.append(record)
            record = {}
            continue

        for field in line.split(' '):
            key, value = field.split(':')
            record[key] = value

    # Add the last record to records
    if record:
        records.append(record)

    return records


def is_valid_passport(passport, strict_validation=False):
    required_keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    if not required_keys.issubset(set(passport.keys())):
        return False

    if strict_validation:
        byr = int(passport['byr'])
        if byr < 1920 or byr > 2002:
            return False

        iyr = int(passport['iyr'])
        if iyr < 2010 or iyr > 2020:
            return False

        eyr = int(passport['eyr'])
        if eyr < 2020 or eyr > 2030:
            return False

        hgt = passport['hgt']
        hgt_value = int(hgt.replace('cm', '').replace('in', ''))
        if 'cm' in hgt:
            if hgt_value < 150 or hgt_value > 193:
                return False
        elif 'in' in hgt:
            if hgt_value < 59 or hgt_value > 76:
                return False
        else:
            return False

        if not re.search(r"^#[0-9a-f]{6}$", passport['hcl']):
            return False

        if passport['ecl'] not in [
            'amb',
            'blu',
            'brn',
            'gry',
            'grn',
            'hzl',
            'oth',
        ]:
            return False

        if not re.search(r"^[0-9]{9}$", passport['pid']):
            return False

    return True


passports = parse_passports(input_data)

valid_passports = [
    passport for passport in passports if is_valid_passport(passport)
]

print(f'Part 1: {len(valid_passports)}')

strict_valid_passports = [
    passport
    for passport in passports
    if is_valid_passport(passport, strict_validation=True)
]

print(f'Part 2: {len(strict_valid_passports)}')
