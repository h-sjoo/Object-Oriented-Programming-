class Car():
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

car = Car("Toyota", "Red")
car.brand = "Honda"
car.color = "blue"

car1 = Car("Tesla", "White")

print(car.brand)
print(car.color)
print(car1.brand)
print(car1.color)
