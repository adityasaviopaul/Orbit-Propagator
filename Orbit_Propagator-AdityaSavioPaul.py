# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 02:41:57 2019
Author: Aditya Savio Paul

Course     : Space Systems (2018/2019)
Institute  : Institute of Technology
University : University of Tartu, Estonia

------------------About------------------------------------------
The following code propagates the orbit of the student satellite
ESTCUBE 1 to a specific date (here : April 10, 2019).
It reads the TLE(Two Line Element Set) from the online resource
https://www.celestrak.com/NORAD/elements/cubesat.txt

The Program downloads the TLE of the satellites into the resource folder and
updates/overwrites the file everytime the code is run/executed.


Reference Websites :
TLE:
https://www.celestrak.com/NORAD/elements/cubesat.txt

TLE format description:
https://spaceflight.nasa.gov/realdata/sightings/SSapplications/Post/JavaSSOP/SSOP_Help/tle_def.html

Tutorial for an orbit propagator:
http://www.castor2.ca/04_Propagation/01_Orbit/index.html

One of the many methods for solving the Kepler equation:
http://murison.alpheratz.net/dynamics/twobody/KeplerIterations_summary.pdf

A page for validating your eccentric anomaly:
http://orbitsimulator.com/sheela/kepler.htm

-----------------------------------------------------------------

