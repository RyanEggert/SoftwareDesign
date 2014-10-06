### makesomeart.py ###

from PIL import Image
from random import randint
from artfunctions import *

## Parameters ##
funcGenerMinDepth = 7
funcGenerMaxDepth = 14
artName = 'myArt_7'
artWidth = 1920 # Desired width of art in pixels
artHeight = 1200 # Desired height of art in pixels
artMode = 'CMYK' # Mode of art ('RGB', 'RGBA', 'CMYK', 'YCbCr', etc.) [http://effbot.org/imagingbook/concepts.htm#mode]

myArt = Image.new(artMode, (artWidth,artHeight))    # Creates an appropriately sized image of black pixels.
channels = myArt.getbands()
allChannels = {}
notscim = {}
for channel in channels:
    funcGenerMaxDepth = randint(1,10)
    # Generate Function
    print channel
    randfunc = buildnestedfunction(funcGenerMinDepth, funcGenerMaxDepth)
    print randfunc
    # Evaluate Function
    newChannel, nonscaledch = calcchanpixvals(artWidth, artHeight, randfunc)
    allChannels[channel] = newChannel
    notscim[channel] = nonscaledch
# Construct numpy array of tuples and write image
finalArray = np.empty((artHeight,artWidth), dtype='i8,'*len(channels))
nsArray = np.empty((artHeight,artWidth), dtype='f8,'*len(channels))
xs = range(artWidth)
ys = range(artHeight)
for i in itertools.product(xs,ys):
    x, y = i
    singlePixel = []
    singlePixelns = []
    for channel in channels:
        singlePixel.append(allChannels[channel][y, x])
        singlePixelns.append(notscim[channel][y,x])
    finalArray[y,x] = tuple(singlePixel)
    nsArray[y,x] = tuple(singlePixelns)
print 'startputpixel'

for i2 in itertools.product(xs,ys):
    x,y = i2
    myArt.putpixel((x,y), tuple(finalArray[y,x]))
myArt.save(artName + '.jpg')
myArt.save(artName + '.tif')