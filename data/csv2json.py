#!/usr/bin/env python3
# azce::csv2json.py - Arizona Edwards
# Created: 2024-11-21 14:00-EST

import csv
import json
import argparse
import sys
import os
import OutputWrapper

def is_quoted(s):
    return s.startswith('"') and s.endswith('"') or s.startswith("'") and s.endswith("'")

def csv_to_json(csv_file_path, json_file_path, dict_key=None, pop_key=False):
    data = []
    with open(csv_file_path, mode='r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        if isinstance(dict_key, int):
            dict_key_index = dict_key
            dict_key = csv_reader.fieldnames[dict_key-1]
            print(f'Info: Interpreting dict_key as field name "{dict_key}" from index {dict_key_index}.', file=sys.stderr)
        elif dict_key and dict_key not in csv_reader.fieldnames:
            if is_quoted(dict_key):
                dict_key_unqoted = dict_key[1:-1]
                if dict_key_unqoted in csv_reader.fieldnames:
                    print(f'Info: Interpreting dict_key as quoted <<{dict_key_unqoted}>> from quoted string <<{dict_key}>>.', file=sys.stderr)
                    dict_key = dict_key_unqoted

        if dict_key and dict_key not in csv_reader.fieldnames:
            print(f'Error: dict_key "{dict_key}" not found in CSV field names.', file=sys.stderr)
            return

        for row in csv_reader:
            data.append(row)

    with OutputWrapper.OutputWrapper(json_file_path, encoding='utf-8-sig') as json_file:
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
    parser.add_argument('csv_file', help='Path to the input CSV file.')
    parser.add_argument('json_file', nargs='?', help='Path to the output JSON file. The "%%" character will be replaced with the csv basename. '
                        'Overrides -j/--auto-json, -o/output, -O/output-nosub. Writes to stdout if not specified.')
    parser.add_argument('-j', '--auto-json', action='store_true', help='Automatically create json output name by replacing .csv or blank extension')
    parser.add_argument('-S', '--nosub', action='store_true', help='Do not automatically replace %% in the specified output filename with the csv basename')
    parser.add_argument('-d', '--dictkey', action='store', nargs=1, help='Create a JSON object instead of a JSON array using the specified key as the object name for each row. '
                        'Specify a 1-based integer column index or a field name. If the field name is an integer, wrap the argument in single and double quotes. e.g. \'"1"\'.')
    parser.add_argument('-p', '--popkey', action='store_true', help='Pop the key from each JSON sub object. Only meaningful with -d/--dictkey')
    parser.add_argument('--force-overwrite', action='store_true', help='Overwrite the output file if it exists')
    args = parser.parse_args()

    args_fail = False
    if not args.csv_file:
        print("Error: You must specify a CSV file. See --help.", file=sys.stderr)
        args_fail = True
    if args.nosub and not args.json_file:
        print("Error: -S/--nosub requires specifying output file. See --help.", file=sys.stderr)
        if args.auto_json:
            print("     - Also specifying -j/--auto-json makes this even more ridiculous. See --help.", file=sys.stderr)
        args_fail = True
    if args.json_file and args.auto_json:
        print("Warning: Specifying output file overrides -j/--auto-json. See --help.", file=sys.stderr)
        args.auto_json = False # Logic below requires auto_json to be True only if json_name came from auto_json.
    if args.popkey and not args.dictkey:
        print("Warning: -p/--popkey is only meaningful with -d/--dictkey. See --help.", file=sys.stderr)
    if args_fail:
        parser.print_help()
        return

    csv_name = args.csv_file
    if not os.path.isfile(csv_name) and not csv_name.endswith('.csv') and os.path.isfile(csv_name + '.csv'):
        csv_name += '.csv'
        print(f'Info: Auto appended ".csv" extension to "{csv_name}".', file=sys.stderr)

    json_name = args.json_file if args.json_file else csv_to_json_ext(args.csv_file) if args.auto_json else None
    if not args.auto_json and not args.nosub and json_name and '%' in json_name:
        basename = os.path.splitext(os.path.basename(csv_name))[0] if csv_name.endswith('.csv') else csv_name
        json_name = json_name.replace('%', basename)
        print(f'Info: Auto replaced % with "{basename}" in "{json_name}".', file=sys.stderr)

    if json_name and os.path.isfile(json_name) and not args.force_overwrite:
        print(f"Error: Output file '{json_name}' already exists", file=sys.stderr)
        return

    dict_key = args.dictkey[0] if args.dictkey else None
    if dict_key:
        if dict_key.isdecimal():
            dict_key = int(dict_key)
            print(f'Info: Interpreting dict_key {dict_key} as 1-based column index.', file=sys.stderr)

    csv_to_json(csv_name, json_name, dict_key, args.popkey)

if __name__ == '__main__':
    main()
