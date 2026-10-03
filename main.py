import sys
import os
import csv
import json

from parser import parse, parse_structured_event
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


    