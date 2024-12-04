#!/usr/bin/env python3
# azce::csvfields.py - Arizona Edwards
# Created: 2024-11-24 14:30-EST

import sys
import os
import argparse
import re
import csv
import json
from collections import namedtuple
from OutputWrapper import OutputWrapper
from buducocvHtml import BuducoCvHtml

Join = namedtuple('Join', ['filename', 'key', 'fkey', 'columns'])

re_join_spec = re.compile(r'^([^:=,]+)(:[^=,]+)?(=[^,]+)?(,.*)?$')

def is_quoted(s):
    return s.startswith('"') and s.endswith('"') or s.startswith("'") and s.endswith("'")

class RowFilter:
    def __init__(self, rows, droprows, key):
        self.rows = rows
        self.droprows = droprows
        self.key = key
        self.kept = 0
        self.dropped = 0

    def accept(self, row):
        keyval = row[self.key]
        if keyval:
            if self.rows:
                self.kept += 1
                return keyval in self.rows
            elif self.droprows:
                self.kept += 1
                return keyval not in self.droprows
        self.dropped += 1
        return False
    
class RowHolder:
    def __init__(self, rows):
        self.rows = rows

def dict_fields(d, fields):
    missing_fields = [field for field in fields if field not in d]
    if missing_fields:
        print(f'Warning: Missing fields: "{missing_fields}" from object {d}.', file=sys.stderr)
    return {field: d[field] for field in fields if field in d }    

def join(row_source, join, row_filter, opts):
    result = RowHolder([])
    with open(join.filename, mode='r', encoding='utf-8-sig') as join_file:
        join_reader = csv.DictReader(join_file)

        if not join_reader.fieldnames:
            print(f'Error: No field names in join file "{join.filename}".', file=sys.stderr)
            return
        if not row_source.fieldnames:
            print(f'Error: No field names in source file.', file=sys.stderr)
            return

        if not join.columns:            
            join_columns = [field for field in join_reader.fieldnames if field not in row_source.fieldnames and field != join.key and field != join.fkey]
        else:
            missing_columns = [field for field in join.columns if field not in join_reader.fieldnames]
            if missing_columns:
                print(f'Error: Missing join columns: "{missing_columns}"', file=sys.stderr)
                return
            duplicate_columns = [field for field in join.columns if field in row_source.fieldnames]
            if duplicate_columns:
                print(f'Error: Duplicate join columns already present in source: "{duplicate_columns}"', file=sys.stderr)
                return
            join_columns = join.columns
        if opts.verbose:
            print(f'Info: Join columns: "{join_columns}"', file=sys.stderr)            
        result.fieldnames = row_source.fieldnames
        result.fieldnames.extend(join_columns)
        if opts.verbose:
            print(f'Info: Resulting columns after join: "{result.fieldnames}"', file=sys.stderr)

        join_dict = {}
        for row in join_reader:
            keyval = row[join.fkey]
            if keyval in join_dict:
                print(f'Warning: Duplicate key "{keyval}" in join file "{join.filename}".', file=sys.stderr)
            join_dict[keyval] = row

        blank_updater = {field: '' for field in join_columns}
        source_row_count = 0
        missing_join_count = 0
        join_count = 0
        for row in row_source:
            source_row_count += 1
            if not row_filter or row_filter.accept(row):
                keyval = row[join.key]
                if keyval in join_dict:
                    join_count += 1
                    row.update(dict_fields(join_dict[keyval], join_columns))
                else:
                    missing_join_count += 1
                    print(f'Warning: Key "{keyval}" not found in join file "{join.filename}".', file=sys.stderr)
                    row.update(blank_updater)
                result.rows.append(row)
        if opts.verbose:
            print(f'Info: Returning {len(result.rows)} rows. Joined {join_count} of {source_row_count} source rows. {missing_join_count} empty joins.', file=sys.stderr)
    return result.rows, result.fieldnames

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
    fieldnames = csv_reader.fieldnames

    # Determine the actual key field. Will be used by later steps
    dict_key = opt.key
    if dict_key and isinstance(dict_key, int):
        dict_key_index = dict_key
        dict_key = fieldnames[dict_key-1]
        if opt.verbose:
            print(f'Info: Interpreting dict_key as field name "{dict_key}" from index {dict_key_index}.', file=sys.stderr)
    elif dict_key and dict_key not in fieldnames:
        if is_quoted(dict_key):
            dict_key_unqoted = dict_key[1:-1]
            if dict_key_unqoted in fieldnames:
                if opt.verbose:
                    print(f'Info: Interpreting dict_key as quoted <<{dict_key_unqoted}>> from quoted string <<{dict_key}>>.', file=sys.stderr)
                dict_key = dict_key_unqoted
        if dict_key and dict_key not in fieldnames:
            print(f'Error: dict_key "{dict_key}" not found in CSV field names.', file=sys.stderr)
            return
    opt.key = dict_key

    # Process any joins to pick up additional fields that will be used by later steps.
    # Row filtering will happen now if there are joins, otherwise after field_effect.
    row_filter = RowFilter(opt.rows, opt.droprows, opt.key) if opt.rows or opt.droprows else None
    row_source, fieldnames = join(csv_reader, opt.join, row_filter, opt) if opt.join else csv_reader

    field_error, resulting_fields = field_effect(ofile, opt.verbose, opt.fields, opt.dropfields, opt.showfields, fieldnames)
    if field_error or not resulting_fields:
        return

    # Do the row filtering now if it wasn't done during the join.    
    if row_filter and not opt.join:
        row_source = [row for row in row_source if row_filter.accept(row)]

    # Show the row filter stats if it was used.
    if row_filter and opt.verbose:
        print(f'Info: Kept {row_filter.kept} rows and dropped {row_filter.dropped} rows.', file=sys.stderr)
    if opt.row_order:
        row_source.sort(key=lambda row: opt.row_order.index(row[dict_key]))

    if opt.template:
        if opt.verbose:
            print(f'Info: Using template "{opt.template}".', file=sys.stderr)
        template_row = BuducoCvHtml.get_template(opt.template)
        if not template_row:
            print(f'Error: Unknown format template "{opt.template}".', file=sys.stderr)
            return
        if opt.html:
            print(BuducoCvHtml.html_start.format(DocTitle=opt.template), file=ofile)
        template_start = BuducoCvHtml.get_template_start(opt.template)
        if template_start:
            print(template_start, file=ofile)
        for row in row_source:
            BuducoCvHtml.fix_dict(row, opt.template)
            print(template_row.format_map(row), file=ofile)
        template_end = BuducoCvHtml.get_template_end(opt.template)
        if template_end:
            print(template_end, file=ofile)
        if opt.html:
            print(BuducoCvHtml.html_end, file=ofile)

    elif opt.lines:
        if opt.verbose:
            print(f'Info: Outputting one field per line including fields {resulting_fields}.', file=sys.stderr)
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

