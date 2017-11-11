# plot module
# Junio 2017

import matplotlib.pyplot as plt
from operations import seg, voltaje, corriente, potencia, vel_kmh, cadence, altitude, dist_enc,altitude_nf
from powercalc import P_prom, Pped, diffpower, Pedpower
#from readpowertap import *
#from readGPSweb import GPSvis_alt
#from EBIKE_main_V2 import date

################## Potencia Batería
plt.figure(num=1, figsize=(14, 6), dpi=100, facecolor='w', edgecolor='k')

plt.subplot(2,1,1)
plt.plot(seg, voltaje, 'b')
plt.plot(seg, corriente, 'r')
plt.xlabel("Segundos")
plt.legend(('Voltaje (V)', 'Corriente (A)'), loc='lower right')

plt.subplot(2,1,2)
plt.plot(seg, potencia, 'g', label='potencia')
plt.xlabel("Segundos")
plt.ylabel("Potencia(W)")

#plt.show()
##################

################## Velocidad
plt.figure(num=2, figsize=(14, 6), dpi=100, facecolor='w', edgecolor='k')
plt.subplot(1,1,1)
plt.plot(seg, vel_kmh, 'b')
#plt.plot(seg, vel_kmh_nf, 'r')
#plt.legend(('Vel filtrada', 'Vel no filtrada'), loc='upper left')
plt.ylabel("Velocidad(km/h)")
#plt.show()
##################

################## Cadencia
plt.figure(num=3, figsize=(14, 6), dpi=100, facecolor='w', edgecolor='k')
plt.title('Cadencia Computador vs. Powertap')
plt.subplot(1,1,1)
plt.plot(dist_enc, cadence, 'b')            #cadencia OBC
#plt.plot(kmpowertap, cadencia, 'r')        #cadencia powertap
plt.legend(('Cadencia computador'), loc='upper left')
plt.ylabel("Cadencia(ped/min)")
'''
plt.subplot(2,1,2)
plt.plot(sec, cadencia, 'g')
plt.ylabel("Cadencia (ped/min")
#plt.show()
'''
##################

################## Perfil de elevación
plt.figure(num=4, figsize=(14, 6), dpi=100, facecolor='w', edgecolor='k')
plt.subplot(1,1,1)
plt.plot(seg, altitude_nf, 'b')
#plt.plot(seg, GPSvis_alt, 'r')
plt.plot(seg, altitude, 'g')
plt.legend(('Altura no filtrada', 'Altura filtrada'), loc='upper left')
plt.ylabel("Elevación(msnm)")
#plt.show()
##################

################## Potencia de pedaleo
plt.figure(num=5, figsize=(14, 6), dpi=100, facecolor='w', edgecolor='k')
plt.subplot(1,1,1)
plt.plot(dist_enc, Pedpower, 'r')       # potencia calculada OBC
#plt.plot(kmpowertap,watts,'g')         # potencia powertap
#plt.plot(dist_enc, diffpower, 'b')     # diferencia de potencia
#plt.legend(('Potencia computador','Potencia powertap', 'Diferencia'), loc='upper left')
plt.ylabel("Potencia del ciclista(W)")
plt.xlabel("Distancia recorrida (m)")

#plt.subplot(2,1,2)
#plt.plot(kmpowertap,watts,'g')
#plt.ylabel("Potencia de pedaleo (W)")
#plt.savefig('graph'+date+'.png', dpi=100)
plt.show()
##################
