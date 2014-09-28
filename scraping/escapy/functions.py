### functions.py ###

## Script for all the fuctions. 


import requests, time
from geopy.geocoders import Nominatim
from authenticate import authtokens

def getlocation():
    geolocator = Nominatim()
    while True:
        inLoc = raw_input('Where are you?\t')
        location = geolocator.geocode(inLoc)
        if location==None:
            print "\nWe're sorry, we cannot find your location. Consider trying again with a more generic location. For example, instead of \"2243 East Loyola Street, MyTown\", try \"Loyola Street, MyTown\".\n"
        else:
            break
    usAddress = location.address
    latlongstr = str(location.latitude) + ','+str(location.longitude)
    airportCode = getairportcode(latlongstr)
    return [latlongstr, airportCode]

def getairportcode(coordstring):
    searchItems = {'near': coordstring, 'format':'json', 'sort':'carriers', 'n':'5'}
    r = requests.post('http://airports.pidgets.com/v1/airports', params = searchItems)
    airportResponse = r.json()[0]   # Of the 5 nearest airports, the airport with the most carriers.
    airportCode = airportResponse['code']   # Get three-letter airport code.
    print airportCode
    return airportCode

def getforecast(coordstring):
    (lat,lon) = (42.292519, -71.262222)
    r = requests.get('https://api.forecast.io/forecast/' + authtokens['forecastio'] + '/' + str(lat) + ',' + str(lon))

    decodedjson =  r.json()
    dailyFores = decodedjson['daily']['data']   # Extract daily forecast data
    foreOut = []
    for i in xrange(len(dailyFores)):
        foreBuild ={}
        foreTime = dailyFores[i]['time']
        timeStruct = time.strptime(time.ctime(foreTime),"%a %b %d %H:%M:%S %Y")
        formattedTime = time.strftime('%A, %B %d, %Y', timeStruct)
        print formattedTime
        forePrecProb = dailyFores[i]['precipProbability']
        if forePrecProb ==0:
            forePrecType = 'N.A.'
            print '\tNo precipitation today.'
        else:
            forePrecType = dailyFores[i]['precipType']
            print '\tThere is a %d%% chance of %s.' % (forePrecProb*100, forePrecType)
            # Construct output data structure
        foreBuild['precipProb'] = forePrecProb
        foreBuild['precipType'] = forePrecType
        foreBuild['date'] = formattedTime
        foreOut.append(foreBuild)
    escadate = findinclweather(foreOut, True)
    return escadate

def findinclweather(forecast, printout):
    for item in forecast:
        if item['precipProb'] > 0.50:
            if printout == True:
                print "Hmm, it looks like it might %s on %s. Why risk it?" % (item['precipType'], item['date'])
            escdt = item['date']
            break
        else:   # If no significant precipitation is in the forecast
            if printout == True:
                print "Oh! No precipitation is in your forecast. Aren\'t you lucky."
            escdt = False
    return escdt
