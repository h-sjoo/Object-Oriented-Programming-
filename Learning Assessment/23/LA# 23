class AnimeCharacter:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability
    def introduce(self, func):
        def char_name(*args, **kwargs):
            print(f"Introducing...")
            func(*args, **kwargs)
            print(f"This character is amazing!")
        return char_name
       
anime = AnimeCharacter("Akame", "Murasame")
@anime.introduce
def intro(name, ability):
    print(f"I am {name} I have {ability}")
intro("Nobara Kugisaki", "Straw Doll Technique")
