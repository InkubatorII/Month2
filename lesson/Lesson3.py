# Приципы ООП, Git clone
# Наследование, полиморфизм, инкапсуляция, абстракция

#DRY - главное правило: "не повторяйся"

# супер либо родительский класс
class Book:
    def __init__(self, title, author, price):
        self.title=title
        self.author=author
        self.price=price
    def reads(self):
        print('я читаю книгу под авторством', self.author)

    def __str__(self):
        return (f'Название: {self.title}\n'
                f'Автор: {self.author}\n'
                f'Цена: {self.price}\n')

tamirlan=Book('Bleach', 'Tamirlan', 2500)
print(tamirlan)
tamirlan.reads()
# Дочерний класс
class Nowella(Book):

    def __init__(self, title, author, price, png):
        Book.__init__(self,title,author,price)
        self.png=png

    def __str__(self):

        return (f'{super().__str__()}'
                f'Размер картинки: {self.png}')

    def reads(self):
        print('я читаю книгу под авторством', self.author, 'и я купил ее за', self.price)

dan = Nowella('Naruto', 'Dan', 2000, '70x20')
print(dan)
dan.reads()