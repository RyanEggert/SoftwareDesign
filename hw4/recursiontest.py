# recursiontest.py

from random import choice
import math


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
            calcVal = math.sin(math.pi * evalnestedfunction(f[1], x, y))
        elif f[0] == 'cosine':
            calcVal = math.cos(math.pi * evalnestedfunction(f[1], x, y))
        elif f[0] == 'x':
            calcVal = x
        elif f[0] == 'y':
            calcVal = y
        else:
            print "There has been an error"
        return calcVal






if __name__ == '__main__':
    genFunc = buildnestedfunction(3,8)
    print genFunc
    evalfun = evalnestedfunction(genFunc, 85, 1)
    print evalfun