### esca.py ###

from functions import *


# Determine Location
locData = getlocation()
escapbydate, _ = getforecast(locData[0], True)

# Do you need to leave?
if not escapbydate: # If escapbydate is FALSE (i.e., if there is no inclement weather and thus no need to leave.)
    print 'Quitting'
    raise SystemExit

# Find places to go
nicePlace = findaniceplace(escapbydate)

findFlights(escapbydate, locData[1], nicePlace[1])

print 'All done! Enjoy!'
# Find a way to go there
    
