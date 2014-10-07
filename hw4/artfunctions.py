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
    For a more complete description of the format of the nested list functions, please see the original assignment. A link
    to this can be found at https://github.com/RyanEggert/SoftwareDesign/tree/master/hw4/References
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

    Inputs: f is a nested list function. x and y are both numeric values (here, integers). f is evaluated for the
    x,y coordinate pair. 
    Outputs: Returns calcVal, a float (with the functions we use, -1<= calcVal <= 1) for the given x and y.
    For a more complete description of the format of the nested list functions, please see the original assignment. A link
    to this can be found at https://github.com/RyanEggert/SoftwareDesign/tree/master/hw4/References
    """
    if type(f[0]) != list:
        if f[0] == 'prod':
            calcVal = evaluate_random_function(f[1], x, y) * evaluate_random_function(f[2], x, y)
        elif f[0] == 'sine':
            piOrNoPi = [0, math.pi]
            calcVal = math.sin(choice(piOrNoPi) * evaluate_random_function(f[1], x, y)) # Choose randomly whether to include pi. More excitement!
        elif f[0] == 'cosine':
            piOrNoPi = [0, math.pi]
            calcVal = math.cos(choice(piOrNoPi) * evaluate_random_function(f[1], x, y)) # Choose randomly whether to include pi. More excitement!
        elif f[0] == 'x':
            calcVal = x
        elif f[0] == 'y':
            calcVal = y
        elif f[0] == 'intsinc':
            calcVal = np.sinc(randint(300,400) * evaluate_random_function(f[1], x, y)) # Calculates the sinc w/ a rand. integer scalar. More noise, it seems
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
    """Calculates pixel values for one channel of an image.

    Inputs: width and height are integers which describe the width and height (in pixels) of the art being created.
    infunction is a nested list function which will be evaluated width*height many unique points. channel is a string
    which describes the image channel (e.g. for RGB, either 'R', 'G', or 'B') associated with infunction.
    Outputs: A numpy array containing all of the pixel values (0-255) for the channel [chanMat]. A numpy array 
    containing all of the unscaled pixel values for the current channel [unmapped].
    """

    xs = range(width)
    ys = range(height)
    totPix = width * height
    xvals = np.linspace(-1, 1, num=width)
    yvals = np.linspace(-1, 1, num=height)   # Replace with remap_interval?
    chanMat = np.empty((height,width))
    unmapped = np.empty((height,width))
    iCounter = 0
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

    print 'Unmapped minimum value: %d' % unmappedmin
    print 'Unmapped maximum value: %d' % unmappedmax
    if unmappedmin == unmappedmax:
        unmappedmax = 1
        unmappedmin = -1
    for i2 in itertools.product(xs,ys):
        x, y = i2
        chanMat[y,x] = remap_interval(unmapped[y,x], unmappedmin, unmappedmax, 0., 255.)
    return chanMat, unmapped


def remap_interval(value, inMin, inMax, outMin, outMax):
    """Remaps a value from one range to another.

    Inputs: Describe a range of values by a minimum [inMin] and a maximum [inMax]. Describe a new range of values
    (to which you wish to map) by a minimum [outMin] and a maximum [outMax]. value is a numeric input which will
    be transformed (affine) to the new range.
    Outputs: Returns a numeric value which has been remapped to the new interval. 
    EX: if value = inMin, then return outMin. EX: if value = inMax, then return outMax. 
    """

    inRange = inMax - inMin
    outRange = outMax - outMin
    scaled = float(float(value) - float(inMin)) / float(inRange)
    return outMin + (scaled * outRange)


if __name__ == '__main__':
    pass