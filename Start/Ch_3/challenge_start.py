# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
import csv
import datetime


# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# Create a CSV file with the following information:
# 40 most significant seismic events, ordered by most recent
# Header row: Magnitude, Place, Felt Reports, Date, and Google Map link
# Date should be in the format of YYYY-MM-DD

def simplify(q):
    prop = q["properties"]
    geo = q["geometry"]
    return {
        "Magnitude": prop["mag"],
        "Place": prop["place"],
        "Felt Reports": prop["felt"],
        "Date": str(datetime.date.fromtimestamp(int(prop["time"]/1000))),
        "Google Map link": f"https://www.google.com/maps/search/?api=1&query={geo['coordinates'][1]}%2C{geo['coordinates'][0]}",
        "Significance": prop["sig"]
    }

simple = list(map(simplify, data["features"]))

simple.sort(key=lambda x: 0 if x["Significance"] 
            is None else x["Significance"], reverse=True)

header = ["Magnitude","Place","Felt Reports","Date", "Google Map link"]
rows = []

for i in range(40):
    rows.append([
        simple[i]["Magnitude"],
        simple[i]["Place"],
        simple[i]["Felt Reports"],
        simple[i]["Date"],
        simple[i]["Google Map link"]]
        )

rows.sort(key=lambda x: x[3], reverse=True)
 
with open("significant.csv", "w") as file:
    writer = csv.writer(file, delimiter=",")
    writer.writerow(header)
    writer.writerows(rows)
