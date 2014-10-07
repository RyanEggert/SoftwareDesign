### artisdead.py ###

## Mass-produce computer-generated art

from makesomeart import makesomeart
from random import randint, choice

artWidth = 1920 # Desired width of art in pixels
artHeight = 1200 # Desired height of art in pixels

for art in xrange(100):
    funcGenerMinDepth = randint(1,10)
    funcGenerMaxDepth = randint(funcGenerMinDepth, 10)
    artModes = ['RGB', 'RGBA', 'CMYK', 'YCbCr']
    artMode = choice(artModes)
    artName = 'generatedArt_%d_%s_min%d_max%d' % (art+1, artMode, funcGenerMinDepth, funcGenerMaxDepth)
    print 'CREATING PIECE #%d: %s' % ((art+1), artName)
    makesomeart(funcGenerMinDepth, funcGenerMaxDepth, artName, artWidth, artHeight, artMode)


