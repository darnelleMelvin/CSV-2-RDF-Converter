import csv
from dateutil import parser
import re

def is_coordinate(value):
    """
    Check if the value matches the pattern for WKT-style coordinates.
    """
    return re.match(r"^Point\(-?\d+(\.\d+)? -?\d+(\.\d+)?\)$", value)

def is_numeric(value):
    """
    Check if the value is numeric (integer or float).
    """
    try:
        float(value)
        return True
    except ValueError:
        return False

def is_boolean(value):
    return value.lower() in {"true", "false"}

def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def is_decimal(value):
    try:
        float(value)
        return '.' in value and not value.isdigit()
    except ValueError:
        return False

def format_triple(subject, predicate, obj):
    """
    Format the RDF triple based on the type of the object.
    """
    # URIs
    if obj.startswith("http"):
        return f"<{subject}> <{predicate}> <{obj}> ."

    # Datetimes
    try:
        parsed_date = parser.isoparse(obj)
        if "T" in obj:
            return f"<{subject}> <{predicate}> \"{parsed_date.isoformat()}\"^^<http://www.w3.org/2001/XMLSchema#dateTime> ."
        else:
            return f"<{subject}> <{predicate}> \"{parsed_date.date()}\"^^<http://www.w3.org/2001/XMLSchema#date> ."
    except ValueError:
        pass

    # Booleans
    if is_boolean(obj):
        return f"<{subject}> <{predicate}> \"{obj.lower()}\"^^<http://www.w3.org/2001/XMLSchema#boolean> ."

    # Numbers
    if is_integer(obj):
        return f"<{subject}> <{predicate}> \"{obj}\"^^<http://www.w3.org/2001/XMLSchema#integer> ."
    if is_decimal(obj):
        return f"<{subject}> <{predicate}> \"{obj}\"^^<http://www.w3.org/2001/XMLSchema#decimal> ."

    # Coordinates
    if is_coordinate(obj):
        return f"<{subject}> <{predicate}> \"{obj}\"^^<http://www.opengis.net/ont/geosparql#wktLiteral> ."

    # Check for existing language tags
    if re.match(r'^".*"@[a-z]{2}$', obj):
        return f"<{subject}> <{predicate}> {obj} ."

    # Escape and default to string with @en
    obj = obj.replace('"', '\\"')
    return f"<{subject}> <{predicate}> \"{obj}\"@en ."

def convert_csv_to_nt(input_csv, output_nt):
    """
    Convert a CSV file to an N-Triples (.nt) file.
    """
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
