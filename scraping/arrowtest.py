
import arrow
# inputs
inor = ['42.291625, -71.2644055', u'BOS']
origin = inor[1]
destination1 = ('Frankfurt Airport', 'FRA', '50.0379326, 8.5621518')
destination = destination1[1]
date = 'Wednesday, October 01, 2014'


arrowdate = arrow.get(date, 'dddd, MMMM DD, YYYY')
newdate = arrowdate.format('YYYY-MM-DD')

print origin
print destination

qpxin = '{"request":{"passengers":{"adultCount":1},"slice":[{"origin":"%s","destination":"%s","date":"%s"}],"solutions":1}}' %(origin,destination,newdate)
print qpxin