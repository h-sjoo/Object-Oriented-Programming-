class Animal():
    def __init__(self, name, type):
        self.name = name
        self.type = type
    def describedAnimal(self):
        print(f"{self.name} is {self.type} with a {self.can_swim}")
       
class Fish(Animal):
    def __init__(self, name, type):
        super().__init__(name, type)
        self.can_swim = True
       
Tilapia = Fish("Tilapia", "Garfish")
print(Tilapia.can_swim)
