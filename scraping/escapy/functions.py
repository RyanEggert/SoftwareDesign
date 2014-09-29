### functions.py ###

## Script for all the fuctions. 


import requests, time, sys
from geopy.geocoders import GoogleV3
from authenticate import authtokens
from random import randint
from destinations import toGo

def getlocation():
    geolocator = GoogleV3()
    while True:
        inLoc = raw_input('Where are you?\t')
        location = geolocator.geocode(inLoc)
        if location==None:
            print "\nWe're sorry, we cannot find your location. Consider trying again with a more generic location. For example, instead of \"2243 East Loyola Street, MyTown\", try \"Loyola Street, MyTown\".\n"
        else:
            break
    usAddress = location.address
    latlongstr = str(location.latitude) + ', '+ str(location.longitude)
    airportCode = getairportcode(latlongstr)
    return [latlongstr, airportCode]

def getairportcode(coordstring):
    searchItems = {'near': coordstring, 'format':'json', 'sort':'carriers', 'n':'5'}
    r = requests.post('http://airports.pidgets.com/v1/airports', params = searchItems)
    airportResponse = r.json()[0]   # Of the 5 nearest airports, the airport with the most carriers.
    airportCode = airportResponse['code']   # Get three-letter airport code.
    print airportCode
    return airportCode

def getforecast(coordstring, printout):
    r = requests.get('https://api.forecast.io/forecast/' + authtokens['forecastio'] + '/' + coordstring)

    decodedjson =  r.json()
    dailyFores = decodedjson['daily']['data']   # Extract daily forecast data.
    foreOut = []
    for i in xrange(len(dailyFores)):
        foreBuild ={}
        foreTime = dailyFores[i]['time']
        timeStruct = time.strptime(time.ctime(foreTime),"%a %b %d %H:%M:%S %Y")
        formattedTime = time.strftime('%A, %B %d, %Y', timeStruct)
        
        forePrecProb = dailyFores[i]['precipProbability']
        
        if forePrecProb ==0:
            forePrecType = 'N.A.'
        else:
            forePrecType = dailyFores[i]['precipType']
        
        if printout == True:    # Print to console if requested.
            print formattedTime
            if forePrecProb == 0:
                print '\tNo precipitation today.'
            else:
                print '\tThere is a %d%% chance of %s.' % (forePrecProb*100, forePrecType)

        foreBuild['precipProb'] = forePrecProb
        foreBuild['precipType'] = forePrecType
        foreBuild['date'] = formattedTime
        foreOut.append(foreBuild)
    escadate = findinclweather(foreOut, printout)
    return escadate, foreOut

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

def findaniceplace(escadate):
    checkedIndices=[]
    noPlaceToGo = True
    while noPlaceToGo:
        while True:
            indexToCheck = randint(0,len(toGo)-1)
            if indexToCheck not in checkedIndices:  # If we haven't already checked this location
                checkedIndices.append(indexToCheck) # Note that we're going to check it and then do so
                break  
        placeToCheck = toGo[indexToCheck][2]
        sys.stdout.write("\rChecking %s, have searched %i potential locations..." % (toGo[indexToCheck][0], len(checkedIndices)))
        sys.stdout.flush()
        escadateNew, foreOut = getforecast(placeToCheck, False)
        if not escadateNew:    # If we've already found that it'll be pleasant throught the entire forecasted time...
            noPlaceToGo = False # Not necessary, but is perhaps symbolic, aiding readability.
            print
            return item  # This would be a good place to go.
        for item in foreOut:
            if item['date'] == escadate:    # Iterate through forecast until we find the day when we want to avoid where we are
                if item['precipProb'] < 0.00:   # Will the weather here be acceptable?
                    noPlaceToGo = False # Not necessary, but is perhaps symbolic, aiding readability.
                    print
                    return item     # Yes, this would be a good place to go
