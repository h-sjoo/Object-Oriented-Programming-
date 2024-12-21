class Phone():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def describedPhone(self):
        print(f"{self.brand} is a {self.model} model")
       
class Android(Phone):
        def __init__(Phone):
            Phone.__init__(self, brand, model)

Apple = Phone("Apple", "Xr")        
Apple.describedPhone()
