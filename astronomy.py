import numpy as np

#constants
G = 6.67428*10**(-11) #gravitatieconstante m^3/kg/s^2
c = float(299792458)               #lichtsnelheid m/s
h = float(6.62607015*10**-34)       #planckconstant J/s
sig = 5.670367 *10**(-8)
g = 9.80665 #m/s^2
avogadro = 6.02214076 * 10 **23
#stronomical constants
AU= int(149597870700)            #astonomical unit m
parsec = 3.08567758*10**16   #parsec in m

#body masses
sunM = int(1.98847 *10**30) #sunmass in kg
earthM =1.9722*10**24       #earthmass in kg
jupiterM = 1.898*10**27     #jupiter mass in kg
ISSM = 450*10**3            #mass ISS
moonM  = 7.34767309*10**22  #moon mass in kg
mercuryM = 3.30*10**23      #mercury mass in kg
venusM = 4.87*10**24            #venus mass in kg
marsM  = 6.42*10**23            #mars mass in kg
saturnM = 5.68*10**26           #saturn mass in kg
uranusM = 8.68*10**25           #Uranus mass in kg
neptuneM = 1.02*10**26           #neptune mass in kg
plutoM = 1.27*10**22            #pluto mass in kg

#body radii
sunR = 6.957*10**8          #sun radius in m
earthR = 6371*10**3         #earth radius in m
mercuryR = 2440*10**3
venusR=6052*10**3
marsR= 3397*10**3
jupiterR = 71492*10**3
saturnR= 60268*10**3
uranusR= 25559*10**3
neptuneR= 24766*10**3
plutoR= 1150*10**3
moonR= 1738*10**3

#body density   g/cm^3
mercuryD = 5.43
venusD =5.24
earthD = 5.52
marsD=3.93
jupiterD = 1.33
saturnD =0.69
uranusD =1.32
neptuneD = 1.64
plutoD =2.06

#lichtkracht
sunL = 3.828*10**26 #WATT

#body orbital Radii
ISSOR = earthR + 407000     #orbital radius ISS
moonOR = 350*10**6      #orbital radius of moon
jupiterOR = 5.203 * AU
saturnOR = 9.537 * AU
uranusOR = 19.191 *AU
neptuneOR = 30.069 *AU
plutoOR = 39482 * AU
mercuryOR = 0.387 *AU
venusOR = 0.723 *AU


def planetdata():
    planeet=["mercury","venus","earth","mars","jupiter","saturn","uranus","neptune","pluto"]
    density=[5.43,5.24,5.52,3.93,1.33,0.69,1.32,1.64,2.06]
    mass =[3.30*10**23,4.87*10**24,5.97*10**24,6.42*10**23,1.898*10**27,5.68*10**26,8.68*10**25,1.02*10**26,1.27*10**22 ]
    radius= [2440*10**3,6052*10**3, 6378*10**3, 3397*10**3,  71492*10**3, 60268*10**3, 25559*10**3, 24766*10**3, 1150*10**3]
    return planeet, density,radius,mass
#3

def gravitationalforce(m1,m2,r):
    f=(G *m1 *m2)/(r**2)

    return f

def escapevel(m1,r):
    v = np.sqrt((2*G*m1)/r)
    return v

def maxangularvel(m1,r):                    #m1 is the object that is being orbited
    v = np.sqrt((G*m1)/r)
    return v

def eq_temperature(luminosity, albedo, orbital_radius):
    Temp = ((luminosity*(1-albedo))/(16*sig*np.pi*orbital_radius**2))**(1/4)
    return Temp