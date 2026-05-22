class Item:
    def __init__(self, name):
        self.name = name

class Character:
    def __init__(self, name, level, HP):
        self.name = name
        self.level = level
        self.HP = HP
        self.pack = []

    def info(self):
        print('Ім\'я:', self.name)
        print('Рівень:', self.level)
        print('Здоров\'я:', self.HP)

    def rest(self):
        self.HP += 10
        print(self.name, 'присів відпочити +10 ХП. Тепер:', self.HP)

    def add_item(self, item):
        self.pack.append(item)
        print(self.name, 'поклав у рюкзак:', item.name)

    def show_inventory(self):
        print('Рюкзак', self.name + ':')
        if len(self.pack) == 0:
            print('Порожньо')
        else:
            for item in self.pack:
                print('—', item.name)

class Warrior(Character):
    def __init__(self, name, level, HP, strength):
        super().__init__(name, level, HP)
        self.strength = strength

    def attack(self, enemy):
        damage = self.strength + 15
        enemy.HP -= damage
        print(self.name, 'розтрощує ворога мечем -', damage, 'ХП')

    def shield(self):
        print(self.name, 'піднімає велетенський щит')

class Mage(Character):
    def __init__(self, name, level, HP, spell_points):
        super().__init__(name, level, HP)
        self.spell_points = spell_points

    def attack(self, enemy):
        if self.spell_points >= 15:
            self.spell_points -= 15
            enemy.HP -= 25
            print(self.name, 'випускає магічний промінь -20 ХП')
        else:
            print(self.name, 'сил більше нема')

    def teleport(self):
        print(self.name, 'розчиняється в повітрі')

class Archer(Character):
    def __init__(self, name, level, HP, stamina):
        super().__init__(name, level, HP)
        self.stamina = stamina

    def attack(self, enemy):
        if self.stamina >= 7:
            self.stamina -= 3
            enemy.HP -= 20
            print(self.name, 'пускає стрілу в ціль -15 ХП')
        else:
            print(self.name, 'руки вже не тримають лук')

    def dodge(self):
        print(self.name, 'перекидається через голову')


hero1 = Warrior('Роберт', 3, 120, 30)
hero2 = Mage('Крістофф', 5, 105, 20)
hero3 = Archer('Альфред', 7, 85, 2)

heroes = [hero1, hero2, hero3]

for hero in heroes:
    hero.info()
    hero.rest()
item1 = Item('Корінь здоров\'я')
item2 = Item('Ягоди сили')

print('Виберіть предмет:')
print('1 - Корінь здоров\'я')
print('2 - Ягоди сили')
choice = input('Твій вибір: ')

if choice == '1':
    hero1.add_item(item1)
    hero2.add_item(item1)
    hero3.add_item(item1)
elif choice == '2':
    hero1.add_item(item2)
    hero2.add_item(item2)
    hero3.add_item(item2)
else:
    print('Нема такого')

print('Показати рюкзаки всіх?')
print('1 - Так')
print('2 - Ні')
choice2 = input('Твій вибір: ')

if choice2 == '1':
    hero1.show_inventory()
    hero2.show_inventory()
    hero3.show_inventory()
elif choice2 == '2':
    print('Бувай')
else:
    print('Помилка')