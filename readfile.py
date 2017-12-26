# readfile module
# Junio 2017

v_bat = []; i_bat = []; pedal_time = []; wheel_time = []
gps_date = []; gps_time = []; gps_lat = []; gps_lng = []; gps_alt = []
altitude_nf = []

import csv

archivo = csv.reader(open("Autonomia\EBIKE prueba JUL 27.txt", 'r', 1))

numstop = 0

# importación de valores a variables
for index, row in enumerate(archivo):
    if row[0] == 'STOP':
        numstop = numstop + 1
        continue
    elif row[0] == 'HEADER:':
        continue
    else:
        v_bat.append(int(row[1]))
        i_bat.append(int(row[2]))
        pedal_time.append(int(row[3]))
        wheel_time.append(int(row[4]))
        gps_date.append(row[5])
        gps_time.append(row[6])
        gps_lat.append(row[7])
        gps_lng.append(row[8])
        #gps_alt.append(row[9])

'''
for a, b in enumerate(gps_alt):
    if gps_alt[a] == 'ALT':
        altitude_nf.append(0)
    else:
        altitude_nf.append(float(gps_alt[a]))


###########
# Eliminación de elevación 0 al inicio
for x,y in enumerate(altitude_nf):
    z = 1
    if altitude_nf[x] == 0:
        while altitude_nf[z] == 0:
            z = z + 1
        altitude_nf[x] = altitude_nf[z]
###########
'''