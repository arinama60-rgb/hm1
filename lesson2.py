class Character:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def info(self):
        print("Имя:", self.name)
        print("Рівень:", self.level)

player1 = Character(name="Knight", level=5)

player1.info()

class Weapon:
    def __init__(self, name, demage):
        self.name = name
        self.demage = demage

    def info(self):
        print("Зброя:", self.name)
        print("Шкода:", self.demage)

player1 = Weapon(name="Iron Sword", demage=25)

player1.info()




class Character:
    def __init__(self, name, level, weapon, armor):
        self.name = name
        self.level = level

        self.weapon = weapon
        self.armor = armor

        self.health = 100


    def show_stats(self):
        print("Имя:", self.name)
        print("НР:", self.health)
        print("Зброя:", self.weapon.name)
        print("Броня:", self.armor.name)

class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class Armor:
    def __init__(self, name, defense):
        self.name = name
        self.defense = defense

armor1 = Armor(name="Iron Armor", defense=15)
armor2 = Armor(name="Golden Armor", defense=25)
armor3 = Armor(name="Diamond Armor", defense=40)

weapon1 = Weapon(name="Steel Sword", damage=30)

player = Character(name="Warrior", level=8, weapon=weapon1, armor=armor1)

player.show_stats()