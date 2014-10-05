### artfunctions.py ###

from random import choice
import math, itertools
import numpy as np


def buildnestedfunction(min_depth, max_depth):
    """docstring"""
    # Possible terminators (variables which end branches)
    terminators = [['x'], ['y']]

    # functions which continue branches. The first tuple value is a string which references the math
    # operation being performed. The second tuple value indicates how many arguements (branches) the
    # function requires.
    contfuncs = [('prod', 2), ('sine', 1), ('cosine', 1)]

    # Base case (depth = 1)
    if max_depth == 1: #or min_depth == 1:
        return choice(terminators)
    else:   # All other depths
        nextFunc, numArgs = choice(contfuncs)
        # Recursive structure: [Function_we_just_chose, [arg1], [arg2], etc.]
        if numArgs == 2:
            return [nextFunc, 
            buildnestedfunction(min_depth-1, max_depth-1),
            buildnestedfunction(min_depth-1, max_depth-1)
            ]
        elif numArgs == 1:
            return [nextFunc, 
            buildnestedfunction(min_depth-1, max_depth-1),
            ]

def evalnestedfunction(f,x,y):
    if type(f[0]) != list:
        if f[0] == 'prod':
            calcVal = evalnestedfunction(f[1], x, y) * evalnestedfunction(f[2], x, y)
        elif f[0] == 'sine':
            calcVal = math.sin(evalnestedfunction(f[1], x, y))
        elif f[0] == 'cosine':
            calcVal = math.cos(evalnestedfunction(f[1], x, y))
        elif f[0] == 'x':
            calcVal = x
        elif f[0] == 'y':
            calcVal = y
        else:
            print "There has been an error"
        return calcVal


def remapvalues(value, inMin, inMax, outMin, outMax):
    inRange = inMax - inMin
    outRange = outMax - outMin
    scaled = float(float(value) - float(inMin)) / float(inRange)
    return outMin + (scaled * outRange)


def calcchanpixvals(width, height, infunction):
    """Calculates pixel values"""
    xs = range(width)
    ys = range(height)
    xvals = np.linspace(-1, 1, num=width)
    yvals = np.linspace(-1, 1, num=width)
    chanMat = np.empty((height,width))
    unmapped = np.empty((height,width))
    for i in itertools.product(xs,ys):
        x, y = i
        xv = xvals[x]
        yv = yvals[y]
        pixValue = evalnestedfunction(infunction, xv, yv)
        unmapped[y,x] = pixValue
    unmappedmin = np.amin(unmapped)
    unmappedmax = np.amax(unmapped)

    print unmappedmin
    print unmappedmax
    for i2 in itertools.product(xs,ys):
        x, y = i2
        chanMat[y,x] = remapvalues(unmapped[y,x], unmappedmin, unmappedmax, 0., 255.)
    return chanMat, unmapped

def writeimage():
    pass

if __name__ == '__main__':
    pass