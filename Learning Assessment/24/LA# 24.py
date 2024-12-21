from abc import ABC, abstractmethod
class GameCharacter(ABC):
    @abstractmethod
    def attack(self):
        pass

class Warrior(GameCharacter):
    def attack(self):
        print("Swings sword!")
       
class Mage(GameCharacter):
    def attack(self):
        print("Cast a fireball!")
       
class Archer(GameCharacter):
    def attack(self):
        print("Shoots an arrow!")

class Healer(GameCharacter):
    def attack(self):
        print("Healing for everyone!")

   
zilong = Warrior()
aurora = Mage()
miya = Archer()
rafaela = Healer()

zilong.attack()
aurora.attack()
miya.attack()
rafaela.attack()
