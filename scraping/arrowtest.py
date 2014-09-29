
import arrow
# inputs
inor = ['42.291625, -71.2644055', u'BOS']
origin = inor[1]
destination1 = ('Frankfurt Airport', 'FRA', '50.0379326, 8.5621518')
destination = destination1[1]
date = 'Tuesdasy, September 30, 2014'


# arrowdate = arrow.get(date, 'dddd, MMMM DD, YYYY')
# newdate = arrowdate.format('YYYY-MM-DD')
# print arrowdate
# arrowdate = arrowdate.replace(days=1)
# print arrowdate

# print origin
# print destination

# qpxin = '{"request":{"passengers":{"adultCount":1},"slice":[{"origin":"%s","destination":"%s","date":"%s"}],"solutions":1}}' %(origin,destination,newdate)
# print qpxin

escdt = date
def whentoleave(escdt):
    escdtIn = arrow.get(escdt,'dddd, MMMM DD, YYYY')
    today = arrow.now().format('dddd, MMMM DD, YYYY')
    if escdt == today:    # If we need to travel today, we will book air travel for today.
        print 'TOASTS'
        escdtOut = escdt  # Not neccessary, but is perhaps symbolic, aiding readability.
        return escdtOut
    else:   # If we need to travel later in the week (forecast range), we will book air travel on the day before the precipitation.
        escdtOut = escdtIn.replace(days=-1).format('dddd, MMMM DD, YYYY') # Decrement the escape day. Leave the day before the precipitation.
        return escdtOut

escdt2 = whentoleave(escdt)

print escdt
print escdt2