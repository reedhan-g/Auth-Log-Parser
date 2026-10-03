import sys
import os
import csv
import json
from parser import parse_text_line, parse_structured_event
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


    