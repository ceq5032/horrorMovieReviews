import os
import csv
import json
import html

input_file = "_src/horror_movies.csv"
output_file = "_src/_data/upComing.json"


os.makedirs(os.path.dirname(output_file), exist_ok=True)


with open(input_file, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    movies = []

    for row in reader:

        row['description'] = html.unescape(row['description'])


        if not row['duration']:
            row['duration'] = "N/A"
        if not row['rating']:
            row['rating'] = "N/A"


        movies.append(row)


with open(output_file, "w", encoding="utf-8") as out:
    json.dump(movies, out, indent=2)

print("✅ Saved as upComing.json for Eleventy.")
