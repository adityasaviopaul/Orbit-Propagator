# -*- coding: utf-8 -*-
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

1. Fetches the most recent TLE for ESTCube-1 from
	https://www.celestrak.com/NORAD/elements/cubesat.txt
2. Extracts and outputs the following parameters:
3. Epoch in a readable date-time format
4. Inclination in radians
5. Right Ascension of the Ascending Node in radians
6. Eccentricity
7. Argument of periapsis in radians
8. Mean anomaly in radians
9. Mean motion

Propagates the orbital parameters to 2019.04.10 16:30:00.

Calculates and outputs the following propagated parameters:
	1. Epoch in a readable date-time format
	2. Mean anomaly in radians
	3. Eccentric anomaly in radians
	4. True anomaly in radians
	5. Semi-major axis in km
	6. Perigee distance in km
	7. Orbital period in minutes

