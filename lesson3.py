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