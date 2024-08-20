
class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase
    def name(self):
        return (f'name: {self.name}')
    def double(self):
        self.health_points *= 2
    def __str__(self):
        return f"Nickname: {self.nickname}, Superpower: {self.superpower}, Health Points: {self.health_points}"
    def __len__(self):
        return len(self.catchphrase)

spider_man = SuperHero("Piter Parker","Spider Man","WEB",100,"With great power comes great responsibility"
)
print(spider_man.name)
spider_man.double()
print(spider_man)
print(len(spider_man))

class Сosmic(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage=damage
        self.fly=fly

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


silver_surfer = Сosmic('Норрин Радд', 'Серебряный Серфер', 'Сила Космоса',150,
                       'Я серебряный сёрфер, куда он несёт?',200)
halk = EarthHero("Брюс Беннер", "Халк","Супер Мощь", 120, "Рот на замок, и ножками",200)

print(silver_surfer.name)
silver_surfer.double_health()
print(silver_surfer)
print(halk.name)
halk.double_health()
print(halk)

class Villain(EarthHero):
    people = 'monster'

    def gen_x(self):
        pass

    def crit(self):
        return self.damage ** 2


loki = Villain("Локи","Бог Обмана", "Иллюзии", 100, "Обманщик", 50)
print(loki)
print(loki.crit())



