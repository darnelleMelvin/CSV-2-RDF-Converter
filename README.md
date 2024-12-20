# CSV-2-RDF-Converter
This Python script converts data stored in a CSV (Comma-Separated Values) file into RDF (Resource Description Framework) triples serialized in the .nt format. It's a handy tool for transforming tabular data into a format suitable for use in semantic web applications, linked data, and knowledge graphs.
## Features
  - Converts CSV files into RDF triples in the .nt serialization format.
  - Supports both URI and literal values as objects.
  - Adds language tags for English to string literals (lang tag can be modified for other languages).
## How to Use
1. **`Input CSV File`**: Provide the path to your CSV file.
2. **`Run the Script`**: Execute the script **`csv2rdfConverter.py`** using Python 3.x. Make sure to have Python installed on your system.
3. **`Output`**: The script will generate an output file in the .nt format containing RDF triples. The output file will be named **`output.nt`** by default, but you can specify a different output file name if desired.
## Requirements
  - Python 3.x
  - **`csv`** module (comes pre-installed with Python)
## Example

Consider a CSV file named **`data.csv`** containing the following data:
~~~~
subject,predicate,object
http://example.org/resource1,http://www.w3.org/1999/02/22-rdf-syntax-ns#type,http://example.org/class1
http://example.org/resource2,http://example.org/property1,"Literal value"

~~~~
Running the script with this input will produce an output file named **`output.nt`** with the following content:
~~~~
<http://example.org/resource1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/class1> .
<http://example.org/resource2> <http://example.org/property1> "Literal value"@en .
~~~~

## Reporting Issues

If you encounter a bug or have a suggestion for improvement, please report it by following these steps:

1. **Search for Existing Issues**: Before creating a new issue, check the [Issues](https://github.com/darnelleMelvin/CSV-2-RDF-Converter/issues) section to see if your issue has already been reported.

2. **Create a New Issue**: If your issue is not listed, click on the "New issue" button. Fill out the issue template, providing detailed information such as:
   - A clear and concise description of the problem or suggestion.
   - Steps to reproduce the issue (if applicable).
   - Expected and actual results.
   - Screenshots or logs (if necessary).
   - Any additional context or configurations.

3. **Use Labels**: If possible, tag your issue with appropriate labels (e.g., bug, enhancement, question) to help categorize it.

4. **Stay Updated**: Once the issue is submitted, you can track updates, ask for clarification, or provide additional information as needed.

Thank you for contributing to improving the project!
~~~~

## License

Source code is made available under the [BSD 3-Clause License](LICENSE). For questions, contact [Darnelle Melvin](https://github.com/darnelleMelvin).
