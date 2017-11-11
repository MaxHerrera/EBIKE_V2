# Create CSV module
# Julio 2017

from operations import *
from powercalc import *
from EBIKE_main_V2 import date
import csv


file = [v_bat, i_bat, pedal_time, wheel_time, gps_date, gps_time, gps_lat, gps_lng, voltaje, corriente, potencia,
        energybatt, vel_kmh, vel_norm, dist_enc, cadence, altitude, Pped, energiaped]
newfile = open('Ebike'+date+'.csv', 'w', newline='')
Ebikenew = csv.writer(newfile, delimiter=',')
Ebikenew.writerow(['V_Bat', 'I_Bat', 'Pedal_time(ms)', 'Wheel_time(ms)', 'GPS_date', 'GPS_time', 'GPS_lat',
                   'GPS_lng', 'Vbat(V)', 'Ibat(A)', 'BattPower(W)', 'Energy(J)', 'Speed(km/h)',
                   'norm.Speed', 'distance from encoder(m)', 'cadencia(RPM)', 'Altitud (msnm)',
                   'Potencia del ciclista (W)','Energía del ciclista (J)'])
Ebikenew.writerows(zip(*file))
print('CSV file created')
