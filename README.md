# Auth-Log-Parser
It is a CLI utility that ingests system authentication logs and extracts structured authentication events from each entry. 
## Description
A python CLI utility, that parses auth logs from .txt, .log, .csv and .json files and converts the extracted events into a standardized output.csv file.
## Build 
### Requirements
Only Python 3, no other external Python packages are required.
The project uses Python's built in modules:
+ sys — command-line arguments
+ os — file extension detection
+ csv — reading and writing CSV files
+ json — reading JSON files
+ re — regular expressions for extracting information from log lines
+ datetime — timestamp conversion
### Structure
**main.py** handles file input, format detection, event collection, and output. \
**parser.py** contains the parsing and timestamp-conversion logic.
## How to USE
### Syntax 
Run the parser from the project directory:
python main.py <input_file>
### Changing the Output File
The output file is being controlled by OUTPUT_FILE variable in main.py, to replace the output file, replace the filename. \
For example: \
OUTPUT_FILE = "new_outputfile.csv" \
The parser will then write the results to:
new_outputfile.csv
## License
This project is licensed under the MIT License
