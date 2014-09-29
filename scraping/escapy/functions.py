### functions.py ###

## Script for all the fuctions. 


import requests, time, sys, arrow
from geopy.geocoders import GoogleV3
from authenticate import authtokens
from random import randint
from destinations import toGo


def getlocation():
    geolocator = GoogleV3(api_key=authtokens['google']) # 2500 free calls per day.
    while True:
        inLoc = raw_input("So, where are you?\t")
        location = geolocator.geocode(inLoc)
        if location==None:
            print "\nWe're sorry, we cannot find your location. Please try again."
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
        foreBuild['precipProb'] = forePrecProb
        foreBuild['precipType'] = forePrecType
        foreBuild['date'] = formattedTime
        foreOut.append(foreBuild)
    if printout:
        printforecast(foreOut,'Your')
    escadate = findinclweather(foreOut, printout)       
    return escadate, foreOut

def printforecast(forecast, whose):
    print '\n' + '_'*60
    print '%s Forecast:'% whose +'\n'+'.'*60 
    for item in forecast:
        print item['date']
        if item['precipProb'] == 0:
            print '\tNo precipitation today.'
        else:
            print '\tThere is a %d%% chance of %s.' % (item['precipProb']*100, item['precipType'])
    print '_'*60+'\n'



def findinclweather(forecast, printout):
    for item in forecast:
        if item['precipProb'] > 0.50:
            if printout:
                print "\nHmm, it looks like it might %s on %s. Why risk it?" % (item['precipType'], item['date'])
            escdt = item['date']
            break
    else:   # If no significant precipitation is in the forecast
        if printout:
            print "Oh! No precipitation is in your forecast. Aren\'t you lucky."
        escdt = False
    return escdt

def findaniceplace(escadate):
    print
    checkedIndices=[]
    noPlaceToGo = True
    while noPlaceToGo:
        while True:
            indexToCheck = randint(0,len(toGo)-1)
            if indexToCheck not in checkedIndices:  # If we haven't already checked this location
                checkedIndices.append(indexToCheck) # Note that we're going to check it and then do so
                break  
        placeToCheck = toGo[indexToCheck][2]
        sys.stdout.write("\rWe have checked %i potential destinations... " % (len(checkedIndices)))
        sys.stdout.flush()
        escadateNew, foreOut = getforecast(placeToCheck, False)
        if not escadateNew:    # If we've already found that it'll be pleasant throught the entire forecasted time...
            noPlaceToGo = False # Not necessary, but is perhaps symbolic, aiding readability.
            print 'Excellent weather ahoy!'
            printforecast(foreOut,'Destination (%s)'% toGo[indexToCheck][0])
            return toGo[indexToCheck]  # This would be a good place to go.
        for item in foreOut:
            if item['date'] == escadate:    # Iterate through forecast until we find the day when we want to avoid where we are
                if item['precipProb'] < 0.20:   # Will the weather here be acceptable?
                    noPlaceToGo = False # Not necessary, but is perhaps symbolic, aiding readability.
                    print 'Good weather ahead!'
                    printforecast(foreOut,'Destination (%s)'% toGo[indexToCheck][0]) 
                    return toGo[indexToCheck]    # Yes, this would be a good place to go
    time.sleep(.15) # Let's not make requests to forecast.io too frequently. 


def findFlights(date, origin, destination):
    arrowdate = arrow.get(date, 'dddd, MMMM DD, YYYY')
    qpxDate = arrowdate.format('YYYY-MM-DD')
    qpxOrigin = origin  # No reformatting neeeded
    qpxDestination = destination    # No reformatting needed
    qpxin = '{"request":{"passengers":{"adultCount":1},"slice":[{"origin":"%s","destination":"%s","date":"%s"}],"solutions":1}}' % (qpxOrigin, qpxDestination, qpxDate)
    headers = {'content-type': 'application/json'}
    qpxlink = 'https://www.googleapis.com/qpxExpress/v1/trips/search?key='+authtokens['google']
    r = requests.post(qpxlink, data = qpxin, headers = headers) # 50 free calls per day.
    flightInfo = r.json()
    parseFlightInfo(flightInfo)
    


def parseFlightInfo(flightInfo):

    QPXtrips = flightInfo['trips']['tripOption'][0]

    fare = QPXtrips['saleTotal']    # Total fare for this trip's flight(s)

    slice = QPXtrips['slice']   # All neccessary flight info is in here
    # print len(slice)    # Length of slice one way or two way flight. If len = 2 , slice[0] is outgoing flight, slice[1] is return flight 
    # Since we only care about the 'to' flight (and that's all we'll be searching for), we should say... 
    slice = QPXtrips['slice'][0]['segment']

    carrier = []    # Carrier abbreviation (e.g. 'US' represents US Airways.)
    flightNum = []  # Flight number (e.g. 1435)
    flightID = []   # Carrier and flight number stiched together (e.g. US 1435)

    deparTime = []  # Departure time read directly from QPX Express
    departureDate = []  # Formatted departure date (i.e. day of year)
    departureTime = []  # Formatted departure time (e.g. 3:52 PM)

    arriTime = []   # Arrival time read directly from QPX Express
    arrivalDate = []    # Formatted arrival date (i.e. day of year)
    arrivalTime = []    # Formatted arrival time (i.e 3:52 PM)

    legOrigin = []  # Origin airport code (e.g. 'BOS' represents Boston Logan Airport)
    legDestination = [] # Destination airport code (e.g. 'BOS' represents Boston Logan Airport)
    print '_'*60
    print '\n\nYour flight information:'
    print '.'*60
    for i in xrange(len(slice)):    # Here len(slice) is the number of legs of the flight. 1 for non-stop, 2 for 1 stop, etc. 
        print "Flight %d of %d:" % (i+1, len(slice))
        curLeg = slice[i]
        carrier.append(curLeg['flight']['carrier'])
        flightNum.append(curLeg['flight']['number'])
        flightID.append(carrier[i] + ' ' + flightNum[i])    # Example: "US 1767"
        print flightID[i]
        curLegInfo = curLeg['leg'][0]
        deparTime.append(curLegInfo['departureTime'])   # Cross-referencing with Kayak has shown that google returns the time in the local time zone. The time zone stamp ("-05:00") only serves to denote the time zone. The time listed is accurate in airport local time as is. 
        legOrigin.append(curLegInfo['origin'])
        arriTime.append(curLegInfo['arrivalTime'])
        legDestination.append(curLegInfo['destination'])
        # Arrival info
        timedyHolder = arrow.get(arriTime[i])
        arrivalTime.append(timedyHolder.format('hh:mmA'))
        arrivalDate.append(timedyHolder.format('dddd, MMM D'))
        # Departure info
        timedyHolder = arrow.get(deparTime[i])
        departureTime.append(timedyHolder.format('hh:mmA'))
        departureDate.append(timedyHolder.format('dddd, MMM D'))

        print "Departing " + legOrigin[i] + ' on ' + departureDate[i] +' at ' + departureTime[i]
        print "Arriving in " + legDestination[i] + ' on ' + arrivalDate[i]+ ' at ' + arrivalTime[i]+ '\n'

    print "Total price: %s" % (fare)
    print '_'*60+'\n'
