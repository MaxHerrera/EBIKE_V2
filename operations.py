# operations module
# Junio 2017

voltaje = []; corriente = []; potencia = []; energybatt = []; seg = []; sumpot = 0
vel_ms = []; vel_kmh = []; vel_norm = []; cadence = []; header = []; dist_enc=[]
av_vel = []; av_cad = []

vel_ms_nf = []; vel_kmh_nf = []

altitude = []; nofiltered = []

##############################
### Parametros de cálculos ###

diameter = 26			# diametro de la rueda de la bicicleta usada en pulgadas
coefv = 0.04			# el valor depende del computador usado, diríjase al informe "Reporte de pruebas funcionales en computadores de a bordo"
coefi = 0.04			# el valor depende del computador usado, diríjase al informe "Reporte de pruebas funcionales en computadores de a bordo"

##############################

from readfile import *
import math
import numpy as np
#import readGPSweb
#from readGPSweb import GPSvis_alt

for i, x in enumerate(v_bat):
    seg.append(i)                               # el arreglo seg lleva el conteo de segundos del recorrido, no se tienen en cuenta STOPS
    voltaje.append(v_bat[i]*coefv)              
    corriente.append(i_bat[i]*coefi)             
    potencia.append(voltaje[i]*corriente[i])
    sumpot = sumpot + potencia[i]
    ########## Energia de la Bateria
    if i == 0:
        energybatt.append(0)
    else:
        energybatt.append(potencia[i] + energybatt[i-1])
    ########## Velocidad No filtrada
    if wheel_time[i] == 0:
        vel_ms_nf.append(0)
    elif wheel_time[i]<= 114:
        vel_ms_nf.append(vel_ms_nf[i-1])
    else:
        vel_ms_nf.append((diameter * 0.0254 * math.pi) / (int(wheel_time[i]) / 1000))  # Cálculo de velocidad (m/s) de bicicleta
    vel_kmh_nf.append(vel_ms_nf[i] * 3.6)       # Cálculo de velocidad (Km/h) de bicicleta
    ##########

#########
# Potencia promedio de la bateria #
potprom = sumpot/max(seg)
#########

######################
# Filtro de velocidad
n = 100                                          # Filtro de datos de velocidad, modificar parametro n =! 1
array = np.linspace(0, 1, n)

for i,x in enumerate(vel_ms_nf):
    sum_time = 0
    a = i
    for a, b in enumerate(array):               # Cada vez q inicie, a debe tomar el valor de i, e iterar n veces
        if a == 0:
            a = i
        else:
            a = i + a
        if a > (len(vel_ms_nf)-1):
            sum_time = 0 + sum_time
        else:
            sum_time = vel_ms_nf[a] + sum_time

    vel_ms.append(sum_time/n)                   # Cálculo de velocidad (m/s) de bicicleta
    vel_kmh.append(vel_ms[i]*3.6)               # Cálculo de velocidad (Km/h) de bicicleta
######################

vel_max = max(vel_kmh)                          # Velocidad máxima (Km/h)
sum_vel = 0
sum_cad = 0

for i, x in enumerate(vel_kmh):                 # #####Calculo de distancia y cadencia#####
    if vel_kmh[i] == 0:
        vel_norm.append(0)
    else:
        vel_norm.append(vel_kmh[i]/vel_max)
    if i == 0:
        dist_enc.append(0)
    else:
        dist_enc.append(vel_ms[i]+dist_enc[i-1])                # Cálculo de distancia (m) recorrida
    sum_vel = vel_kmh[i] + sum_vel
    header.append('MEDIDA')                                     # Creación de arreglo encabezado para documento excel
    if pedal_time[i] == 0:
        cadence.append(0)
    elif (pedal_time[i] <= 499)and(pedal_time[i] != 0):         # filtro de datos de cadencia
        cadence.append(cadence[i-1])
    else:
        cadence.append((1/pedal_time[i])*60000)                 # Cálculo de cadencia (rpm) del ciclista
    sum_cad = cadence[i] + sum_cad

vel_prom = sum_vel / max(seg)                                   # Cálculo de velocidad (Km/h) promedio
cad_prom = sum_cad / max(seg)                                   # Cálculo de cadencia (rpm) promedio

###########################
# Impresion de datos relevantes #

print('Velocidad promedio ' + str(vel_prom) + ' Km/h')
print('Cadencia de pedaleo promedio ' + str(cad_prom) + ' rpm')
print('Distancia recorrida ' + str(max(dist_enc) / 1000) + ' Km')
print('Potencia promedio de la batería: ' + str(potprom) + ' Watts')
print('Energía de la batería ' + str(max(energybatt)) + ' Joules')
print('Número de paradas: ' + str(numstop))
print('Tiempo del recorrido: ' + str(max(seg)) + ' segundos')

###########################

for i, x in enumerate(seg):
    # av_vel.append(vel_prom)                                   # Arreglo de velocidad promedio para gráficas
    av_cad.append(cad_prom)                                     # Arreglo de cadencia promedio para gráficas

#readGPSweb

selector = True                                # Selector de datos de altitud(True=EBIKE GPS data/False=GPS visualizer data)
if selector:
    nofiltered = altitude_nf
else:
    nofiltered = GPSvis_alt

#####################################
# Filtro de altitud GPS
n = 100                                          # Filtro de datos de altitud, modificar parametro n =! 1
array = np.linspace(0, 1, n)

for i,x in enumerate(gps_alt):
    suma = 0
    a = i
    for a, b in enumerate(array):               # Cada vez q inicie, a debe tomar el valor de i, e iterar n veces
        if a == 0:
            a = i
        else:
            a = i + a
        if a > (len(nofiltered)-1):
            suma = nofiltered[len(nofiltered)-1] + suma
        else:
            suma = nofiltered[a] + suma

    altitude.append(suma/n)
######################################
