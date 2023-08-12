#Change the following to whatever the data is for your satellite. Choose the closest TLE entry to what you are trying to calculate. First line is s, second line is t
s = '1 29249U 06027A   14065.77636423 0.00000554  00000-0  00000-0 0    02'
t = '2 29249  63.5707  74.0747 6996698 268.0737  17.6773  2.00636060    50'

#Pretty self explanatory, just separate entries with spaces
year, month, day, hour, minute, second = 2014, 3, 7, 18, 22, 00

try:
	from sgp4.api import Satrec
	from sgp4.api import jday
except:
	print('Packages failed to load. You may have to install them - "pip install sgp4". Make sure you have pip installed too!')

if __name__ == '__main__':
	jd, fr = jday(year, month, day, hour, minute, second)

	satellite = Satrec.twoline2rv(s, t)
	e, r, v = satellite.sgp4(jd, fr)

	print('This is ECI (Earth-Centred Inertial) format, which is a format that is not Earth-fixed - you will need to use the converter here https://astroconverter.com/eci2ecef.html with the following XYZ coordinates and velocity values to convert to ECEF (Earth-Centred, Earth-Fixed)')
	print('')
	print('x = ', r[0])
	print('y = ',r[1])
	print('z = ',r[2])
	print('xv = ',v[0])
	print('yv = ',v[1])
	print('zv = ',v[2])
	print('')
	print('The converter found at https://www.oc.nps.edu/oc2902w/coord/llhxyz.htm is fantastic for converting ECEF to WGS84, which will allow you to see where this particular satellite was using Google Maps')