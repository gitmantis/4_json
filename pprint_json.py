import json
import sys
import os.path
from pprint import pprint

def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as json_file:
        return json.load(json_file)

def pretty_print_json(data):
    pprint(data) 


if __name__ == '__main__':
    fpath = sys.argv[1]
    pretty_print_json(load_data(fpath))




