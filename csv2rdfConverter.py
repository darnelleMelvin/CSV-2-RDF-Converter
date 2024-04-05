# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 11:38:33 2024

@author: dmelvin
"""

import csv
import os

def format_triple(subject, predicate, obj):
    # Check if object is a URI or literal
    if obj.startswith("http"):
        return f"<{subject}> <{predicate}> <{obj}> ."
    else:
        # Specify English language tag
        return f"<{subject}> <{predicate}> \"{obj}\"@en ."

def convert_csv_to_nt(input_csv, output_nt):
    with open(input_csv, 'r', newline='', encoding='utf-8') as csvfile, open(output_nt, 'w', encoding='utf-8') as ntfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Skip the header row
        for row in csvreader:
            if len(row) >= 3:
                subject, predicate, obj, *_ = row
                nt_triple = format_triple(subject, predicate, obj)
                ntfile.write(nt_triple + '\n')
            else:
                print("Error: Invalid row format - should contain at least 3 columns")

if __name__ == "__main__":
    input_csv_file = "C:/Users/dmelvin/Downloads/construct.csv"  # Change this to the path of your input CSV file
    output_nt_file = "C:/Users/dmelvin/Documents/graphBD_test/rdf_batch/output"  # Change this to the desired path of your output .nt file
    
    # Ensure the output file has the .nt extension
    if not output_nt_file.endswith('.nt'):
        output_nt_file += '.nt'
    
    convert_csv_to_nt(input_csv_file, output_nt_file)
