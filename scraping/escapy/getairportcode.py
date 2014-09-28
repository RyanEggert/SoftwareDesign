### getairportcode.py ###

## Lookup an airport code for a given city

import requests

def getairportcode(coordstring):
    searchItems = {'near': coordstring, 'format':'json', 'sort':'carriers'}
    r = requests.post('http://airports.pidgets.com/v1/airports', params = searchItems)
    airportResponse = r.json()[0]   # The nearest airport with the most carriers.
    airportCode = airportResponse['code']   # Get three-letter airport code.
    print airportCode