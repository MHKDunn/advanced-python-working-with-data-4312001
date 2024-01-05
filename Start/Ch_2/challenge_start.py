# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
from collections import Counter


# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

events = Counter(list(map(lambda x: x["properties"]["type"], data["features"])))

for k, v in events.items():
    print(f"{k.ljust(20)}: {v}")
