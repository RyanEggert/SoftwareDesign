#!/usr/bin/python -u
# -*- coding: utf-8 -*-

### destinations.py ###

#Data structure which holds all the unvalidated possible places one could escape. 

destsToVal = [
    ('Calgary International Airport', 'YYC'), 
    ('Pierre Elliott Trudeau International Airpor', 'YUL'), 
    ('Ottawa Macdonald-Cartier International Airport', 'YOW'), 
    ('Lester B. Pearson International Airport', 'YYZ'), 
    ('Vancouver International Airport', 'YVR'), 
    ('Hartsfield-Jackson Atlanta International', 'ATL'), 
    ('Ted Stevens Anchorage International Airport', 'ANC'), 
    ('Austin-Bergstrom International', 'AUS'), 
    ('Baltimore/Washington International - BWI Airport', 'BWI'), 
    ('Logan International', 'BOS'), 
    ('Charlotte Douglas International', 'CLT'), 
    ('Chicago Midway Airport', 'MDW'), 
    ('Chicago O\'Hare International', 'ORD'), 
    ('Cincinnati/Northern Kentucky International', 'CVG'), 
    ('Cleveland Hopkins International', 'CLE'), 
    ('Port Columbus International', 'CMH'), 
    ('Dallas/Ft. Worth International - DFW Airport', 'DFW'), 
    ('Denver International Airport', 'DEN'), 
    ('Detroit Metropolitan Wayne County Airport', 'DTW'), 
    ('Fort Lauderdale/Hollywood International', 'FLL'), 
    ('Southwest Florida International', 'RSW'), 
    ('Bradley International', 'BDL'), 
    ('Hawaii Honolulu International', 'HNL'), 
    ('George Bush Intercontinental', 'IAH'), 
    ('William P. Hobby Airport', 'HOU'), 
    ('Indianapolis International', 'IND'), 
    ('Kansas City International', 'MCI'), 
    ('McCarran International', 'LAS'), 
    ('Los Angeles International - LAX Airport', 'LAX'), 
    ('Memphis International', 'MEM'), 
    ('Miami International Airport', 'MIA'), 
    ('Minneapolis/St. Paul International', 'MSP'), 
    ('Nashville International', 'BNA'), 
    ('Louis Armstrong International', 'MSY'), 
    ('John F. Kennedy International', 'JFK'), 
    ('LaGuardia International', 'LGA'), 
    ('Newark Liberty International', 'EWR'), 
    ('Metropolitan Oakland International', 'OAK'), 
    ('Ontario International', 'ONT'), 
    ('Orlando International', 'MCO'), 
    ('Philadelphia International', 'PHL'), 
    ('Sky Harbor International', 'PHX'), 
    ('Pittsburgh International', 'PIT'), 
    ('Portland International', 'PDX'), 
    ('Raleigh-Durham International', 'RDU'), 
    ('Sacramento International', 'SMF'), 
    ('Salt Lake City International', 'SLC'), 
    ('San Antonio International', 'SAT'), 
    ('Lindbergh Field International', 'SAN'), 
    ('San Francisco International', 'SFO'), 
    ('Mineta San José International', 'SJC'), 
    ('"John Wayne Airport", Orange County"', 'SNA'), 
    ('Seattle-Tacoma International - Seatac Airport', 'SEA'), 
    ('Lambert-St. Louis International', 'STL'),
    ('Tampa International', 'TPA'), 
    ('Dulles International Airport', 'IAD'), 
    ('Ronald Reagan Washington National', 'DCA'),
    ('Beijing Capital International Airport', 'PEK'),
    ('London Heathrow', 'LHR'),
    ('Haneda Airport', 'HND'),
    ('Paris-Charles de Gaulle Airport', 'CDG'),
    ('Frankfurt Airport', 'FRA'),
    ('Hong Kong International Airport', 'HKG'),
    ('Adolfo Suárez Madrid-Barajas', 'MAD'),
    ('Dubai International Airport', 'DXB'),
    ('Amsterdam-Schiphol', 'AMS'),
    ('Soekarno-Hatta International Airport', 'CGK'),
    ('Suvarnabhumi Airport', 'BKK'),
    ('Singapore Changi International Airport', 'SIN'),
    ('Guangzhou Baiyun International Airport', 'CAN'),
    ('Pudong International Airport', 'PVG'),
    ('Leonardo da Vinci-Fiumicino Airport', 'FCO'),
    ('Sydney Airport', 'SYD'),
    ('Munich International Airport', 'MUC')

]