def parse_join(join):
    m = re_join_spec.match(join)
    filename = m.group(1)
    key = m.group(2)[1:] if m.group(2) else None
    fkey = m.group(3)[1:] if m.group(3) else None
    columns = m.group(4)[1:] if m.group(4) else None
    return {'filename':filename, 'key':key, 'fkey':fkey, 'columns':columns.split(',') if columns else []} 

def guess_extension(args):
    if args.json:
        return '.json'
    elif args.html or args.template:
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
    parser = argparse.ArgumentParser(description='Format CSV files.')
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
    parser.add_argument('--join', help='CSV file with additional columns to join. filename[:key[=fkey]][,col,...]. There cannot be commas in the filename or column names.'
                        ' Specify key if different from -k/--key or -k/key not specified or fkey is different.'
                        ' Specify fkey if different from key. Optionally specify columns.')
    parser.add_argument('-j', '--json', action='store_true', help='Format the data as a JSON array. If --key is also specified, the data is formatted as a JSON object.')
    parser.add_argument('-p', '--popkey', action='store_true', help='Pop the key from each JSON sub object. Only meaningful with -j/--json and -k/--key')
    parser.add_argument('-k', '--key', help='Which field to use as the key for operations that need a key like --rows or --json.'
                        ' Specify a 1-based integer column index or a field name. If the field name is an integer, wrap the argument in single and double quotes. e.g. \'"1"\'.')
    parser.add_argument('-l', '--lines', action='store_true', help='Output as text, one field per line.')
    parser.add_argument('-v', '--verbose', action='store_true', help='Print verbose output. Includes -s/--showfields.')
    parser.add_argument('--template', help='Format each row using the specified template')
    parser.add_argument('--html', action='store_true', help='Wrap the formatted rows in a complete HTML file.')
    args = parser.parse_args()

    args_fail = False
    if not args.input:
        print("Error: You must specify an input CSV file. See --help.", file=sys.stderr)
        args_fail = True
    if args.output and args.output_nosub:
        print("Error: You may not specify both -o/--output and -O/--output_nosub. See --help.", file=sys.stderr)
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
        if args.lines or args.template or args.json or args.rows:
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
    if args.key and not (args.rows or args.droprows or args.json or args.join):
        print("Warning: You should not specify -k/--key without also specifying -r/--rows, --droprows, or -j/--json, or --join. See --help.", file=sys.stderr)
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

    if args.join:
        join_spec = parse_join(args.join)
        if not join_spec['key']:
            if not args.key:
                print(f'Error: You must specify a key either with -k/--key or directly in the join argument when using --join. No key in "{join_spec}".', file=sys.stderr)
                parser.print_help()
                return
            join_spec['key'] = args.key
        if not join_spec['fkey']:
            join_spec['fkey'] = join_spec['key']
        if args.verbose:
            print(f'Info: Joining with "{join_spec}".', file=sys.stderr)
        args.join = Join(join_spec['filename'], join_spec['key'], join_spec['fkey'], join_spec['columns'])

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
