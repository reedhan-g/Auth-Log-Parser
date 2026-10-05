import sys
import os
import csv
import json
from parser import parse_text_line, parse_structured_event
OUTPUT_FILE = "output.csv"
FIELDS = [
    "timestamp",
    "source_ip",
    "username",
    "event_type",
    "status",
    "pid",
    "port"
]
def parse_csv_file(filename):
    events = []
    try:
     with open(filename, "r", newline="") as file:
          reader = csv.DictReader(file)
          for row in reader:
              try:
                event = parse_structured_event(row)
                if event["event_type"]:
                    events.append(event)
              except (ValueError, TypeError):
                     continue
    except (FileNotFoundError, PermissionError):
        return []
    return events
def parse_json_file(filename):
     events=[]
     try:
        with open(filename, "r") as file:
            data = json.load(file)
        if isinstance(data, dict):
            data = [data]
        if not isinstance(data, list):
            return []
        for item in data:
         if not isinstance(item, dict):
                continue
         try:
          event = parse_structured_event(item)
          if event["event_type"]:
                    events.append(event)

         except (ValueError, TypeError):
            continue

     except (FileNotFoundError, PermissionError, json.JSONDecodeError):
        return []
     return events
def parse_text_file(filename):
    events = []
    try:
        with open(filename, "r") as file:
         for line in file:
             try:
                 event = parse_text_line(line)
                 if event is not None:
                    events.append(event)
             except (ValueError, TypeError, AttributeError):
                continue
    except (FileNotFoundError, PermissionError):
        return []
    return events
def write_csv(events):
    with open(OUTPUT_FILE, "w", newline="") as file:
     writer = csv.DictWriter(
        file,
        fieldnames=FIELDS
        )
     writer.writeheader()
     for event in events:
        writer.writerow(event)
def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <input_file>")
        return
    filename = sys.argv[1]
    extension = os.path.splitext(filename)[1].lower()
    if extension in [".txt", ".log"]:
     events = parse_text_file(filename)
    elif extension == ".csv":
     events = parse_csv_file(filename)
    elif extension == ".json":
     events = parse_json_file(filename)
    else:
     print("Error: unsupported file format.")
     print("Supported formats: .txt, .log, .csv, .json")
     return
    write_csv(events)
    print(f"Parsed {len(events)} events.")
    print(f"Output written to {OUTPUT_FILE}")
if __name__ == "__main__":
    main()

    