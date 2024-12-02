#!/usr/bin/env python3
# azce::csvfields.py - Arizona Edwards
# Created: 2024-11-24 14:30-EST

import sys
import os
import argparse
import csv
import json
from OutputWrapper import OutputWrapper
from buducocvHtml import BuducoCvHtml

def is_quoted(s):
    return s.startswith('"') and s.endswith('"') or s.startswith("'") and s.endswith("'")

def field_effect(ofile, verbose, fields, dropfields, showfields, fieldnames):
    if showfields:
        print(f'Info: fields in file:"{fieldnames}"', file=sys.stderr)

    resulting_fields = []
    field_error = False
    if fields:
        if len(fields) == 1 and fields[0].startswith(':'):
            if fields[0] == ':all' or fields[0] == ':':
                fields = fieldnames
                if verbose:
                    print (f'Info: Including all fields.', file=sys.stderr)
            else:
                print (f'Dropping first colon (":") from first field name: "{fields[0]}".', file=sys.stderr)
                fields[0] = fields[0][1:]

        missing_fields = [field for field in fields if field not in fieldnames]
        if missing_fields:
            present_fields = [field for field in fieldnames if field in fields]
            print (f'Error: Missing fields: "{missing_fields}"', file=sys.stderr)
            print (f'     - The available requested fields are:"{present_fields}"', file=sys.stderr)
            field_error = True
        else:
            skipped_fields = [field for field in fieldnames if field not in fields]
            if verbose and skipped_fields:
                print (f'Info: Skipping fields:"{skipped_fields}"', file=sys.stderr)
            resulting_fields = fields
    elif dropfields:
        resulting_fields = [field for field in fieldnames if field not in dropfields]
        missing_dropfields = [field for field in dropfields if field not in fieldnames]
        if missing_dropfields:
            present_dropfields = [field for field in dropfields if field in fieldnames]
            if present_dropfields:
                print (f'Warning: Missing drop fields: "{missing_dropfields}"', file=sys.stderr)
                print (f'       - These fields will be dropped:"{present_dropfields}"', file=sys.stderr)
            else:
                print (f'Error: Missing all drop fields: "{missing_dropfields}". No fields would be dropped.', file=sys.stderr)
                field_error = True

    if field_error:
        print (f'Error: Field errors. No output file created.', file=sys.stderr)
    if verbose or field_error:
        would_be = ' would have been' if field_error else ''
        print (f'Info: Resulting fields{would_be}:"{resulting_fields}"', file=sys.stderr)
    return field_error, resulting_fields

def csv_fields(ofile, csv_file, opt): # verbose, input_name, fields, dropfields, showfields, lines):
    csv_reader = csv.DictReader(csv_file)
    field_error, resulting_fields = field_effect(ofile, opt.verbose, opt.fields, opt.dropfields, opt.showfields, csv_reader.fieldnames)
    if field_error or not resulting_fields:
        return

    dict_key = opt.key
    if dict_key and isinstance(dict_key, int):
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

    row_source = csv_reader
    if opt.rows or opt.droprows:
        row_source = []
        kept_row_count = 0
        dropped_row_count = 0
        for row in csv_reader:
            if opt.rows:
                if row[dict_key] in opt.rows:
                    row_source.append(row)
                    kept_row_count += 1
                else:
                    dropped_row_count += 1
            elif opt.droprows:
                if row[dict_key] not in opt.droprows:
                    row_source.append(row)
                    kept_row_count += 1
                else:
                    dropped_row_count += 1
        if opt.verbose:
            print(f'Info: Kept {kept_row_count} rows and dropped {dropped_row_count} rows.', file=sys.stderr)
        if opt.row_order:
            row_source.sort(key=lambda row: opt.row_order.index(row[dict_key]))

    if opt.format:
        template_row = BuducoCvHtml.get_template(opt.format)
        if not template_row:
            print(f'Error: Unknown format template "{opt.format}".', file=sys.stderr)
            return
        if opt.html:
            print(BuducoCvHtml.html_start.format(DocTitle=opt.format), file=ofile)
        template_start = BuducoCvHtml.get_template_start(opt.format)
        if template_start:
            print(template_start, file=ofile)
        for row in row_source:
            BuducoCvHtml.fix_dict(row, opt.format)
            print(template_row.format_map(row), file=ofile)
        template_end = BuducoCvHtml.get_template_end(opt.format)
        if template_end:
            print(template_end, file=ofile)
        if opt.html:
            print(BuducoCvHtml.html_end, file=ofile)

    elif opt.lines:
        print (f'Included fields: {resulting_fields}', file=ofile)
        for row in row_source:
            print("===== Start Record:\n", file=ofile)
            for field in resulting_fields:
                print(f'Field {field}:\n{row[field]}\n', file=ofile)

    elif opt.json:
        if dict_key:
            jo = {}
            for row in row:
                if opt.pop_key:
                    key = row.pop(dict_key)
                    jo[key]=row
                else:
                    jo[row[dict_key]]=row
            json.dump(jo, ofile, indent=4)
        else:
            json.dump(row_source, ofile, indent=4)

    else:
        delete_fields = [field for field in csv_reader.fieldnames if field not in resulting_fields]
        csv_writer = csv.DictWriter(ofile, fieldnames=resulting_fields)
        csv_writer.writeheader()
        for row in row_source:
            if delete_fields:
                for field in delete_fields:
                    del row[field]
            csv_writer.writerow(row)

