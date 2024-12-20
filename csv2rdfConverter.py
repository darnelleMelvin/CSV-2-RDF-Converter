import csv
from dateutil import parser


def format_triple(subject, predicate, obj):
    # Check if object is a URI
    if obj.startswith("http"):
        return f"<{subject}> <{predicate}> <{obj}> ."
    else:
        # Check if object is a datetime
        try:
            parsed_date = parser.isoparse(obj)
            # Format as xsd:dateTime
            return f"<{subject}> <{predicate}> \"{parsed_date.isoformat()}\"^^<http://www.w3.org/2001/XMLSchema#dateTime> ."
        except ValueError:
            # Escape single and double quotes within the object string
            obj = obj.replace('"', '\\"')
            # Specify English language tag
            return f"<{subject}> <{predicate}> \"{obj}\"@en ."


def convert_csv_to_nt(input_csv, output_nt):
    with open(input_csv, 'r', newline='', encoding='utf-8') as csvfile, open(output_nt, 'w', encoding='utf-8') as ntfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Skip the header row
        for row in csvreader:
            if len(row) >= 3:
                subject, predicate, obj, *_ = row
                try:
                    nt_triple = format_triple(subject, predicate, obj)
                    ntfile.write(nt_triple + '\n')
                except Exception as e:
                    print(f"Error processing row {row}: {e}")
            else:
                print(f"Error: Invalid row format - should contain at least 3 columns. Row: {row}")


if __name__ == "__main__":
    input_csv_file = "inputFilepathHere.csv"  # Change this to the path of your input CSV file
    output_nt_file = "outputFilepathHere.nt"  # Change this to the desired path of your output .nt file

    convert_csv_to_nt(input_csv_file, output_nt_file)
