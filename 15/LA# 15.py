class Dog:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name}: bark")
       
class Cat:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name}: meow")
       
class Bird:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name}: chirp")
       
class Fish:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name}: is ...")

def animal_sounds(animal):
    animal.speak
       
dog = Dog("Shiztsu")
cat = Cat("Siamese")
bird = Bird("Maya")
fish = Fish("Goldfish")

animals = [dog, cat, bird, fish]

for animal in [dog, cat, bird, fish]:  
    animal.speak()
