class Player:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.inventory = []

    def attack(self, enemy):
        print(f"{self.name} атакує {enemy.name} і завдає {self.damage} шкоди")
        enemy.hp -= self.damage

    def add_item(self, item):
        self.inventory.append(item)
        print(f"Предмет '{item.name}' додано до інвентарю")

    def show_inventory(self):
        print("Інвентар")
        for item in self.inventory:
            print(f"- {item.name}: цінність {item.value}")

class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, player):
        print(f"{self.name} атакує {player.name} і завдає {self.damage} шкоди")
        player.hp -= self.damage

class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value

player = Player(name="Воїн", hp=100, damage=20)
enemy = Enemy(name="Гоблін", hp=60, damage=15)

item1 = Item(name="Зілля лікування", value=50)
item2 = Item(name="Старий меч", value=30)

player.add_item(item1)
player.add_item(item2)

player.show_inventory()

print(f"\nПочинається бій {player.name} vs {enemy.name}")
print(f"{player.name}: {player.hp} HP | {enemy.name}: {enemy.hp} HP\n")

while player.hp > 0 and enemy.hp > 0:
    player.attack(enemy)
    if enemy.hp <= 0:
        print(f"{enemy.name} переможений {player.name} виграв бій")
        break
    print(f"{enemy.name} має {enemy.hp} HP\n")

    enemy.attack(player)
    if player.hp <= 0:
        print(f"{player.name} загинув.. {enemy.name} переміг.")
        break
    print(f"{player.name} має {player.hp} HP\n")