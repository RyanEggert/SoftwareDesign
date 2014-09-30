### QPXExpressparsetest.py ###

## Script for experimenting and testing the QPX Express API output. This API deals with airfare search and return. 
## This should prevent unneccessary API calls. 

import arrow

QPXresp = {u'kind': u'qpxExpress#tripsSearch', u'trips': {u'tripOption': [{u'saleTotal': u'USD130.60', u'kind': u'qpxexpress#tripOption', u'slice': [{u'duration': 262, u'kind': u'qpxexpress#sliceInfo', u'segment': [{u'kind': u'qpxexpress#segmentInfo', u'bookingCodeCount': 9, u'flight': {u'carrier': u'US', u'number': u'1767'}, u'leg': [{u'origin': u'BOS', u'originTerminal': u'B', u'departureTime': u'2014-11-05T20:30-05:00', u'destinationTerminal': u'B', u'secure': True, u'destination': u'PHL', u'kind': u'qpxexpress#legInfo', u'aircraft': u'319', u'onTimePerformance': 41, u'arrivalTime': u'2014-11-05T21:50-05:00', u'duration': 80, u'id': u'LBtFajmeaAXap3go', u'mileage': 279}], u'connectionDuration': 55, u'bookingCode': u'E', u'duration': 80, u'id': u'GS5iATluVjdhVgjJ', u'cabin': u'COACH', u'marriedSegmentGroup': u'0'}, {u'kind': u'qpxexpress#segmentInfo', u'bookingCodeCount': 9, u'flight': {u'carrier': u'US', u'number': u'4039'}, u'leg': [{u'origin': u'PHL', u'originTerminal': u'F', u'departureTime': u'2014-11-05T22:45-05:00', u'onTimePerformance': 60, u'secure': True, u'destination': u'MKE', u'kind': u'qpxexpress#legInfo', u'aircraft': u'CRJ', u'mileage': 688, u'arrivalTime': u'2014-11-05T23:52-06:00', u'duration': 127, u'operatingDisclosure': u'OPERATED BY US AIRWAYS EXPRESS-AIR WISCONSIN', u'id': u'LqxWPVV-ePeGNOOn'}], u'bookingCode': u'E', u'duration': 127, u'id': u'GvtT3J4w4fBirVsi', u'cabin': u'COACH', u'marriedSegmentGroup': u'0'}]}], u'id': u'HjBvDDP5vCHPnpxNnuERa7001', u'pricing': [{u'fare': [{u'origin': u'BOS', u'basisCode': u'EA14XSI5', u'kind': u'qpxexpress#fareInfo', u'destination': u'MKE', u'carrier': u'US', u'id': u'AE/XysIoiU4PsYXsE60QOZxPzx0DGHdpjfH4fLzxg2LE'}], u'saleTotal': u'USD130.60', u'kind': u'qpxexpress#pricingInfo', u'segmentPricing': [{u'kind': u'qpxexpress#segmentPricing', u'fareId': u'AE/XysIoiU4PsYXsE60QOZxPzx0DGHdpjfH4fLzxg2LE', u'freeBaggageOption': [{u'kind': u'qpxexpress#freeBaggageAllowance', u'bagDescriptor': [{u'count': 0, u'subcode': u'0GM', u'kind': u'qpxexpress#bagDescriptor', u'commercialName': u'ASSISTIVE DEVICES'}, {u'count': 0, u'subcode': u'0G5', u'kind': u'qpxexpress#bagDescriptor', u'commercialName': u'INFANT CAR SEAT', u'description': [u'Infant Car Seat']}, {u'count': 0, u'subcode': u'0F4', u'kind': u'qpxexpress#bagDescriptor', u'commercialName': u'STROLLER OR PUSHCHAIR', u'description': [u'Stroller/Pushchair']}], u'pieces': 0}], u'segmentId': u'GS5iATluVjdhVgjJ'}, {u'kind': u'qpxexpress#segmentPricing', u'fareId': u'AE/XysIoiU4PsYXsE60QOZxPzx0DGHdpjfH4fLzxg2LE', u'freeBaggageOption': [{u'kind': u'qpxexpress#freeBaggageAllowance', u'bagDescriptor': [{u'count': 0, u'subcode': u'0GM', u'kind': u'qpxexpress#bagDescriptor', u'commercialName': u'ASSISTIVE DEVICES'}, {u'count': 0, u'subcode': u'0G5', u'kind': u'qpxexpress#bagDescriptor', u'commercialName': u'INFANT CAR SEAT', u'description': [u'Infant Car Seat']}, {u'count': 0, u'subcode': u'0F4', u'kind': u'qpxexpress#bagDescriptor', u'commercialName': u'STROLLER OR PUSHCHAIR', u'description': [u'Stroller/Pushchair']}], u'pieces': 0}], u'segmentId': u'GvtT3J4w4fBirVsi'}], u'passengers': {u'kind': u'qpxexpress#passengerCounts', u'adultCount': 1}, u'ptc': u'ADT', u'tax': [{u'kind': u'qpxexpress#taxInfo', u'code': u'US', u'country': u'US', u'salePrice': u'USD7.53', u'chargeType': u'GOVERNMENT', u'id': u'US_1'}, {u'kind': u'qpxexpress#taxInfo', u'code': u'AY', u'country': u'US', u'salePrice': u'USD5.60', u'chargeType': u'GOVERNMENT', u'id': u'AY'}, {u'kind': u'qpxexpress#taxInfo', u'code': u'XF', u'country': u'US', u'salePrice': u'USD9.00', u'chargeType': u'GOVERNMENT', u'id': u'XF'}, {u'kind': u'qpxexpress#taxInfo', u'code': u'ZP', u'country': u'US', u'salePrice': u'USD8.00', u'chargeType': u'GOVERNMENT', u'id': u'ZP'}], u'fareCalculation': u'BOS US X/PHL US MKE 100.47EA14XSI5 USD 100.47 END ZP BOS PHL XT 7.53US 8.00ZP 5.60AY 9.00XF BOS4.50 PHL4.50', u'saleFareTotal': u'USD100.47', u'baseFareTotal': u'USD100.47', u'saleTaxTotal': u'USD30.13', u'latestTicketingTime': u'2014-09-27T23:59-04:00'}]}], u'kind': u'qpxexpress#tripOptions', u'data': {u'city': [{u'kind': u'qpxexpress#cityData', u'code': u'BOS', u'name': u'Boston'}, {u'kind': u'qpxexpress#cityData', u'code': u'MKE', u'name': u'Milwaukee'}, {u'kind': u'qpxexpress#cityData', u'code': u'PHL', u'name': u'Philadelphia'}], u'kind': u'qpxexpress#data', u'tax': [{u'kind': u'qpxexpress#taxData', u'id': u'ZP', u'name': u'US Flight Segment Tax'}, {u'kind': u'qpxexpress#taxData', u'id': u'XF', u'name': u'US Passenger Facility Charge'}, {u'kind': u'qpxexpress#taxData', u'id': u'AY', u'name': u'US September 11th Security Fee'}, {u'kind': u'qpxexpress#taxData', u'id': u'US_1', u'name': u'US Transportation Tax'}], u'airport': [{u'city': u'BOS', u'kind': u'qpxexpress#airportData', u'code': u'BOS', u'name': u'Boston Logan International'}, {u'city': u'MKE', u'kind': u'qpxexpress#airportData', u'code': u'MKE', u'name': u'Milwaukee General Mitchell'}, {u'city': u'PHL', u'kind': u'qpxexpress#airportData', u'code': u'PHL', u'name': u"Philadelphia/Wilmington Int'l"}], u'aircraft': [{u'kind': u'qpxexpress#aircraftData', u'code': u'319', u'name': u'Airbus A319'}, {u'kind': u'qpxexpress#aircraftData', u'code': u'CRJ', u'name': u'Canadair Reg. Jet'}], u'carrier': [{u'kind': u'qpxexpress#carrierData', u'code': u'US', u'name': u'US Airways, Inc.'}]}, u'requestId': u'PiMwxjQVVKZGQGGMe0KjVd'}}

QPXtrips = QPXresp['trips']['tripOption'][0]

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
    print "Arriving in " + legDestination[i] + ' on ' + departureDate[i]+ ' at ' + arrivalTime[i]+ '\n'

print "Total price: %s" % (fare)



