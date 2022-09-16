import csv
import json
from dataclasses import field

data = {}
# csv_dict的键名
fieldnames = ("id", "name", "type", "hardware_model")

with open("test.csv", "r", encoding="utf-8") as csvf:
    csv_reader = csv.DictReader(csvf, fieldnames)
    with open("test.json", "w", encoding="utf-8") as jsf:
        
        jsf.write("[\n")
        for row in csv_reader:
            json.dump(row, jsf, indent = 4)
            jsf.write(",\n")
        jsf.write(']')
    

