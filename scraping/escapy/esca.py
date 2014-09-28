### esca.py ###

from functions import *

# Determine Location
locData = getlocation()
escapbydate = getforecast(locData[0])

# Do you need to leave?
if not escapbydate: # If escapbydate is FALSE (i.e., if there is no inclement weather and thus no need to leave.)
    print 'Quitting'
    raise SystemExit

# Find places to go


# Find a way to go there
    
