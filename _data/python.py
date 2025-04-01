import requests

URL = "https://horror.fandom.com/wiki/Chronological_List_of_Horror_Films"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(URL, headers=headers)

print(response.status_code)  # Should be 200
print(response.text[:500])   # Preview the first 500 characters of the page

