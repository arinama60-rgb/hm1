class Student:
    def __init__(self, name, age, subjects):
        self.name = name
        self.age = age
        self.subjects = subjects
        self.money = 500
        self.knowledge = 50
        self.energy = 70
        self.day = 0
        print(f"Мене звати {self.name}, мені {self.age} років")

    def __len__(self):
        return len(self.subjects)

    def work(self):
        if self.energy >= 20:
            self.money += 200
            self.energy -= 20
            print(f"Попрацював. Грошей: {self.money}, Енергія: {self.energy}")
        else:
            print("Немає сил працювати")

    def rest(self):
        if self.money >= 100:
            self.money -= 100
            self.energy += 30
            print(f"Відпочив. Грошей: {self.money}, Енергія: {self.energy}")
        else:
            print("Немає грошей на відпочинок")
            self.energy += 10

    def study(self):
        if self.energy >= 15:
            self.knowledge += 10
            self.energy -= 15
            print(f"Повчився. Знання: {self.knowledge}, Енергія: {self.energy}")
        else:
            print("Втомився, не може вчитися")

    def live_day(self):
        self.day += 1
        print(f"\nДень {self.day}")

        if self.money < 100:
            print("Мало грошей, тому йде працювати")
            self.work()
        elif self.knowledge < 40:
            print("Проблеми з навчанням, тому вчиться")
            self.study()
        elif self.energy < 30:
            print("Втомився, тому відпочиває")
            self.rest()
        else:
            if self.money < 300:
                self.work()
            elif self.knowledge < 70:
                self.study()
            else:
                self.rest()

        if self.energy > 100:
            self.energy = 100
        if self.knowledge > 100:
            self.knowledge = 100

    def live_year(self):
        while self.day < 365:
            self.live_day()
        print("\nРік прожито")
        print(f"Підсумок — Грошей: {self.money}, Знання: {self.knowledge}, Енергія: {self.energy}")


s1 = Student("Макс", 16, ["математика", "англ", "біологія"])
print("Кількість предметів:", len(s1))
s1.live_year()