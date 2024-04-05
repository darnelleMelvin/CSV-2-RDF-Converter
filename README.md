# CSV-2-RDF-Converter
This Python script converts data stored in a CSV (Comma-Separated Values) file into RDF (Resource Description Framework) triples serialized in the .nt format. It's a handy tool for transforming tabular data into a format suitable for use in semantic web applications, linked data, and knowledge graphs.
## Features
  - Converts CSV files into RDF triples in the .nt serialization format.
  - Supports both URI and literal values as objects.
  - Adds language tags for English to string literals.
## How to Use
1. **`Input CSV File`**: Provide the path to your CSV file.
2. **`Run the Script`**: Execute the script **`csv2rdfConverter.py`** using Python 3.x. Make sure to have Python installed on your system.
3. Output: The script will generate an output file in the .nt format containing RDF triples. The output file will be named **`output.nt`** by default, but you can specify a different output file name if desired.
## Requirements
  - Python 3.x
  - **`csv`** module (comes pre-installed with Python)
## License
