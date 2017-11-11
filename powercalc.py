# Power calculation module
# Julio 2017

import math
from operations import vel_ms, seg, dist_enc, altitude
#from readpowertap import watts, sec

va = []; acc = []
Pke = []; Ppe = []; Pbearing = []; Proll = []; Pair = []; Pres = []; Pped = []; P_prom = []
diffpower = []; Pedpower = []; energiaped = []


#####################################
#Cálculo de potencia de pedaleo
pesobicicleta = 14
pesociclista = 70
masatotal = pesobicicleta + pesociclista
n = 0.975

#Utilice estos PRINT para verificar que los vectores tengan el mismo tamaño (altitude = dist_enc - 1), de no ser así siga las observaciones del archivo LEEME
#print(len(dist_enc))
#print(len(altitude))


for c,d in enumerate(vel_ms):
    va.append(vel_ms[c])
    if c == 0:
        acc.append(0)
        theta = 0
    else:
        acc.append(vel_ms[c] - vel_ms[c-1])
        if (dist_enc[c]-dist_enc[c-1]) != 0:                                     #comentar if si usa datos del modGPS
            if (dist_enc[c]-dist_enc[c-1]) <= (altitude[c]-altitude[c-1]):
                theta = theta
            else:
                theta = math.asin(((altitude[c]-altitude[c-1])/(dist_enc[c]-dist_enc[c-1])))
        else:
            theta = 0
    Pke.append((1/2) * (masatotal + 0.14 / (0.3 ** 2)) * (acc[c] ** 2))
    Ppe.append(vel_ms[c] * masatotal * 9.81 * math.sin(theta))
    Pbearing.append((0.091 * vel_ms[c]) + (0.0087 * (vel_ms[c] ** 2)))
    Proll.append(vel_ms[c] * math.cos(theta) * 0.0032 * masatotal * 9.81)
    Pair.append((1/2) * 0.8962 * 1 * 0.504 * (va[c] ** 2) * vel_ms[c])
    Pres.append(Pair[c] + Proll[c] + Pbearing[c] + Ppe[c] + Pke[c])
    Pped.append(Pres[c] * (1/n))

for e,f in enumerate(seg):
    if Pped[e] <= 0:
        Pedpower.append(0)
    else:
        Pedpower.append(Pped[e])
    if e == 0:
         P_av = 0
    else:
         P_av = Pedpower[e - 1] + P_av
#####################################
P_av = P_av / max(seg)
print('Potencia promedio calculada ' + str(P_av) + ' Watts')
for i, j in enumerate(Pped):
    #diffpower.append(watts[i]-Pedpower[i])     # Diferencia de potencia calculada-Powertap,
    P_prom.append(P_av)


'''
#######
# Potencia promedio Powertap

for i, j in enumerate(watts):
    if i == 0:
         PT_av = 0
    else:
         PT_av = watts[i - 1] + PT_av
PT_av = PT_av / max(sec)
print('Potencia promedio PowerTap ' + str(PT_av) + ' Watts')
'''

#######
# Energía de pedaleo del ciclista #

for i, j in enumerate(Pped):
    if i == 0:
        energiaped.append(0)
    else:
        energiaped.append(Pped[i]+energiaped[i-1])

print('Energía del ciclista ' + str(max(energiaped)) + ' Joules')