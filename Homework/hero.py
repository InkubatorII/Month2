
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