def guess_extension(args):
    if args.json:
        return '.json'
    elif args.html or args.format:
        return '.html'
    elif args.lines:
        return '.txt'
    else:
        return '.2.csv'

def replace_csv_extension(filename, extension):
    if filename.endswith('.csv'):
        return filename[:-4] + extension
    else:
        return filename + extension

def main():
    parser = argparse.ArgumentParser(description='Convert CSV to JSON')
    parser.add_argument('-i', '--input', help='Path to the input CSV file')
    parser.add_argument('-o', '--output', help='Path to the output file, %% in the name will be replaced with the input file basename'
                        ' while a value of %%.%% will auto generate the entire output filename')
    parser.add_argument('-O', '--output_nosub', help='Path to the output file avoiding %% marker substitution.')
    parser.add_argument('-S', '--nosub', action='store_true', help='Do not perform %% marker substitution on the output filename.')
    parser.add_argument('--force-overwrite',action='store_true', help='Overwrite the output file if it exists')
    parser.add_argument('-f', '--fields', nargs='+', help='List and order of fields to include. ":" or ":all" includes all fields.')
    parser.add_argument('-d', '--dropfields', nargs='+', help='List of fields to drop. Remaining fields will be kept in existing order.')
    parser.add_argument('-s', '--showfields', action='store_true', help='Show the existing list of fields.')
    parser.add_argument('-r', '--rows', nargs='+', help='List of rows to include.')
    parser.add_argument('--row-order', nargs='+', help='List of rows to include in the specified order.')
    parser.add_argument('--droprows', nargs='+', help='List of rows to drop.')
    parser.add_argument('-j', '--json', action='store_true', help='Format the data as a JSON array. If --key is also specified, the data is formatted as a JSON object.')
    parser.add_argument('-p', '--popkey', action='store_true', help='Pop the key from each JSON sub object. Only meaningful with -j/--json and -k/--key')
    parser.add_argument('-k', '--key', help='Which field to use as the key for operations that need a key like --rows or --json.'
                        ' Specify a 1-based integer column index or a field name. If the field name is an integer, wrap the argument in single and double quotes. e.g. \'"1"\'.')
    parser.add_argument('-v', '--verbose', action='store_true', help='Print verbose output. Includes -s/--showfields.')
    parser.add_argument('--format', help='Format each row using the specified template')
    parser.add_argument('--html', action='store_true', help='Wrap the formatted rows in a complete HTML file.')
    args = parser.parse_args()

    args_fail = False
    if not args.input:
        print("Error: You must specify an input CSV file. See --help.", file=sys.stderr)
        args_fail = True
    if args.output and args.output_nosub:
        print("Error: You must may not specify both -o/--output and -O/--output_nosub. See --help.", file=sys.stderr)
        args_fail = True
    if not (args.output or args.output_nosub) and (args.nosub or args.force_overwrite):
        print("Error: You may not specify filename modifiers like -S/--nosub or --force-overwrite without also specifying an output file. See --help.", file=sys.stderr)
        args_fail = True
    if args.output_nosub and args.nosub:
        print("Warning: -S/--nosub has no additional effect when -O/--output_nosub is specified.", file=sys.stderr)
    if args.fields and args.dropfields:
        print("Error: You may not specify both -f/--fields and -d/--dropfields. See --help.", file=sys.stderr)
        args_fail = True
    if not (args.fields or args.dropfields or args.showfields):
        if args.lines or args.format or args.json or args.rows:
            args.fields = [':all']
        else:
            print("Error: You must specify at least one of -f/--fields, -d/--dropfields, -s/--showfields, or -r/--rows if the output is still csv. See --help.", file=sys.stderr)
        args_fail = True
    if args.rows and args.row_order:
        print("Error: You may not specify both -r/--rows and --row-order because --row-order implies and overrides -r/--rows. See --help.", file=sys.stderr)
        args_fail = True
    if args.row_order:
        args.rows = args.row_order
    if args.rows and args.droprows:
        print("Error: You may not specify both (-r/--rows or --row-order) and --droprows. See --help.", file=sys.stderr)
        args_fail = True
    if (args.rows or args.droprows) and not args.key:
        print("Error: You must specify a key with -k/--key when filtering rows with -r/--rows, --row-order or --droprows. See --help.", file=sys.stderr)
        args_fail = True
    if args.key and not (args.rows or args.droprows or args.json):
        print("Error: You may not specify -k/--key without also specifying -r/--rows, --droprows, or -j/--json. See --help.", file=sys.stderr)
        args_fail = True
    if args.popkey and not (args.key and args.json):
        print("Warning: -p/--popkey is only meaningful when both -k/--key and -j/--json are also specified. See --help.", file=sys.stderr)
    if args_fail:
        parser.print_help()
        return

    if args.json:
        print("Sorry: -j/--json is not yet implemented.", file=sys.stderr)
        return

    if args.output_nosub:
        args.output = args.output_nosub
        args.nosub = True
    if args.verbose:
        args.showfields = True

    if args.key:
        if args.key.isdecimal():
            args.key = int(args.key)
            print(f'Info: Interpreting key {args.key} as 1-based column index.', file=sys.stderr)

    input_name = args.input
    if not os.path.isfile(input_name) and not input_name.endswith('.csv') and os.path.isfile(input_name + '.csv'):
        input_name += '.csv'
        print(f'Info: Auto appended ".csv" extension to "{input_name}".', file=sys.stderr)

    output_name = args.output if args.output else None
    if output_name and not args.nosub and (output_name == '%.%' or output_name == '%%'):
        output_name = replace_csv_extension(input_name, guess_extension(args))
        print(f'Info: Auto generated output filename "{output_name}".', file=sys.stderr)
    elif output_name and not args.nosub and '%' in output_name:
        basename = os.path.splitext(os.path.basename(input_name))[0]
        output_name = output_name.replace('%', basename)
        print(f'Info: Auto replaced % with "{basename}" in "{output_name}".', file=sys.stderr)


    if output_name and os.path.isfile(output_name) and not args.force_overwrite:
        print(f"Error: Output file '{output_name}' already exists", file=sys.stderr)
        return

    if args.verbose:
        print(f'Info: Extracting CSV fields from "{input_name}"', file=sys.stderr)
        if args.fields:
            print (f'Info: Requested fields: "{args.fields}"', file=sys.stderr)
        if args.dropfields:
            print (f'Info: Requested drop fields: "{args.dropfields}"', file=sys.stderr)

    with OutputWrapper(output_name) as ofile:
        with open(input_name, mode='r', encoding='utf-8-sig') as csv_file:
            csv_fields(ofile, csv_file, args)

if __name__ == '__main__':
    main()
