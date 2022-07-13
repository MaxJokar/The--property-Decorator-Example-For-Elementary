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
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value...")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value


# create an object
human = Celsius(37)

print(human.temperature)

print(human.to_fahrenheit())

coldest_thing = Celsius(-300)


# Output:
    #     Setting value...
    # Getting value...
    # 37
    # Getting value...
    # 98.60000000000001
    # Setting value...
