# Define a Vehicle class:

# Attributes: make, model.
# Method: vehicle_info() that returns a formatted string with vehicle details.
# Define a Car subclass that inherits from Vehicle:

# Additional Attribute: year.
# Override the vehicle_info() method to include the year.
# Create instances of Vehicle and Car and display their information using the vehicle_info() method.

class Vehicle:
    def __init__(self, make:str, model:str) -> None:
        self._make = make
        self._model = model

    def vehicle_info(self) -> str:
        return f"Vehicle {self._make} {self._model}"
    

class Car(Vehicle):
    def __init__(self, make: str, model: str, year:int) -> None:
        super().__init__(make, model)
        self._year = year

    def vehicle_info(self) -> str:
        return f"Car {self._make} {self._model} {self._year}"
    

veh = Vehicle("Honda", "Amaze")
kia = Car("Kia", "Sonnet", 2023)

print(veh.vehicle_info())
print(kia.vehicle_info())
