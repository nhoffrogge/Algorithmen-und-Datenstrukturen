import string
from dataclasses import dataclass, field

# Basic method of setting and getting attributes on Python

class Celsius:
    def __init__(self, temperature=0):
        #self.temperature = temperature
        self.set_temperature(temperature)
        
    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32
    
# Making Getters and Setters methods

# getter method
    def get_temperature(self):
        print(self._temperature)
        return self._temperature

    
# setter method
    def set_temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible.")
        self._temperature = value
        
# creating a property object
temperature = property(get_temperature, set_temperature)
    
# Create a new object, set_temperature() internally called by __init()__
human = Celsius(37)

print(human.temperature)
print(human.to_fahrenheit())

human.temperature = -300

# Get the temperature attribute via getter
#print(human.get_temperature())

# Get the fahrenheit method, get_temperature() called by the method itself
#print(human.to_fahrenheit())

# new constraint implementation
#human.set_temperature(-300)

# Get the to_fahrenheit method
#print(human.to_fahrenheit())
