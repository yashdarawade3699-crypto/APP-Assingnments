import csv
import json

input_file = "student.csv"
output_file = "student.json"

with open(input_file, "r") as csvfile:
    reader = csv.DictReader(csvfile)
    data = list(reader)

with open(output_file, "w") as jsonfile:
    json.dump(data, jsonfile, indent=4)

print("CSV converted to JSON successfully!")