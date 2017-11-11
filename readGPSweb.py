# Read GPS visualizer web data module
# Julio 2017

import csv

GPSvis_alt = []

GPSvis = csv.reader(open("MAY 1 alt-data.csv", 'r', 1))

for index, row in enumerate(GPSvis):
    if row[0] == 'type':
        continue
    else:
        GPSvis_alt.append(float(row[3]))

for x, y in enumerate(GPSvis_alt):
    z = 1
    if GPSvis_alt[x] == 0:
        while GPSvis_alt[z] == 0:
            z = z + 1
        GPSvis_alt[x] = GPSvis_alt[z]