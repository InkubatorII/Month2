# ООП
# принципы ООП:

class Book:
    strr = 400;

    #методы
    def __init__(self, title, author, color):
        self.title=title
        self.author=author
        self.color=color
    def info(self):
        print(self.title, self.author, self.color, self.strr)

    def __str__(self):
        return (f'Title: {self.title}, Author: {self.author}, \n'
                f'Color: {self.color}, Strr: {self.strr}')


    def __len__(self):
        return len(self.title + self.author + self.color)


# объект\экземпляр класса
город_воров = Book('город воров', 'чак хоган', 'зеленый')
капитанская_дочка = Book('капитанская_дочка', 'пушкин', 'серый')
print(город_воров.strr, город_воров.title, город_воров.author, город_воров.color )
print(город_воров)
print(капитанская_дочка)
город_воров.info()
капитанская_дочка.info()

beka=Book('Etomir', 'Beka', 'Black')
print(len(beka))




