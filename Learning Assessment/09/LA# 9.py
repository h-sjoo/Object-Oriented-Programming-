class Car():
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    def __str__(self):
        return f"The car is {self.brand} and color {self.color}"
       
Lambo = Car("Lambo", "Green")
print(Lambo)
del Lambo
print(Lambo)
