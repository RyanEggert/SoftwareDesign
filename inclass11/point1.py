"""

Code example from Think Python, by Allen B. Downey.
Available from http://thinkpython.com

Copyright 2012 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.

"""

class Point(object):
    """Represents a point in 2-D space."""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.location = (x,y)

    def distfrom(self, newx, newy):
        xDist = newx - self.x
        yDist = newy - self.y
        tDist = float((xDist**2 + yDist**2)**0.5)
        return tDist

    def printloc(self):
        print self.location
        


def print_point(p):
    """Print a Point object in human-readable format."""
    print '(%g, %g)' % (p.x, p.y)


class Rectangle(object):
    """Represents a rectangle. 

    attributes: width, height, corner.
    """


def find_center(rect):
    """Returns a Point at the center of a Rectangle."""
    p = Point()
    p.x = rect.corner.x + rect.width/2.0
    p.y = rect.corner.y + rect.height/2.0
    return p


def grow_rectangle(rect, dwidth, dheight):
    """Modify the Rectangle by adding to its width and height.

    rect: Rectangle object.
    dwidth: change in width (can be negative).
    dheight: change in height (can be negative).
    """
    rect.width += dwidth
    rect.height += dheight


def main():
    blank = Point()
    blank.x = 3
    blank.y = 4
    print 'blank',
    print_point(blank)

    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 0.0
    box.corner.y = 0.0

    center = find_center(box)
    print 'center',
    print_point(center)

    print box.width
    print box.height
    print 'grow'
    grow_rectangle(box, 50, 100)
    print box.width
    print box.height


def distance_between_points(pointOne, pointTwo):
    xDist = pointTwo.x - pointOne.x
    yDist = pointTwo.y - pointOne.y
    tDist = float((xDist**2 + yDist**2)**0.5)
    return tDist


if __name__ == '__main__':
    point1 = Point(1,4)
    point2 = Point(3,7)
    distance = distance_between_points(point1,point2)
    print 'The distance is %f.' % distance
    print point1.distfrom(8,8)
    print point2.location
    point2.printloc()






