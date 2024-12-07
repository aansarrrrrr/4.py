import random

class Human:
    def __init__(self, name="Human"):
        self.name = name
        self.money = 100
        self.happiness = 50
        self.hunger = 50
        self.food = 50
        self.car_fuel = 100
        self.house_mess = 0

    def eat(self):
        if self.food > 0:
            print(f"{self.name} поел.")
            self.hunger += 10
            self.food -= 10
        else:
            print(f"У {self.name} нет еды! Нужно купить.")

    def work(self):
        print(f"{self.name} пошел работать.")
        self.money += 50
        self.happiness -= 5
        self.hunger -= 5
        self.car_fuel -= 10

    def relax(self):
        print(f"{self.name} отдыхает.")
        self.happiness += 10
        self.house_mess += 5

    def clean(self):
        print(f"{self.name} убрался в доме.")
        self.house_mess = 0
        self.happiness -= 5

    def shop(self, item):
        if item == "food":
            print(f"{self.name} купил еду.")
            self.food += 30
            self.money -= 30
        elif item == "fuel":
            print(f"{self.name} купил бензин.")
            self.car_fuel += 50
            self.money -= 50

    def status(self):
        print(f"\nДень {day}. Жизнь {self.name}:")
        print(f"Деньги: {self.money}, Счастье: {self.happiness}, Сытость: {self.hunger}")
        print(f"Еда дома: {self.food}, Бензин: {self.car_fuel}, Беспорядок: {self.house_mess}")

    def live(self):
        self.status()
        if self.hunger < 20:
            self.eat()
        elif self.car_fuel < 20:
            self.shop("fuel")
        elif self.money < 0:
            self.work()
        elif self.house_mess > 20:
            self.clean()
        else:
            action = random.choice(["work", "relax", "shop"])
            if action == "work":
                self.work()
            elif action == "relax":
                self.relax()
            elif action == "shop":
                self.shop("food")
        if self.happiness <= 0 or self.hunger <= 0 or self.money < -100:
            print(f"{self.name} не смог дальше жить...")
            return False
        return True


class Worker(Human):
    def __init__(self, name="Worker"):
        super().__init__(name)
        self.experience = 0  # Эксклюзивный атрибут для Worker

    def work(self):
        super().work()  # Используем метод work из родительского класса
        self.experience += 1  # Увеличиваем опыт при каждой работе
        print(f"{self.name} набрал {self.experience} опыта.")

    def status(self):
        super().status()
        print(f"Опыт работы: {self.experience}")  # Показываем опыт


class Traveler(Human):
    def __init__(self, name="Traveler"):
        super().__init__(name)
        self.traveled_distance = 0  # Эксклюзивный атрибут для Traveler

    def travel(self):
        if self.car_fuel >= 20:
            print(f"{self.name} отправился в путешествие.")
            self.traveled_distance += random.randint(50, 150)  # Путешествует на случайное расстояние
            self.car_fuel -= 20  # Тратим 20 литров бензина
        else:
            print(f"{self.name} не может поехать, не хватает бензина.")

    def status(self):
        super().status()
        print(f"Пройдено расстояние: {self.traveled_distance} км")  # Показываем пройденное расстояние


# Симуляция с разными персонажами
nick = Worker(name="Ник")  # Создаем рабочего
jane = Traveler(name="Джейн")  # Создаем путешественника

# Симуляция жизни
for day in range(1, 150):  # Симуляция 150 дней
    if not nick.live():
        break

for day in range(1, 150):  # Симуляция для путешественника
    if not jane.live():
        break
    if random.choice([True, False]):  # Путешествует или работает
        jane.travel()  # Джейн может путешествовать
