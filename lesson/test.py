class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def get_name(self):
        return self.name

    def double_health(self):
        self.health_points *= 2

    def __str__(self):
        return f"Nickname: {self.nickname}, Superpower: {self.superpower}, Health: {self.health_points}"

    def __len__(self):
        return len(self.catchphrase)

# Наследники от SuperHero

class AirHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def double_health(self):
        self.health_points **= 2
        self.fly = True

    def true_phrase(self):
        return "True in the True_phrase"

class EarthHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def double_health(self):
        self.health_points **= 2
        self.fly = True

    def true_phrase(self):
        return "True in the True_phrase"

# Создаем объекты классов AirHero и EarthHero и применяем методы

air_hero = AirHero(name="Peter", nickname="SkyMaster", superpower="Control Wind", health_points=80, catchphrase="Fly high!", damage=30)
earth_hero = EarthHero(name="Bruce", nickname="RockMan", superpower="Earthquake", health_points=120, catchphrase="Solid as a rock!", damage=50)

# Применяем методы
air_hero.double_health()
earth_hero.double_health()

print(air_hero)                  # Вывод информации о герое
print(earth_hero)                # Вывод информации о герое

print(air_hero.true_phrase())    # Вывод фразы от воздушного героя
print(earth_hero.true_phrase())  # Вывод фразы от земного героя

# Создаем класс Villain, наследованный от EarthHero

class Villain(EarthHero):
    people = 'monster'

    def gen_x(self):
        pass  # Метод пока ничего не делает

    def crit(self):
        return self.damage ** 2

# Создаем объект класса Villain и применяем методы

villain = Villain(name="Loki", nickname="God of Mischief", superpower="Illusion", health_points=100, catchphrase="Trickster!", damage=40)

print(villain.crit())            # Возводим урон в квадрат