def validatedestinations(destinationlist):
    """Validation function for transforming destinationlist into usable toGo data.

    Takes a list of tuples [of the form (Airport_name, IATA code)] and verifies and geocodes
    each destination. A string of latitude, longitude is appended to each original tuple. The 
    new list of tuples (Airport_name, IATA code, 'lat,long', shortaddress_string) is printed and returned. 
    """
    from geopy.geocoders import GoogleV3
    from authenticate import authtokens
    import time

    destcoords = []
    geolocator = GoogleV3(authtokens['google'])
    for item in destinationlist:
        searchStr = item[0] + ' ' + item[1]
        while True:
            try:
                location = geolocator.geocode(searchStr)
            except:
                print 'Timeout -- retrying.'
                time.sleep(10)
            else:
                break
        if location==None:
            print '\nERROR: %s\n' % searchStr
        else:
            coordinstring = str(location.latitude) +', '+ str(location.longitude)
            print location.address.encode('utf-8') + ' (' + coordinstring +')'
            toParse = location.raw
            addComponents = toParse['address_components']
            locality = ''
            territ = ''
            country = ''
            for item2 in addComponents:
                if item2['types'] == [u'locality', u'political']:
                    locality = item2['long_name']
                elif item2['types'] == [u'administrative_area_level_1', u'political']:
                    territ = item2['long_name']
                elif item2 ['types'] == [u'country', u'political']:
                    country = item2 ['long_name']
            shortLoc = locality + ', ' + territ + ', ' + country
            print shortLoc.encode('utf-8')
            destcoords.append(item + (coordinstring, shortLoc.encode('utf-8')))
        time.sleep(.2)
    print destcoords
    return destcoords

