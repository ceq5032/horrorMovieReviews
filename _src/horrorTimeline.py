import os
import csv
import json

# Input CSV file and output JSON file
input_file = "_src/horror_movies.csv"
output_file = "_src/_data/upComing.json"

# Ensure the output directory exists
os.makedirs(os.path.dirname(output_file), exist_ok=True)

# Read the CSV file and load data into a list of dictionaries
with open(input_file, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    movies = list(reader)

# Write the data to a JSON file
with open(output_file, "w", encoding="utf-8") as out:
    json.dump(movies, out, indent=2)

print("✅ Saved as upComing.json for Eleventy.")

