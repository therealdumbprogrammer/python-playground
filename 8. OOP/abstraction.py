# Define an Abstract Animal Class:
# Abstract Method: make_sound() that returns the sound the animal makes.
# Define Subclasses Dog and Cat that Inherit from Animal:
# Implement the make_sound() Method:
# Dog: Returns "Woof!"
# Cat: Returns "Meow!"
# Create Instances of Dog and Cat and Call Their make_sound() Methods:
# Print the returned sounds to the console.

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"
    
d = Dog()
print(d.make_sound())