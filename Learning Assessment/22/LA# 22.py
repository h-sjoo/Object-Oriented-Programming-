class bdayp:
    def __init__(self, theme, food):
        self.theme = theme
        self.food = food
    def __foods(self):
        print(f"Theme: {self.theme}")
        print(f"Secret dish: {self.food}")
    def secret(self):
        print("Birthday foods: Chimken, Sinigang, Lechon")
        self.__foods()
       
theme1 = bdayp("Euphoria", "Adobi")
theme1.secret()
print("")
theme2 = bdayp("Hollywood", "Menudo")
theme2.secret()
print("")
theme3 = bdayp("Dinosaur", "Sisig")
theme3.secret()
