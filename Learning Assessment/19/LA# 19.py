class Adobi:
    def __init__(self, chimken, toyo, vinegar, laurel,):
        self.__chimken = chimken
        self._toyo = toyo
        self.__vinegar = vinegar
        self.__laurel = laurel
    def __str__(self):
        return f"My Adobi needs {self.__chimken} and {self._toyo} and {self.__vinegar} also {self.__laurel}"

mixed = Adobi("Breast Fillet", "Datung puti toyo", "Datung puti suka", "Laurel")
print(mixed.__laurel)