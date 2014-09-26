### QPXExpresstest.py ###

## Script for experimenting and testing the QPX Express API. This API deals with airfare search and return.

from authenticate import authtokens
import requests, time, json


qpxin = '{"request":{"passengers":{"adultCount":1},"slice":[{"origin":"BOS","destination":"MKE","date":"2014-11-05"}],"solutions":1}}'
headers = {'content-type': 'application/json'}

qpxlink = 'https://www.googleapis.com/qpxExpress/v1/trips/search?key='+authtokens['qpxgoogle']


r = requests.post(qpxlink, data = qpxin, headers = headers)
print r.url
print r.json()
print r.text
