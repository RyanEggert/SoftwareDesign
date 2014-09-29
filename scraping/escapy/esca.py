### esca.py ###

from functions import *


# Determine Location
locData = getlocation()
escapbydate, _ = getforecast(locData[0], True)

# Do you need to leave?
if not escapbydate: # If escapbydate is FALSE (i.e., if there is no inclement weather and thus no need to leave.)
    print 'Quitting'
    raise SystemExit

print 'Toast'
# Find places to go
findaniceplace(escapbydate)

# Find a way to go there
    
