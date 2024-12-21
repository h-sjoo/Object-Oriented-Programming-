class Vehicle():
    def __init__(self, brand, model, fuel_type):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type
    def describedVehicle(self):
        print(f"{self.brand} is a {self.model} with a {self.fuel_type} type of gas")

class Car(Vehicle):
    pass
Nissan = Car("Nissan", "Rogue", "Premium")
Nissan.describedVehicle()
class Motorcycle(Vehicle):
    pass
Honda = Motorcycle("Honda", "RS125", "Diesel")
Honda.describedVehicle()
