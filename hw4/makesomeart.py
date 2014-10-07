### makesomeart.py ###

from PIL import Image
from random import randint
from artfunctions import *

## Parameters ##
funcGenerMinDepth = 15
funcGenerMaxDepth = 16
artName = 'myArt_18'
artWidth = 300 # Desired width of art in pixels
artHeight = 300 # Desired height of art in pixels
artMode = 'RGB' # Mode of art ('RGB', 'RGBA', 'CMYK', 'YCbCr', etc.) [http://effbot.org/imagingbook/concepts.htm#mode]

myArt = Image.new(artMode, (artWidth,artHeight))    # Creates an appropriately sized image of black pixels.
channels = myArt.getbands()
allChannels = {}
nonScaledChannels = {}    # Not scaled image

for channel in channels:
    # Generate Function
    print channel
    randFunc = build_random_function(funcGenerMinDepth, funcGenerMaxDepth)
    print randFunc
    print 'Generated %s-channel random function.' % channel
    # Evaluate Function
    newChannel, newNonScaledChannel, xyIterLen = calcchanpixvals(artWidth, artHeight, randFunc, channel)
    allChannels[channel] = newChannel
    nonScaledChannels[channel] = newNonScaledChannel

# Construct numpy array of tuples
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
        singlePixelns.append(nonScaledChannels[channel][y, x])
    finalArray[y,x] = tuple(singlePixel)
    nsArray[y,x] = tuple(singlePixelns)


print 'Writing image.'

for i2 in itertools.product(xs,ys):
    x,y = i2
    myArt.putpixel((x,y), tuple(finalArray[y,x]))
myArt.save(artName + '.jpg')
myArt.save(artName + '.tif')