import math

class Bird(object):
    def __init__(self, name, speed, age, noise):
        self.name = name
        self.noise = noise
        self.speed = speed
        self.age = age
        self.pos = [0, 0] # x,y
    
    def __str__(self): 
        """ Returns a formatted string with position, name, and age information"""
        return '%s is %d years old and is at (%.2f, %.2f).' % (self.name, self.age, self.pos[0], self.pos[1])
    
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

class Phoenix(Bird):
    """docstring for Phoenix"""
    def __init__(self, name, speed, age, noise, flamecolor):
        super(Phoenix, self).__init__(name, speed, age, noise)
        self.flamecolor = flamecolor # Upon combustion, the color of a phoenix's flames
        self.pos = [5,5]    # Phoenixes don't start at the origin--too mainstream.

    def burnem(self):
        """Burns the phoenix"""
        self.age = 0   # Reborn
        return 'And, in pillars of %s flames, %s is reborn.' % (self.flamecolor, self.name)

    def talk(self, times):
        """Phoenixes are shy."""
        return '**impenetrable silence**'



def main():
    """create an instance of both the parent and child class
    call a method with each
    change an attribute for each
    print each instance
    """
    McGee = Phoenix('Hank McGee', 5, 2, 'Moo', 'blue')
    Schmitz = Bird('Harvey Schmitz', 2, 37, 'Bark')
    Schmitz.fly(5, 103)   
    story = McGee.burnem()
    print story
    print McGee, Schmitz
    print McGee.talk(5)

if __name__ == "__main__":
    main()

