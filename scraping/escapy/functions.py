### functions.py ###

## Script for all the fuctions. 

import arrow, requests, sys, time
from geopy.geocoders import GoogleV3    # Geocoding module
from random import randint              # Generate random integers
from authenticate import authtokens     # Retrieves API authentication from a .gitignored .py file. See sampleauthenticate.py for structure.
from destinations import toGo           # See destinations.py


def getlocation():
    """Requests a user's location, geocodes the string, and returns the coordinates and the nearest major airport (IATA code)

    Inputs: None.
    Outputs: A two-element list. First element is a string of geographic coordinates. The second element is a string giving the three-letter
    IATA code of the major airport nearest to the coordinates. (EX: [('40.303056, -105.685833', 'DEN'])
    """
    geolocator = GoogleV3(api_key=authtokens['google']) # 2500 free calls per day.
    while True:
        inLoc = raw_input("So, where are you?\t")
        location = geolocator.geocode(inLoc)
        if location==None:
            print "\nWe're sorry, we cannot find your location. Please try again."
        else:
            break
    usAddress = location.address
    latlongstr = str(location.latitude) + ', '+ str(location.longitude) # Prepare the geographic coordinates for return and future use
    airportCode = getairportcode(latlongstr)    # Find the airport from which you should depart
    return [latlongstr, airportCode]


def getairportcode(coordstring):
    """Given a string of geog. coordinates, returns the coordinates and the nearest major airport (IATA code)

    Inputs: A string of geographic coordinates [coordstring] (EX: '40.303056, -105.685833')
    Outputs: A string giving the three-letter IATA code of the major airport nearest to the given coordinates. (EX: 'DEN')
    """
    searchItems = {'near': coordstring, 'format':'json', 'sort':'carriers', 'n':'5'}
    r = requests.post('http://airports.pidgets.com/v1/airports', params = searchItems)
    airportResponse = r.json()[0]   # Of the 5 nearest airports, the airport with the most carriers.
    airportCode = airportResponse['code']   # Get three-letter airport code.
    return airportCode


def getforecast(coordstring, printout):
    """Given a string of geog. coordinates, returns (and conditionally prints) a daily forecast for the specified location.

    Inputs: A string of geographic coordinates [coordstring] (EX: '40.303056, -105.685833'), and a boolean value [printout]. The boolean value
            indicates whether to print forecast to the console.
    Outputs: A formatted date string [escadate] which indicates the day/whether the local weather will be unacceptably likely to precipitate. False if the weather
            is good for the entire forecasted time. Date string of format "Tuesday, December 9, 2014" otherwise. Also returns a list of dictionaries of relevant 
            forecast information [foreOut] for analysis/printing by other functions. 
    """
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
        if forePrecProb == 0:
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
    """Given a forecast dictionary list and an identifier, formats and prints forecast to console.

    Inputs: A forecast dictionary list [forecast]. Each element dictionary in the list corresponds to the forecast for a day. Forecast specifics
            are carried within the element dictionaries. Each dictionary has keys 'date' (EX: 'Tuesday, December 9, 2014'), 'precipProb' (EX: 0.58), 
            and 'precipType' (EX: 'rain'). An identifier [whose] prepends a string to the forecast title. For example, if whose = 'Your', the function
            will print 'Your forecast' at the top of the console-printed forecast.
    Outputs: None.
    """
    print '\n' + '_'*60
    print '%s Forecast:'% whose +'\n'+'.'*60 
    for item in forecast:
        print item['date']
        if item['precipProb'] == 0:
            print '\tNo precipitation today.'
        else:
            print '\tThere is a %d%% chance of %s.' % (item['precipProb']*100, item['precipType'])
    print '\tForecast data from forecast.io'    # Forecast.io API terms request an attribution when forecast data is displayed.
    print '_'*60+'\n'



def findinclweather(forecast, printout):
    """Given a forecast dictionary list, checks for inclement weather and conditionally prints results to the console.

    Inputs: A forecast dictionary list [forecast]. Each element dictionary in the list corresponds to the forecast for a day. Forecast specifics
            are carried within the element dictionaries. Each dictionary has keys 'date' (EX: 'Tuesday, December 9, 2014'), 'precipProb' (EX: 0.58), 
            and 'precipType' (EX: 'rain'). A boolean value [printout], which indicates whether to print forecast to the console.
    Outputs: A formatted date string [escdt] which indicates the day/whether the local weather will be unacceptably likely to precipitate. False if the weather
            is good for the entire forecasted time. Date string of format "Tuesday, December 9, 2014" otherwise.
    """
    for item in forecast:
        if item['precipProb'] > 0.40:   # Precipitation risk tolerance
            if printout:
                print "\nHmm, it looks like it might %s on %s. Why risk it?" % (item['precipType'], item['date'])
            escdt = item['date']
            break
    else:   # If no significant precipitation is in the forecast
        if printout:
            print "Oh! No precipitation is in your forecast. Aren\'t you lucky."
        escdt = False
    return escdt


