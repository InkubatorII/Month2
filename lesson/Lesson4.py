# принципы ООП, инкапсуляция, абстракция, множественное наследование
# супер класс - Object
from Lesson3 import Nowella

#наследование
# class Manga(Nowella):...
#
# manga = Manga('Берсерк', 'кентаро миура', 2500, '70x70')
# manga.reads()
# print(manga)

#полиморфизм
class Manga(Nowella):
    def reads(self):
        print(f'я люблю мангу: {self.title} ')

manga = Manga('Берсерк', 'кентаро миура', 2500, '70x70')
manga.reads()
print(manga)

# MRO - metod resolution order / порядок выполнения методов
print(Manga.mro())


#  инкапсуляция

class Anime: ...

print(Anime.mro())