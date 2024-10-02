class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f'{self.name} рычит')

    def eat(self):
        print(f'{self.name} кушает')

class Bird(Animal):
    def __init__(self,name, age, color):
        super().__init__(name, age)
        self.color = color

    def make_sound(self):
        print(f'{self.name} чирикает')

class Mammal(Animal):
    def __init__(self, name, age, sort):
        super().__init__(name, age)
        self.sort = sort

    def make_sound(self):
        print(f'{self.name} мычит')

class Reptile(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print(f'{self.name} шипит')

def animal_sound(animals):
    for animal in animals:
     animal.make_sound()

animals = [Bird('воробей', 4, 'коричневый'), Mammal('корова', 5, 'травоядное'), Reptile('варан', 20)]

animal_sound(animals)
