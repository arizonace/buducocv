#!/usr/bin/env python3
# azce::csvfields.py - Arizona Edwards
# Created: 2024-11-24 14:30-EST

import csv
import argparse
import sys
import os
import OutputWrapper

def field_effect(ofile, verbose, fields, dropfields, showfields, fieldnames):
    if showfields:
        print(f'Info: fields in file:"{fieldnames}"', file=sys.stderr)

    resulting_fields = []
    field_error = False
    if fields:
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
                resulting_fields = []

    if field_error:
        print (f'Error: Field errors. No output file created.', file=sys.stderr)
    if verbose or field_error:
        would_be = ' would have been' if field_error else ''
        print (f'Info: Resulting fields{would_be}:"{resulting_fields}"', file=sys.stderr)
    return field_error, resulting_fields

def csv_fields(ofile, verbose, input_name, fields, dropfields, showfields):
    with open(input_name, mode='r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        field_error, resulting_fields = field_effect(ofile, verbose, fields, dropfields, showfields, csv_reader.fieldnames)
        if field_error or not resulting_fields:
            return
        
        delete_fields = [field for field in csv_reader.fieldnames if field not in resulting_fields]   
        if verbose:
            print (f'Info: Writing to "{ofile.output.name}"', file=sys.stderr)            
        csv_writer = csv.DictWriter(ofile, fieldnames=resulting_fields)

        csv_writer.writeheader()
        for row in csv_reader:
            if delete_fields:
                for field in delete_fields:
                    del row[field]
            csv_writer.writerow(row)


def main():
    parser = argparse.ArgumentParser(description='Convert CSV to JSON')
    parser.add_argument('-i', '--input', help='Path to the input CSV file')
    parser.add_argument('-o', '--output', help='Path to the output CSV file')
    parser.add_argument('-O', '--output_nosub', help='Path to the output CSV file, Do not substitute %% with input file basename')
    parser.add_argument('-S', '--nosub', action='store_true', help='Do not automatically replace %% in the output filename with the input basename.')
    parser.add_argument('--force-overwrite',action='store_true', help='Overwrite the output file if it exists')
    parser.add_argument('-f', '--fields', nargs='+', help='List and order of fields to include.')
    parser.add_argument('-d', '--dropfields', nargs='+', help='List of fields to drop. Remaining fields will be kept in existing order.')
    parser.add_argument('-s', '--showfields', action='store_true', help='Show the existing list of fields.')
    parser.add_argument('-v', '--verbose', action='store_true', help='Print verbose output. Includes -s/--showfields.')
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
        print("Error: You must specify at least one of -f/--fields, -d/--dropfields, or -s/--showfields. See --help.", file=sys.stderr)
        args_fail = True
    if args_fail:
        parser.print_help()
        return    
    
    if args.output_nosub:
        args.output = args.output_nosub
        args.nosub = True
    if args.verbose:
        args.showfields = True
       
    input_name = args.input
    if not os.path.isfile(input_name) and not input_name.endswith('.csv') and os.path.isfile(input_name + '.csv'):
        input_name += '.csv'    
        print(f'Info: Auto appended ".csv" extension to "{input_name}".', file=sys.stderr)
    
    output_name = args.output if args.output else None
    if output_name and not args.nosub and '%' in output_name:
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
        
    with OutputWrapper.OutputWrapper(output_name) as ofile:
        csv_fields(ofile, args.verbose, input_name, args.fields, args.dropfields, args.showfields)

if __name__ == '__main__':
    main()
