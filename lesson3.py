class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.health = 100
        self.is_alive = True

    def info(self):
        print("Ім'я:", self.name)
        print("Вік:", self.age)
        print("HP:", self.health)
        print("Живий:", "Так" if self.is_alive else "Ні")

    def sound(self):
        print("Тварина видає звук")

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            self.is_alive = False
            print(self.name, "помер")
        else:
            print(self.name, "отримав", damage, "шкоди. HP:", self.health)


class WildAnimal(Animal):
    def __init__(self, name, age, power):
        super().__init__(name, age)
        self.power = power

    def hunt(self, prey):
        if not self.is_alive:
            print(self.name, "мертвий і не може полювати")
            return
        if not prey.is_alive:
            print(prey.name, "вже мертвий, нема сенсу полювати")
            return
        print(self.name, "полює на", prey.name)
        damage = self.power
        prey.take_damage(damage)


class Predator(WildAnimal):
    def __init__(self, name, age, power, claw_damage):
        super().__init__(name, age, power)
        self.claw_damage = claw_damage

    def hunt(self, prey):
        if not self.is_alive:
            print(self.name, "мертвий")
            return
        if not prey.is_alive:
            print(prey.name, "вже мертвий")
            return
        total_damage = self.power + self.claw_damage
        print(self.name, "атакує кігтями", prey.name, "на", total_damage, "шкоди")
        prey.take_damage(total_damage)

    def roar(self):
        print(self.name, "грізно реве")


class Herbivorous(WildAnimal):
    def __init__(self, name, age, power, speed):
        super().__init__(name, age, power)
        self.speed = speed

    def run_away(self):
        print(self.name, "тікає зі швидкістю", self.speed)

    def hunt(self, prey):
        print(self.name, "не їсть м'ясо, травоїдний")


class Lion(Predator):
    def __init__(self, name, age, power, claw_damage, mane_size):
        super().__init__(name, age, power, claw_damage)
        self.mane_size = mane_size

    def sound(self):
        print(self.name, "гучно реве: Рррр!")

    def info(self):
        super().info()
        print("Розмір гриви:", self.mane_size)


class Tiger(Predator):
    def __init__(self, name, age, power, claw_damage, stripes):
        super().__init__(name, age, power, claw_damage)
        self.stripes = stripes

    def sound(self):
        print(self.name, "гарчить: Рррр!")

    def info(self):
        super().info()
        print("Кількість смуг:", self.stripes)


class Wolf(Predator):
    def __init__(self, name, age, power, claw_damage, pack_size):
        super().__init__(name, age, power, claw_damage)
        self.pack_size = pack_size

    def sound(self):
        print(self.name, "виє: Аууу")

    def info(self):
        super().info()
        print("Розмір зграї:", self.pack_size)

    def pack_hunt(self, prey):
        print("Зграя з", self.pack_size, "вовків полює на", prey.name)
        total_damage = (self.power + self.claw_damage) * self.pack_size
        prey.take_damage(total_damage)


class Wildebeest(Herbivorous):
    def __init__(self, name, age, power, speed, herd_size):
        super().__init__(name, age, power, speed)
        self.herd_size = herd_size

    def sound(self):
        print(self.name, "мукає: Мууу")

    def info(self):
        super().info()
        print("Розмір стада:", self.herd_size)


class Hare(Herbivorous):
    def __init__(self, name, age, power, speed, ear_length):
        super().__init__(name, age, power, speed)
        self.ear_length = ear_length

    def sound(self):
        print(self.name, "пищить: Пі-пі-пі!")

    def info(self):
        super().info()
        print("Довжина вух:", self.ear_length)

    def hide(self):
        print(self.name, "ховається в кущах")


class Deer(Herbivorous):
    def __init__(self, name, age, power, speed, antler_size):
        super().__init__(name, age, power, speed)
        self.antler_size = antler_size

    def sound(self):
        print(self.name, "трубить: І-го-го!")

    def info(self):
        super().info()
        print("Розмір рогів:", self.antler_size)

    def kick(self):
        print(self.name, "б'є копитом")


print("Система полювання")

lion = Lion("Лев", 5, 40, 25, "велика")
tiger = Tiger("Тигр", 4, 45, 30, "95")
wolf = Wolf("Вовк", 3, 30, 20, 5)

wildebeest = Wildebeest("Антілопа", 2, 10, 80, 20)
hare = Hare("Заєць", 1, 5, 90, 15)
deer = Deer("Олень", 3, 12, 70, 30)

print("\nІнформація про хижаків")
for predator in [lion, tiger, wolf]:
    predator.info()
    predator.sound()

print("\nІнформація про травоїдних")
for herb in [wildebeest, hare, deer]:
    herb.info()
    herb.sound()

print("\nСистема полювання")
lion.hunt(wildebeest)
tiger.hunt(deer)
wolf.pack_hunt(hare)
hare.hide()
deer.kick()


class BankAccount:
    def __init__(self, money):
        self.money = money

    def withdraw(self, amount):
        if amount == 0:
            raise ValueError("Сума зняття не може дорівнювати 0")

        if amount < 0:
            raise ValueError("Не можна знімати мінус")

        if amount > self.money:
            credit = amount - self.money
            print(f"Не вистачає {credit} грн")
            days = int(input("На скільки днів взяти кредит? "))

            if days <= 30:
                percent = credit * 0.01 * days
                rate = "1%"
            else:
                percent = credit * 0.04
                rate = "4%"

            answer = input(f"Взяти кредит {credit} грн під {rate} (відсотки: {percent} грн)? (так/ні): ")

            if answer.lower() == "так":
                self.money += credit
                self.money -= percent
                self.money -= amount
                print(f"Знято {amount}. Залишок: {self.money}")
            else:
                print("Кредит відхилено")
            return

        self.money -= amount
        print("Знято:", amount)
        print("Залишок:", self.money)

    def add_money(self, amount):
        if amount < 0:
            raise ValueError("Не можна додати від'ємну суму")
        self.money += amount
        print("Додано:", amount)
        print("Залишок:", self.money)


account = BankAccount(100)

try:
    take = int(input("\nСкільки зняти? "))
    account.withdraw(take)

except ValueError as e:
    print("Помилка:", e)