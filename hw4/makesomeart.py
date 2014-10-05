### makesomeart.py ###

from PIL import Image
from artfunctions import *

## Parameters ##
funcGenerMinDepth = 2
funcGenerMaxDepth = 4

artWidth = 6  # Desired width of art in pixels
artHeight = 6 # Desired height of art in pixels
artMode = 'RGBA' # Mode of art ('RGB', 'RGBA', 'CMYK', 'YCbCr', etc.) [http://effbot.org/imagingbook/concepts.htm#mode]

myArt = Image.new(artMode, (artWidth,artHeight))    # Creates an appropriately sized image of black pixels.
channels = myArt.getbands()
allChannels = {}
for channel in channels:
    # Generate Function
    print channel
    randfunc = buildnestedfunction(funcGenerMinDepth, funcGenerMaxDepth)
    print randfunc
    # Evaluate Function
    newChannel = calcchanpixvals(artWidth, artHeight, randfunc)
    allChannels[channel] = newChannel

# Construct numpy array of tuples and write image
finalArray = np.empty((artHeight,artWidth), dtype='i8,'*len(channels))
xs = range(artWidth)
ys = range(artHeight)
for i in itertools.product(xs,ys):
    x, y = i
    singlePixel = []
    for channel in channels:
        singlePixel.append(allChannels[channel][y, x])
    finalArray[y,x] = tuple(singlePixel)

print finalArray