"""
print("-----------------------------------------------------")
print(".................Orbit Propagator....................")
print("-----------------------------------------------------")
#Importing Libraries
import os
import math
import wget
from datetime import datetime  
from datetime import timedelta  


if os.path.exists('cubesat.txt'):
    os.remove('cubesat.txt')
        
#Reading file from online resource
file_url = 'https://www.celestrak.com/NORAD/elements/cubesat.txt'
#Downloading file to home folder
f = wget.download(file_url, 'cubesat.txt')

#Search string
lookup = 'ESTCUBE 1'

#Searching for Estcube in the Satellite TLE file
if lookup in open(f).read():
    #print(lookup,"Located")
    n=1
else:
    #print(lookup," Not Located")
    n=0

#Reading downloaded satellite TLE data
data=open('cubesat.txt')
lines=data.readlines()

if(n==1):
    with open(f) as f1:
        for num, line in enumerate(f1,1):
            if lookup in line:
                print (lookup,'found at line:', num)
                num1 = num
                
elif(n==0):
    print(lookup," Not in List")


#Obtaining and Printing TLE for Estcube 1 
print("\nTwo Element Lines for Estcube 1")
tle1 = lines[num1]
tle1 = tle1.split()
print((tle1))
tle2 = lines[num1+1]
tle2 = tle2.split()
print(tle2)

##Uncomment if you want to print every element of TLE
#Printing TLE for Esctube 1 as an array
#for i in range(len(tle1)):
#    print(tle1[i])
#print()
#for j in range(len(tle2)):
#    print(tle2[j])

#Calculating Epoch
val01 = float(tle1[3])
i,d = divmod(val01,1)
day = list(str(i))


#year
days = day[2]+day[3]+day[4]
year = '20'+day[0]+day[1]

#Hours
hours = d*24
i,d = divmod(hours,1)
hours = int(i)
#print(hours,"hours")

#minutes
minutes = d*60
i,d = divmod(minutes,1)
minutes = int(i)
#print(minutes,"minutes")

#seconds
seconds = d*60
i,d = divmod(seconds,d)
seconds = int(i)
#print(seconds,"seconds")


#Calculating Inclination in radians
inc_deg = float(tle2[2])
inc_rad = math.radians(inc_deg)

#Calculating 
#Right Ascension of the Ascending Node in radians
raan_deg = float(tle2[3])
raan_rad = math.radians(raan_deg)

#Calculating Eccentricity
ecc = "0."+(tle2[4])
ecc = float(ecc)
#print(ecc)

#Calculating Argument of Periapsis in radians
peri_deg = float(tle2[5])
peri_rad = math.radians(peri_deg)

#Calculating Mean Anomaly
ma_deg = float(tle2[6])
ma_rad = math.radians(ma_deg)

#Calculating Mean Motion
mm = tle2[6]
mm=float(mm)
#print(mm)

#---------------Orbit Propagtion-------------------------#

#Calculating Delta t (Days Elapsed)
datetimeFormat = '%Y-%m-%d %H:%M:%S'
#Adding days from TLE to January 01, 2019 
start_date = "2019-01-01 00:00:00" 

date_1 = datetime.strptime(start_date , "%Y-%m-%d %H:%M:%S")
date1 = date_1 + timedelta(days=int(days),minutes=minutes,seconds=seconds)
#print (date1)

#Reference Date 
date2 = '2019-04-10 16:30:00'        # Seminar   Date
#print(date2)

#Elapsed Days
diff = datetime.strptime(str(date1), datetimeFormat)\
    - datetime.strptime(str(date2), datetimeFormat)

#print(diff)
dt = abs(diff.days)
#print("Delta Days : ",dt)

#Calculating Mean Anomaly
a=ma_deg
b=(mm*dt)-int(mm*dt)
ma_op_deg= a + (360*(b-int((a+360*b)/360)))
#print("Mean Anomaly (Deg) ",ma_op_deg)
ma_op_rad = math.radians(ma_op_deg)
#print("Mean Anomaly (rad)",ma_op_rad)


#Calculating Eccentric Anomaly
#Since eccentricity is zero, Mean Anomaly ~ Eccentric Anomaly
#Using 3rd Order Approimation
#Reference
#http://murison.alpheratz.net/dynamics/twobody/KeplerIterations_summary.pdf
ecc_an_op_rad = ma_rad + (ecc*(math.sin(ma_rad))) + (ecc*ecc*math.sin(ma_rad)*math.cos(ma_rad))+(0.5*ecc*ecc*ecc*math.sin(ma_rad)*((3*math.cos(ma_rad)*math.cos(ma_rad))-1))
ecc_an_op_deg = math.degrees(ecc_an_op_rad)



#Calcuating True Anomaly

ta_op_rad = math.acos((math.cos(ecc_an_op_rad)-ecc)/(1-(ecc*math.cos(ecc_an_op_rad))))
ta_op_deg = math.degrees(ta_op_rad)

#Calculating Semi Major Axis(km)
mu = 2.97554e15 #Gravitational Parameter of earth
sma_op = math.pow((mu / (math.pow((2*3.157*mm),2))),(1./3.))
#print(sma_op)

#Calculating Perigee Distance
pd_op = sma_op*(1-float(ecc))

#Orbital Period
G=6.673e-11
me=5.98e24
R = sma_op 
ot = 24*60*math.sqrt((4*math.pow(math.pi,2)*17*math.pow(R,3)/(G*me)))
#print(ot)



#================Final Output==================#
print("-----------------------------------------------------")
print("Name of Satellite        : ",lookup)
print("Satellite Number         : ",tle2[1])
print("Epoch                    : ",year,"/",days,":",hours,":",minutes,":",seconds)
print("Inclination(rad)         : ",inc_rad)
print("Right Ascension of")
print("the Ascending Node (rad) : ",raan_rad)
print("Eccentricity             : ",ecc)
print("Argument Periapsis       : ",peri_rad)
print("Mean Anomaly             : ",ma_rad,)
print("Mean Motion              : ",mm)
print("Delta t (days)           : ",dt)
print()
print("----------------Propagated Orbit----------------------")
print("Epoch                    :",year,"/",days,":",hours,":",minutes,":",seconds)
print("Propogatordate           :",date2)
print("Mean Anomaly (rad)       :",ma_op_rad)
print("Eccentric Anomaly (rad)  :",ecc_an_op_rad)
print("Eccentric Anomaly (deg)  :",ecc_an_op_deg)
print("True Anomaly(rad)        :",ta_op_rad)
print("True Anomaly(deg)        :",ta_op_deg)
print("Semi Major Axis (km)     :",sma_op)
print("Perigee Distance (km)    :",pd_op)
print("Orbital Period (minutes) :",ot)
print("-----------------------------------------------------")
data.close()

#===========End Of Program==========================================================#