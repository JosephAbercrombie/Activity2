from mpl_toolkits import mplot3d
import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt



data_field1 = pd.read_csv('sensorData1.csv')

acc_X = data_field1['ACCELEROMETER X']
acc_Y = data_field1['ACCELEROMETER Y']
acc_Z = data_field1['ACCELEROMETER Z']
grav_X = data_field1['GRAVITY X']
grav_Y = data_field1['GRAVITY Y']
grav_Z = data_field1['GRAVITY Z']
linacc_X = data_field1['LINEAR ACCELERATION X']
linacc_Y = data_field1['LINEAR ACCELERATION Y']
linacc_Z = data_field1['LINEAR ACCELERATION Z']
gyro_X = data_field1['GYROSCOPE X']
gyro_Y = data_field1['GYROSCOPE Y']
gyro_Z = data_field1['GYROSCOPE Z']
light = data_field1['LIGHT']
mag_X = data_field1['MAGNETIC FIELD X']
mag_Y = data_field1['MAGNETIC FIELD Y']
mag_Z = data_field1['MAGNETIC FIELD Z']
pitch = data_field1['ORIENTATION X']
roll = data_field1['ORIENTATION Y']
azimuth = data_field1['ORIENTATION Z']
atmos_press = data_field1['ATMOSPHERIC PRESSURE']
loc_lat = data_field1['LOCATION Latitude : ']
loc_lon = data_field1['LOCATION Longitude : ']
loc_alt = data_field1['LOCATION Altitude']
loc_spd = data_field1['LOCATION Speed']
time = data_field1['Time']
sound_lev = data_field1['SOUND LEVEL']

plt.plot(time, acc_X, 'g')
plt.plot(time, acc_Y, 'b')
plt.plot(time, acc_Z, 'r')
plt.title("Accelerometer vs. Time")
plt.xlabel("Time (ms)")
plt.ylabel("Accelerometer Values (m/s^2)")
plt.show()

plt.plot(time, grav_X, 'g')
plt.plot(time, grav_Y, 'b')
plt.plot(time, grav_Z, 'r')
plt.title("Gravity vs. Time")
plt.xlabel("Time (ms)")
plt.ylabel("Gravity (m/s^2)")
plt.show()

plt.plot(time, linacc_X, 'g')
plt.plot(time, linacc_Y, 'b')
plt.plot(time, linacc_Z, 'r')
plt.title("Linear Acceleration vs. Time")
plt.xlabel("Time (ms)")
plt.ylabel("Linear Acceleration (m/s^2)")
plt.show()

plt.plot(time, gyro_X, 'g')
plt.plot(time, gyro_Y, 'b')
plt.plot(time, gyro_Z, 'r')
plt.title("Gyroscope Values vs. Time")
plt.xlabel("Time (ms)")
plt.ylabel("Gyroscope Values (rad/s)")
plt.show()

plt.plot(time, light, 'r')
plt.title("Light Values vs. Time")
plt.xlabel("Time (ms)")
plt.ylabel("Light Values (lux)")
plt.show()

plt.plot(time, mag_X, 'g')
plt.plot(time, mag_Y, 'b')
plt.plot(time, mag_Z, 'r')
plt.title("Magnetic Field vs. Time")
plt.xlabel("Time (ms)")
plt.ylabel("Magnetic Field (T)")
plt.show()

plt.plot(time, pitch, 'g')
plt.plot(time, roll, 'b')
plt.plot(time, azimuth, 'r')
plt.title("Orientation vs. Time")
plt.xlabel("Time (ms)")
plt.ylabel("Orientation")
plt.show()

plt.plot(time, atmos_press, 'r')
plt.title("Atmospheric Pressure vs. Time")
plt.xlabel("Time (ms)")
plt.ylabel("Atmospheric Pressure (hPa)")
plt.show()

plt.plot(time, loc_spd, 'r')
plt.title("Speed vs. Time")
plt.xlabel("Time (ms)")
plt.ylabel("Speed (kmh)")
plt.show()

plt.plot(time, sound_lev, 'r')
plt.title("Sound Level vs. Time")
plt.xlabel("Time (ms)")
plt.ylabel("Sound Level (dB)")
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection ='3d')
ax.plot(loc_lon, loc_lat, loc_alt, 'red')
ax.set_title("Position")
ax.set_xlabel("Longitude(degrees)")
ax.set_ylabel("Latitude(degrees)")
ax.set_zlabel("Altitude(m)")
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection ='3d')
ax.plot(acc_X, acc_Y, acc_Z, 'red')
ax.set_title("Accelerometer Readings")
ax.set_xlabel("Acceleration X(m/s^2)")
ax.set_ylabel("Acceleration Y(m/s^2)")
ax.set_zlabel("Acceleration Z(m/s^2)")
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection ='3d')
ax.plot(grav_X, grav_Y, grav_Z, 'red')
ax.set_title("Gravity")
ax.set_xlabel("Gravity X(m/s^2)")
ax.set_ylabel("Gravity Y(m/s^2)")
ax.set_zlabel("Gravity Z(m/s^2)")
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection ='3d')
ax.plot(linacc_X, linacc_Y, linacc_Z, 'red')
ax.set_title("Linear Acceleration")
ax.set_xlabel("Acceleration X(m/s^2)")
ax.set_ylabel("Acceleration Y(m/s^2)")
ax.set_zlabel("Acceleration Z(m/s^2)")
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection ='3d')
ax.plot(gyro_X, gyro_Y, gyro_Z, 'red')
ax.set_title("Gyroscope Readings")
ax.set_xlabel("Gyroscope X(rad/s)")
ax.set_ylabel("Gyroscope Y(rad/s)")
ax.set_zlabel("Gyroscope Z(rad/s)")
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection ='3d')
ax.plot(mag_X, mag_Y, mag_Z, 'red')
ax.set_title("Magnetic Field")
ax.set_xlabel("Magnetic X(T)")
ax.set_ylabel("Magnetic Y(T)")
ax.set_zlabel("Magnetic Z(T)")
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection ='3d')
ax.plot(pitch, roll, azimuth, 'red')
ax.set_title("Orientation")
ax.set_xlabel("Pitch(degrees)")
ax.set_ylabel("Roll(degrees)")
ax.set_zlabel("Azimuth(degrees)")
plt.show()
