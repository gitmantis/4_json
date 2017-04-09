import json
import sys
import os.path

def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as json_file:
        return json.load(json_file)

def pretty_print_json(data):
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))


if __name__ == '__main__':
    fpath = sys.argv[1]
    if not os.path.exists(fpath):
        print ("File '%s' not found" % (fpath)) 
        sys.exit()
 
    pretty_print_json(load_data(fpath))




