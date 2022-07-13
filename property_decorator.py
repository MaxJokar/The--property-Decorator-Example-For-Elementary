"""
In Python, property() is a built-in function that creates and returns a property object
property(fget=None, fset=None, fdel=None, doc=None)
property(fget=None, fset=None, fdel=None, doc=None)

where,
fget is function to get value of the attribute
fset is function to set value of the attribute
fdel is function to delete the attribute
doc is a string (like a comment)

A property object has three methods, getter(), setter(), and deleter() to specify fget, fset and fdel at a later point
"""

# Using @property decorator
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature  #2    #6       #19   #23

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32    #13   # 16

    @property
    def temperature(self):
        print("Getting value...") #9 prints      #14 Prints
        return self._temperature   #10           #15

    @temperature.setter
    def temperature(self, value):
        print("Setting value...")  #3 prints in terminal     #20
        if value < -273.15:  #4        # 21
            raise ValueError("Temperature below -273 is not possible")   # 22  # 25 ERROR :Temperature below -273 is not possible
        self._temperature = value   #5


# create an object
human = Celsius(37)    #1 Breakpoint    #7

print(human.temperature) #8   #11

print(human.to_fahrenheit())    #12   # 17

coldest_thing = Celsius(-300)  # 18  #24


# Output:
    #     Setting value...
    # Getting value...
    # 37
    # Getting value...
    # 98.60000000000001
    # Setting value...
    #ERROR:Temperature below -273 is not possible
