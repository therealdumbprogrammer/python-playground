# Define a Car class:

# Attributes: make, model, year.
# Method: description() that returns a formatted string with car details.
# Create two instances of Car:

# Example: car1 and car2 with different attributes.
# Call the description() method on both instances and print the results.

class Car:
    def __init__(self, make, model, year) -> None:
        self.make = make
        self.model = model
        self.year = year

    def description(self):
        print(f"{self.model} {self.make} {self.year}")


honda = Car("Honda", "City", 2018)
honda.description()

kia = Car("Kia", "Sonnet", 2023)
kia.description()