### geopytest.py ###

## Script for experimenting with geopy. Geopy should be used to convert an input location to a set of coordinates.

from geopy.geocoders import Nominatim
geolocator = Nominatim()

while True:
    inLoc = raw_input('Where are you?\t')
    location = geolocator.geocode(inLoc)
    if location==None:
        print "\nWe're sorry, we cannot find your location. Consider trying again with a more generic location. For example, instead of \"2243 East Loyola Street, MyTown\", try \"Loyola Street, MyTown\".\n"
    else:
        break
   
print location.address
print '('+str(location.latitude) + ','+str(location.longitude)+')'