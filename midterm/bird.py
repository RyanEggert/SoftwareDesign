import math

class Bird(object):
    def __init__(self, name, speed, age):
        self.name = name
        self.noise = noise
        self.speed = speed
        self.age = age
        self.pos = [0, 0] # x,y
    
    def __str__( # fill this in)
    """ also fill this in """
    
    def fly(self, flaps, direction):
        rad_dir = math.radians(direction)
        self.pos[0] = self.pos[0] + (self.speed * flaps * math.cos(rad_dir))
        self.pos[1] = self.pos[1] + (self.speed * flaps * math.cos(rad_dir))

    def talk(self, times):
        return self.noise * times
    
    def grow_up(self):
        self.age += 1


""" Create a child class phoenix that inherits from Bird. 
implement at least one new method e.g. reborn_from_ashes
override at least one method
add at least one attribute
set one attribute to be a specific value for phoenix objects
"""


def main():
    """create an instance of both the parent and child class
    call a method with each
    change an attribute for each
    print each instance
    """
    

if __name__ == "__main__":
    main()

