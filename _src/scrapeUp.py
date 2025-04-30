import os
import csv, json

input_file = "horror_coming_soon.csv"
output_file = "_data/moviesUP.json"


os.makedirs(os.path.dirname(output_file), exist_ok=True)


with open(input_file, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    movies = list(reader)


with open(output_file, "w", encoding="utf-8") as out:
    json.dump(movies, out, indent=2)

print(" Saved as moviesUP.json for Eleventy.")
