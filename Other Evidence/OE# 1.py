class drmteam():
    def __init__(self, name, role, dmg_type):
        self.name = name
        self.role = role
        self.dmg_type = dmg_type

    def __str__(self):
        return f"{self.name} is a/an {self.role} with a {self.dmg_type} power."

    def describe(self):
        return self

char1 = drmteam("Joy", "assassin", "magic damage")
char2 = drmteam("Zhuxin", "mage", "magic damage")
char3 = drmteam("Lesley", "marksman", "physical damage")
char4 = drmteam("Phoveus", "fighter", "magic damage")
char5 = drmteam("Floryn", "support", "magic damage")

print(f'''
DREAM TEAM:
Hero: {char1.name}
Role: {char1.role}
Damage Type: {char1.dmg_type}
Description: {char1.describe()}

Hero: {char2.name}
Role: {char2.role}
Damage Type: {char2.dmg_type}
Description: {char2.describe()}

Hero: {char3.name}
Role: {char3.role}
Damage Type: {char3.dmg_type}
Description: {char3.describe()}

Hero: {char4.name}
Role: {char4.role}
Damage Type: {char4.dmg_type}
Description: {char4.describe()}

Hero: {char5.name}
Role: {char5.role}
Damage Type: {char5.dmg_type}
Description: {char5.describe()}
      ''')
