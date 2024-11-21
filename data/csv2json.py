#!/usr/bin/env python3
import csv
import json
import argparse
import sys
import os

class OutputWrapper:
    def __init__(self, filename=None, encoding="utf-8"):
        if filename:
            self.output = open(filename, mode='w', encoding=encoding)
        else:
            self.output = sys.stdout

    def write(self, message):
        self.output.write(message)

    def writelines(self, lines):
        self.output.writelines(lines)

    def close(self):
        if self.output is not sys.stdout:
            self.output.close()
            
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

def csv_to_json(csv_file_path, json_file_path, dict_key=None, pop_key=False):
    data = []
    with open(csv_file_path, mode='r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.DictReader(csv_file)
    
        for row in csv_reader:
            data.append(row)

    with OutputWrapper(json_file_path, encoding='utf-8-sig') as json_file:
        if dict_key:
            jo = {}
            for row in data:
                if pop_key:
                    key = row.pop(dict_key)
                    jo[key]=row
                else:
                    jo[row[dict_key]]=row                
            json.dump(jo, json_file, indent=4)
        else:
            json.dump(data, json_file, indent=4)

def csv_to_json_ext(filename):
    if filename.endswith('.csv'):
        return filename[:-4] + '.json'
    else:
        return filename + '.json'

def main():
    parser = argparse.ArgumentParser(description='Convert CSV to JSON')
    parser.add_argument('csv_file', help='Path to the input CSV file')
    parser.add_argument('json_file', nargs='?', help='Path to the output JSON file. Overrides -j/--auto-json')
    parser.add_argument('-j', '--auto-json', action='store_true', help='Automatically replace the .csv extension with .json')
    parser.add_argument('-d', '--dictkey',action='store', nargs=1, help='Create a JSON object instead of a JSON array')
    parser.add_argument('-p', '--popkey',action='store_true', help='Pop the key from each JSON sub object. Only meaningful with -d/--dictkey')
    parser.add_argument('-o', '--overwrite',action='store_true', help='Overwrite the output file if it exists')
    args = parser.parse_args()

    if args.popkey and not args.dictkey:
        print("Warning: -p/--popkey is only meaningful with -d/--dictkey. See --help.", file=sys.stderr)
    if args.json_file and args.auto_json:
        print("Warning: Specified json_file overrides -j/--auto-json. See --help.", file=sys.stderr)

    if not args.csv_file:
        print("Error: You must specify a CSV file", file=sys.stderr)
        parser.print_help()
        return
    
    csv_name = args.csv_file
    if not os.path.isfile(csv_name) and not csv_name.endswith('.csv') and os.path.isfile(csv_name + '.csv'):
        csv_name += '.csv'    
        print(f'Info: Auto appended ".csv" extension to "{csv_name}".', file=sys.stderr)
    
    json_name = args.json_file if args.json_file else csv_to_json_ext(args.csv_file) if args.auto_json else None
    if json_name and os.path.isfile(json_name) and not args.overwrite:
        print(f"Error: Output file '{json_name}' already exists", file=sys.stderr)
        return
    
    dict_key = args.dictkey[0] if args.dictkey else None
    csv_to_json(csv_name, json_name, dict_key, args.popkey)

if __name__ == '__main__':
    main()