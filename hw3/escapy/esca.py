### esca.py ###
from functions import *

# Determine Location
locData = getlocation()
badDay, _ = getforecast(locData[0], True)

# Do you need to leave?
if not badDay: # If there is no inclement weather and thus no need to leave,...
    print 'Go outside and enjoy yourself!'  # Print congratulations and stop the program
    raise SystemExit

# When should you leave?
escapbydate = whentoleave(badDay)

# Find places to go
nicePlace = findaniceplace(escapbydate)

# Find a way to go there
findFlights(escapbydate, locData[1], nicePlace[1])

print 'All done! Enjoy!'

    
