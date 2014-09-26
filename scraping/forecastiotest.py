### forecastiotest.py ###

## Script for experimenting and testing the forecast.io API. This API deals with (hyper-local) weather forecasting.

from authenticate import authtokens
import requests, time

(lat,lon) = (42.292519, -71.262222)
r = requests.get('https://api.forecast.io/forecast/' + authtokens['forecastio'] + '/' + str(lat) + ',' + str(lon))

decodedjson =  r.json()
dailyFores = decodedjson['daily']['data']   # Extract daily forecast data

for i in xrange(len(dailyFores)):
    foreTime = dailyFores[i]['time']
    timeStruct = time.strptime(time.ctime(foreTime),"%a %b %d %H:%M:%S %Y")
    formattedTime = time.strftime('%A, %B %d, %Y', timeStruct)
    print formattedTime
    forePrecProb = dailyFores[i]['precipProbability']
    if forePrecProb ==0:
        print '\tNo precipitation today.'
    else:
        forePrecType = dailyFores[i]['precipType']
        print '\tThere is a %d%% chance of %s.' % (forePrecProb*100, forePrecType)
