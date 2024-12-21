class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, target):
        target.health -= self.power
        print(f"{self.name} attacks {target.name}!, {self.name} deals {target.name} damage, {target.name} now has only {target.health}")

    def special_move(self):
        pass

    def defend (self, attacker):
        dmg_taken = attacker.power * 0.9
        self.health -= dmg_taken
        print(f"{self.name} defends against {attacker.name}'s attack. {self.name}'s health is now {self.health}.")

class Warrior(Character):
    def special_move(self, target):
        self.power *= 2
        print(f"{self.name} uses Shield Bash!")

class Mage(Character):
    def special_move(self, target):
        target.health -= 100
        print(f"{self.name} casts Fireball! {target.name}'s health is reduced by 100.")

class Archer(Character):
    def special_move(self, target):
        target.health -= self.power * 1.5
        print(f"{self.name} shoots a Piercing Arrow! {target.name}'s health is reduced by 1.5 times than the normal damage.")

class Monster(Character):
    def special_move(self, target):
        target.health += 50
        print(f"{self.name} roars and gains 50 health.")

warrior = Warrior("Warrior", 100, 20)
mage = Mage("Mage", 80, 15)
archer = Archer("Archer", 70, 25)
monster = Monster("Monster", 250, 30)

characters = [warrior, mage, archer]

while True:
    for attacker in characters:
        attacker.attack(monster)
        attacker.special_move(monster)
        monster.defend(attacker)

        if monster.health <= 0:
            print("Monster defeated!")
    break

    for character in characters:
        monster.attack(character)
        monster.special_move(character)
        character.defend(monster)

    if character.health <= 0:
        print(f"{character.name} is defeated!")
        characters.remove(character)
    break

    if not characters:
        print("Monster wins!")
    break
