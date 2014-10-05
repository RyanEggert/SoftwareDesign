# testfile.py
import numpy, scipy
import itertools
from PIL import Image
import numpy as np
# xs = range(6)
# print xs
# ys = range(20)

# for i in itertools.product(xs, ys):
#     print i

# img = Image.open("test2image.png")
# arr = numpy.array(img)

# print arr.shape

# pythonmatrix = np.array([[50,60,12,200,140,14],[50,60,12,200,3,140],[50,60,12,200,30,14],[50,60,12,200,166,14],[50,60,12,200,160,14],[50,60,12,200,232,14]])
# print pythonmatrix.shape
# numpyim=Image.fromarray(arr)


# picz = Image.new('RGB', (1500,1500), "white")
# for i in itertools.product(range(440,460), range(640,900)):
#     picz.putpixel(i,0)

# picz.save('test6image.png')


matrix = np.zeros((3,6))

matrix[2,1] = 5

print matrix

tobo = (5,2,2,6,7,19)

for thing in tobo:
    print thing


import artfunctions

evalnestedfunction()