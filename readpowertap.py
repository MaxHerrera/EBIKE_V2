# readpowertap module
# Julio 2017

sec = []; watts = []; cadencia = []; kmpowertap = []

import csv

archivo = csv.reader(open("Powertap JUN 30 2017 prueba2.csv", 'r', 1))

for index, row in enumerate(archivo):
    if row[0] == 'Minutes':
        continue
    else:
        sec.append(int(index)-1)
        watts.append(int(row[3]))
        cadencia.append(int(row[5]))
        kmpowertap.append(float(row[4])*1000)
