class Item:
    def __init__(self, name):
        self.name = name

class Character:
    def __init__(self, name, level, HP):
        self.name = name
        self.level = level
        self.HP = HP
        self.inventory = []


    def info(self):
        print('Імя:',self.name)
        print('Рівень:', self.level)
        print('Здоровя:', self.HP)

    def rest(self):
        self.HP += 10
        print(self.name, 'Відпочив і відновив здоровя. Тепер HP:', self.HP)

    def add_item(self, item):
        self.inventory.append(item)

    def show_inventory(self):
        print('Інвентар ben|den|pen:')
        if len(self.inventory) == 0:
            print('Порожній')
        else:
            for item in self.inventory:
                print(item.name)

class Warrior(Character):
    def __init__(self, name, level, HP, strength):
        super().__init__(name, level, HP)
        self.strength = strength

    def attack(self, enemy):
        damage = self.strength + 10
        enemy.HP -= damage
        print(self.name, 'б,є (-30HP)')

    def shield(self):
        print(self.name, 'використовує щит')

class Mage(Character):
    def __init__(self, name, level, HP, mana):
        super().__init__(name, level, HP)
        self.mana = mana

    def attack(self, enemy):
        if self.mana >= 10:
            self.mana -= 10
            enemy.HP -=20
            print(self.name, 'використовує магію (-20HP)')
        else:
            print(self.name, 'нема мани')

    def teleport(self):
        print(self.name, 'телепортується')

class Archer(Character):
    def __init__(self, name, level, HP, energy):
        super().__init__(name, level, HP)
        self.energy = energy

    def attack(self, enemy):
        if self.energy >= 5:
            self.energy -= 5
            enemy.HP -=15
            print(self.name, 'стріляє (-20HP)')
        else:
            print(self.name, 'нема єнергії')

    def dodge(self):
        print(self.name, 'ухиляється')



hero1 = Warrior('Ben', 5, 100, 20, )
hero2 = Mage('Den', 7, 90, 30)
hero3 = Archer('Pen', 4, 70, 20)

heroes = [hero1, hero2, hero3]

for hero in heroes:
    hero.info()
    hero.show_inventory()
    hero.rest()
    print('----------')

item1 = Item('Зілля регенерацї')
item2 = Item('Зілля сили')

print('Виберіть предмет:')
print('1 - Зілля регенерацї')
print('2 - Зілля сили')
choice = input('Ваш вибір: ')
print('-------------------')

if choice == '1':
    hero1.add_item(item1)
    hero2.add_item(item1)
    hero3.add_item(item1)
elif choice == '2':
    hero1.add_item(item2)
    hero2.add_item(item2)
    hero3.add_item(item2)
else:
    print('Немає такого предмета')

print('Бажаєта побачити інвентар ВСІХ персонажів??')
print('1 - Відкрити')
print('2 - Вихід')
choice2 = input('Ваш вибір: ')

if choice2 == '1':
    hero1.show_inventory()
    hero2.show_inventory()
    hero3.show_inventory()
elif choice2 == '2':
    print('Вихід')
else:
    print('Помилка')