class Spiderman:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def describeSpiderman(self):
        print(f"He is {self.name} and {self.age}")

class Tobey(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age)
        self.movieTitle = movieTitle

class Andrew(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age)
        self.movieTitle = movieTitle
   
class Tom(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age)
        self.movieTitle = movieTitle
   
sp1 = Tobey("Tobey", 18, "Spiderman 1")
print("Name: ",sp1.name.upper(), "\nMovie:", sp1.movieTitle)
sp2 = Andrew("Andrew", 21, "Spiderman 2")
print("\nName: ",sp2.name.upper(),"\nMovie:", sp2.movieTitle)
sp3 = Tom("Tom", 28, "Homecoming")
print("\nName: ", sp3.name.upper(),"\nMovie:", sp3.movieTitle)