# Validated Destinations w/coordinates
toGo = [('Calgary International Airport', 'YYC', '51.131471, -114.010556', 'Calgary, Alberta, Canada'), ('Pierre Elliott Trudeau International Airpor', 'YUL', '45.45764, -73.749697', 'Dorval, Quebec, Canada'), ('Ottawa Macdonald-Cartier International Airport', 'YOW', '45.319212, -75.6691652', 'Ottawa, Ontario, Canada'), ('Lester B. Pearson International Airport', 'YYZ', '43.681727, -79.612049', 'Mississauga, Ontario, Canada'), ('Vancouver International Airport', 'YVR', '49.1966913, -123.1815123', 'Richmond, British Columbia, Canada'), ('Hartsfield-Jackson Atlanta International', 'ATL', '33.639975, -84.444032', 'Atlanta, Georgia, United States'), ('Ted Stevens Anchorage International Airport', 'ANC', '61.173915, -149.981017', 'Anchorage, Alaska, United States'), ('Austin-Bergstrom International', 'AUS', '30.202633, -97.668146', 'Austin, Texas, United States'), ('Baltimore/Washington International - BWI Airport', 'BWI', '39.1774042, -76.6683922', 'Baltimore, Maryland, United States'), ('Logan International', 'BOS', '42.3656132, -71.0095602', 'Boston, Massachusetts, United States'), ('Charlotte Douglas International', 'CLT', '35.220969, -80.944215', 'Charlotte, North Carolina, United States'), ('Chicago Midway Airport', 'MDW', '41.7867759, -87.7521884', 'Chicago, Illinois, United States'), ("Chicago O'Hare International", 'ORD', '41.9741625, -87.9073214', 'Chicago, Illinois, United States'), ('Cincinnati/Northern Kentucky International', 'CVG', '39.055222, -84.661251', 'Hebron, Kentucky, United States'), ('Cleveland Hopkins International', 'CLE', '41.411675, -81.834693', 'Cleveland, Ohio, United States'), ('Port Columbus International', 'CMH', '39.9999399, -82.8871767', 'Columbus, Ohio, United States'), ('Dallas/Ft. Worth International - DFW Airport', 'DFW', '32.8998091, -97.0403352', 'DFW Airport, Texas, United States'), ('Denver International Airport', 'DEN', '39.8630335, -104.67364', 'Denver, Colorado, United States'), ('Detroit Metropolitan Wayne County Airport', 'DTW', '42.2161722, -83.3553842', 'Detroit, Michigan, United States'), ('Fort Lauderdale/Hollywood International', 'FLL', '26.0742344, -80.1506022', 'Fort Lauderdale, Florida, United States'), ('Southwest Florida International', 'RSW', '26.54285, -81.754568', 'Fort Myers, Florida, United States'), ('Bradley International', 'BDL', '41.928687, -72.683873', 'Windsor Locks, Connecticut, United States'), ('Hawaii Honolulu International', 'HNL', '21.332898, -157.921418', 'Honolulu, Hawaii, United States'), ('George Bush Intercontinental', 'IAH', '29.9902199, -95.3367827', 'Houston, Texas, United States'), ('William P. Hobby Airport', 'HOU', '29.6541074, -95.2766145', 'Houston, Texas, United States'), ('Indianapolis International', 'IND', '39.7168593, -86.2955952', 'Indianapolis, Indiana, United States'), ('Kansas City International', 'MCI', '39.3006427, -94.7125937', 'Kansas City, Missouri, United States'), ('McCarran International', 'LAS', '36.0839998, -115.1537389', 'Las Vegas, Nevada, United States'), ('Los Angeles International - LAX Airport', 'LAX', '33.9415889, -118.40853', 'Los Angeles, California, United States'), ('Memphis International', 'MEM', '35.044702, -89.981659', 'Memphis, Tennessee, United States'), ('Miami International Airport', 'MIA', '25.796549, -80.275614', 'Miami, Florida, United States'), ('Minneapolis/St. Paul International', 'MSP', '44.881234, -93.203111', 'Saint Paul, Minnesota, United States'), ('Nashville International', 'BNA', '36.134773, -86.668042', 'Nashville, Tennessee, United States'), ('Louis Armstrong International', 'MSY', '29.984223, -90.255969', 'Kenner, Louisiana, United States'), ('John F. Kennedy International', 'JFK', '40.6434612, -73.7822056', ', New York, United States'), ('LaGuardia International', 'LGA', '40.7769271, -73.8739659', 'New York, New York, United States'), ('Newark Liberty International', 'EWR', '40.68987, -74.17821', 'Newark, New Jersey, United States'), ('Metropolitan Oakland International', 'OAK', '37.7125689, -122.2197428', 'Oakland, California, United States'), ('Ontario International', 'ONT', '34.060855, -117.598279', 'Ontario, California, United States'), ('Orlando International', 'MCO', '28.4311577, -81.308083', 'Orlando, Florida, United States'), ('Philadelphia International', 'PHL', '39.8743959, -75.2424229', 'Philadelphia, Pennsylvania, United States'), ('Sky Harbor International', 'PHX', '33.4372686, -112.0077881', 'Phoenix, Arizona, United States'), ('Pittsburgh International', 'PIT', '40.495999, -80.256693', 'Pittsburgh, Pennsylvania, United States'), ('Portland International', 'PDX', '45.5897694, -122.5950942', 'Portland, Oregon, United States'), ('Raleigh-Durham International', 'RDU', '35.8743815, -78.7897901', 'Morrisville, North Carolina, United States'), ('Sacramento International', 'SMF', '38.6950854, -121.5900648', 'Sacramento, California, United States'), ('Salt Lake City International', 'SLC', '40.785596, -111.980673', 'Salt Lake City, Utah, United States'), ('San Antonio International', 'SAT', '29.524947, -98.473251', 'San Antonio, Texas, United States'), ('Lindbergh Field International', 'SAN', '32.7299705, -117.1912227', 'San Diego, California, United States'), ('San Francisco International', 'SFO', '37.615223, -122.389979', 'San Francisco, California, United States'), ('Mineta San Jos\xc3\xa9 International', 'SJC', '37.366695, -121.925906', 'San Jose, California, United States'), ('"John Wayne Airport", Orange County"', 'SNA', '33.680488, -117.860223', 'Santa Ana, California, United States'), ('Seattle-Tacoma International - Seatac Airport', 'SEA', '47.44443, -122.300497', 'Seattle, Washington, United States'), ('Lambert-St. Louis International', 'STL', '38.7419782, -90.3649791', 'St. Louis, Missouri, United States'), ('Tampa International', 'TPA', '27.976891, -82.533377', 'Tampa, Florida, United States'), ('Dulles International Airport', 'IAD', '38.953381, -77.447712', 'Dulles, Virginia, United States'), ('Ronald Reagan Washington National', 'DCA', '38.851242, -77.0402315', 'Arlington, Virginia, United States'), ('Beijing Capital International Airport', 'PEK', '40.0798573, 116.6031121', 'Beijing, Beijing, China'), ('London Heathrow', 'LHR', '51.4700223, -0.4542955', ', , United Kingdom'), ('Haneda Airport', 'HND', '35.5493932, 139.7798386', 'Ota, Tokyo, Japan'), ('Paris-Charles de Gaulle Airport', 'CDG', '49.004, 2.5711', 'Roissy-en-France, \xc3\x8ele-de-France, France'), ('Frankfurt Airport', 'FRA', '50.0379326, 8.5621518', 'Frankfurt, Hesse, Germany'), ('Hong Kong International Airport', 'HKG', '22.308047, 113.9184808', ', , Hong Kong'), ('Adolfo Su\xc3\xa1rez Madrid-Barajas', 'MAD', '40.4839361, -3.5679515', 'Madrid, Community of Madrid, Spain'), ('Dubai International Airport', 'DXB', '25.2531745, 55.3656728', 'Dubai, Dubai, United Arab Emirates'), ('Amsterdam-Schiphol', 'AMS', '52.3105392, 4.7682743', 'Amsterdam Airport Schiphol, North Holland, The Netherlands'), ('Soekarno-Hatta International Airport', 'CGK', '-6.1275118, 106.6536859', ', , Indonesia'), ('Suvarnabhumi Airport', 'BKK', '13.6899991, 100.7501124', 'Rachathewa, Samut Prakan, Thailand'), ('Singapore Changi International Airport', 'SIN', '1.3644202, 103.9915308', 'Singapore, , Singapore'), ('Guangzhou Baiyun International Airport', 'CAN', '23.3959079, 113.3079699', 'Guangzhou, Guangdong, China'), ('Pudong International Airport', 'PVG', '31.1443439, 121.808273', 'Shanghai, Shanghai, China'), ('Leonardo da Vinci-Fiumicino Airport', 'FCO', '41.7998868, 12.2462384', 'Fiumicino, Lazio, Italy'), ('Sydney Airport', 'SYD', '-33.935048, 151.164719', 'Mascot, New South Wales, Australia'), ('Munich International Airport', 'MUC', '48.3536621, 11.7750279', 'Munich, Bavaria, Germany')]

if __name__ == '__main__':
    desttuple = validatedestinations(destsToVal)  # Run validation function. 
