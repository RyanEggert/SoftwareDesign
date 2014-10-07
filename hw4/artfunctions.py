### artfunctions.py ###

from random import choice, randint
import math, itertools, sys
import numpy as np


def build_random_function(min_depth, max_depth):
    """Constucts a nested list of randomly selected mathematical functions

    Inputs: Takes in an integer which defines the smallest desired "depth" or level of recursion [min_depth].
    Also takes in an integer which defines the greatest desired "depth" or level of recursion [max_depth]
    Outputs: Returns the nested list of randomly selected mathematical functions. Note that the mathematical
    functions are strings, not expressions. More code is required to parse the list into the appropriate mathematical
    functions and evaluate numerically. 
    For a more complete description of the format of 
    """
    
    # Possible terminators (variables which end branches)
    terminators = [['x'], ['y']]

    # Possible functions which continue branches. The first tuple value is a string which references the math
    # operation being performed. The second tuple value indicates how many arguements (branches) the
    # function requires.
    contfuncs = [
                ('prod', 2),
                ('sine', 1),
                ('cosine', 1),
                ('intsinc', 1),
                ('pow2abs', 1),
                ('avg3', 3),
                ('cube', 1)   
    ]

    # Base case (depth = 1)
    if max_depth == 1 or (min_depth == 1 and randint(0,1) == 1):    # As soon as we hit the minimum recursion depth, we
        return choice(terminators)                                     # randomly decide whether to terminate or continue.
    else:   # All other depths
        nextFunc, numArgs = choice(contfuncs)
        # Recursive structure: [Function_we_just_chose, [arg1], [arg2], etc.]
        if numArgs == 3:
            return [nextFunc, 
            build_random_function(min_depth-1, max_depth-1),
            build_random_function(min_depth-1, max_depth-1),
            build_random_function(min_depth-1, max_depth-1)
            ]
        if numArgs == 2:
            return [nextFunc, 
            build_random_function(min_depth-1, max_depth-1),
            build_random_function(min_depth-1, max_depth-1)
            ]
        elif numArgs == 1:
            return [nextFunc, 
            build_random_function(min_depth-1, max_depth-1),
            ]


def evaluate_random_function(f,x,y):
    """Evaluates numerically a nested list function for a given numeric x,y

    Inputs: f is a nested list function. x and y are both 
    """

    if type(f[0]) != list:
        if f[0] == 'prod':
            calcVal = evaluate_random_function(f[1], x, y) * evaluate_random_function(f[2], x, y)
        elif f[0] == 'sine':
            calcVal = math.sin(math.pi * evaluate_random_function(f[1], x, y))
        elif f[0] == 'cosine':
            calcVal = math.cos(math.pi * evaluate_random_function(f[1], x, y))
        elif f[0] == 'x':
            calcVal = x
        elif f[0] == 'y':
            calcVal = y
        elif f[0] == 'intsinc':
            calcVal = np.sinc(randint(5,5) * evaluate_random_function(f[1], x, y)) # Calculates the sinc w/ a rand. integer scalar. 
        elif f[0] == 'pow2abs':
            calcVal = np.exp2(-abs(evaluate_random_function(f[1], x, y)))
        elif f[0] == 'avg3':
            calcVal = np.mean(np.array([evaluate_random_function(f[1], x, y), evaluate_random_function(f[1], x, y), evaluate_random_function(f[1], x, y)]))
        elif f[0] == 'cube':
            calcVal = math.pow(evaluate_random_function(f[1], x, y), 3)
        else:
            print "There has been an error"
        return calcVal


def calcchanpixvals(width, height, infunction, channel):
    """Calculates pixel values for one channel of an image."""

    xs = range(width)
    ys = range(height)
    totPix = width * height
    xvals = np.linspace(-1, 1, num=width)
    yvals = np.linspace(-1, 1, num=height)   # Replace with remap_interval?
    chanMat = np.empty((height,width))
    unmapped = np.empty((height,width))
    iCounter = 0
    print
    for i in itertools.product(xs,ys):
        iCounter +=1
        x, y = i
        xv = xvals[x]
        yv = yvals[y]
        pixValue = evaluate_random_function(infunction, xv, yv)
        if iCounter%(totPix/20) == 0:
            sys.stdout.write('\rCalculated %d%% of all %s-channel pixels.' % (iCounter*100/totPix, channel)) 
            sys.stdout.flush()
        unmapped[y,x] = pixValue
    print
    unmappedmin = np.amin(unmapped)
    unmappedmax = np.amax(unmapped)

    print unmappedmin
    print unmappedmax
    if unmappedmin == unmappedmax:
        unmappedmax = 1
        unmappedmin = -1
    for i2 in itertools.product(xs,ys):
        x, y = i2
        chanMat[y,x] = remap_interval(unmapped[y,x], unmappedmin, unmappedmax, 0., 255.)
    return chanMat, unmapped, iCounter


def remap_interval(value, inMin, inMax, outMin, outMax):
    """docstring"""

    inRange = inMax - inMin
    outRange = outMax - outMin
    scaled = float(float(value) - float(inMin)) / float(inRange)
    return outMin + (scaled * outRange)


def writeimage():
    pass

if __name__ == '__main__':
    pass