def whentoleave(escdt):
    """Given a formatted date string, returns a formatted date string which has been adjusted to book travel optimally. 

    Inputs: A formatted date string [escdt] which indicates the day the local weather will be unacceptably likely to precipitate.
            Date string of format "Tuesday, December 9, 2014".
    Outputs: A formatted date string [escdtOut] which indicates the proper day to book travel. If the input escdt is today, we 
            should book flights for today. If the input escdt is in the future, we will book travel the day before escdt so that
            we can entirely avoid the bad weather at our origin.
    """    
    escdtIn = arrow.get(escdt,'dddd, MMMM DD, YYYY')
    today = arrow.now().format('dddd, MMMM DD, YYYY')
    if escdt == today:    # If we need to travel today, we will book air travel for today.
        escdtOut = escdt  # Not neccessary, but is perhaps symbolic, aiding readability.
        return escdtOut
    else:   # If we need to travel later in the week (forecast range), we will book air travel on the day before the precipitation.
        escdtOut = escdtIn.replace(days=-1).format('dddd, MMMM DD, YYYY') # Decrement the escape day. Leave the day before the precipitation.
        return escdtOut


def findaniceplace(escadate):
    """Given a formatted date string, finds a location which will have good weather on the date. 

    Inputs: A formatted date string [escadate] which indicates the day the local weather will be unacceptably likely to precipitate.
            Date string of format "Tuesday, December 9, 2014".
    Outputs: A destination tuple [toGo[indexToCheck]] which contains an airport name, the corresponding three-letter IATA airport code,
            a coordinate string, and a reduced address string. 
            (EX: ('Denver International Airport', 'DEN', '39.8630335, -104.67364', 'Denver, Colorado, United States')) 
            The function randomly iterates through a list of potential destinations [toGo], checking the forecast on escadate (and then
            the day after escadate, if possible) at each until a location with good weather on escadate is found. Prints results to console. 
    """   
    print   # Newline before future console prints.
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
            printforecast(foreOut,'Destination (%s)'% toGo[indexToCheck][3])
            return toGo[indexToCheck]  # This would be a good place to go.
        for item in foreOut:
            if item['date'] == escadate:    # Iterate through forecast until we find the day when we want to get away.
                if item['precipProb'] < 0.20:   # Will the weather here be acceptable?
                    checktomorrow = foreOut.index(item) + 1
                    if checktomorrow <= len(foreOut): # As long as we have a forecast for 'tomorrow'
                        if foreOut[checktomorrow]['precipProb'] < 0.20: # Make sure tomorrow's weather is good too.
                            noPlaceToGo = False # Not necessary, but is perhaps symbolic, aiding readability.
                            print 'Good weather ahead!'
                            printforecast(foreOut,'Destination (%s)'% toGo[indexToCheck][3]) 
                            return toGo[indexToCheck]    # Yes, this would be a good place to go.
    time.sleep(.15) # Let's not make requests to forecast.io too frequently. 


def findFlights(date, origin, destination):
     """Given a formatted date, origin, and destination, finds a one-person, one-way flight. 

    Inputs: A formatted date string [date] which indicates the day of departure. Date string of format "Tuesday, December 9, 2014". A
            three-letter string IATA code representing the origin airport [origin] (EX: 'BOS'). A three-letter string IATA code representing the 
            destination airport [destination] (EX: 'DEN').
    Outputs: None
            Uses Google-QPX Express API to return a JSON structure (parsed into Python data structures by the Requests module) of flight 
            information [flightInfo]. This structure is passed directly into the parseFlightInfo function.
    """   
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
    """Given a complex data structure of flight information, extract relevant information, format it, and print it to the console. 

    Inputs: A Google-QPX Express response JSON (for a one-way flight) which has been parsed into Python data structures by the
            Requests module [flightInfo]. 
    Outputs: None
            Formats and prints flight information (origin/destination, departure/arrival times for each leg of flight, 
            and total fare (tax- and fee-inclusive)) to the console. 
    """ 

    QPXtrips = flightInfo['trips']['tripOption'][0]
    fare = QPXtrips['saleTotal']    # Total fare for this trip's flight(s)
    # slice = QPXtrips['slice']   # All neccessary flight info is in here
    # print len(slice)    # Length of slice indicates one way or two way flight. If len = 2 , slice[0] is outgoing flight, slice[1] is return flight 
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
