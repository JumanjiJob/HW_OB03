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
        print(f'{self.name} воет')

class Reptile(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print(f'{self.name} шипит')

def animal_sound(animals):
    for animal in animals:
     animal.make_sound()

class Zookeeper():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def feed_animal(self):
        print(f'{self.name} кормит животных')

class Veterinarian():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def heal_animal(self):
        print(f'{self.name} лечит животных')

class Zoo():
    def __init__(self, zookeeper, veterinarian):
        self.zookeeper = zookeeper
        self.veterinarian = veterinarian

    def info_people(self, people):
        print('\nСотрудники зоопарка: ')
        for human in people:
            if isinstance(human, Zookeeper):
                print(f'Имя - {human.name}, Возраст - {human.age}, Профессия - смотритель зоопарка')
            if isinstance(human, Veterinarian):
                print(f'Имя - {human.name}, Возраст - {human.age}, Профессия - ветеринар')

    def info_animals(self, animals):
        print('\nЖивотные зоопарка: ')
        for animal in animals:
            if isinstance(animal, Bird):
                print(f'Вид - {animal.name}, Возраст - {animal.age}, Цвет - {animal.color}')
            if isinstance(animal, Mammal):
                print(f'Вид - {animal.name}, Возраст - {animal.age}, Вид - {animal.sort}')
            if isinstance(animal, Reptile):
                print(f'Вид - {animal.name}, Возраст - {animal.age}')
    def add_human(self, human, people):
        people.append(human)
        return print(f'{human.name} успешно добавлен в список сотрудников зоопарка')

    def remove_human(self, human, people):
        people.remove(human)
        return print(f'{human.name} успешно удален из списка сотрудников зоопарка')

    def add_animal(self, animal, animals):
        animals.append(animal)
        return print(f'{animal.name} успешно добавлен в список животных зоопарка')

    def remove_animal(self, animal, animals):
        animals.remove(animal)
        return print(f'{animal.name} успешно удален из списка животных зоопарка')

vet1 = Veterinarian('Ted', 24)
vet2 = Veterinarian('Arnold', 50)
keeper1 = Zookeeper('Mike', 42)
keeper2 = Zookeeper('Lia', 19)
animal1 = Bird('воробей', 4, 'коричневый')
animal2 = Mammal('волк', 5, 'хищник')
animal3 = Reptile('варан', 20)
zoo = Zoo(keeper1, vet1)

people = []
zoo.add_human(vet1, people)
zoo.add_human(vet2, people)
zoo.add_human(keeper1, people)
zoo.add_human(keeper2, people)
zoo.remove_human(vet2, people)

animals = []
zoo.add_animal(animal1, animals)
zoo.add_animal(animal2, animals)
zoo.add_animal(animal3, animals)
zoo.remove_animal(animal1, animals)
animal_sound(animals)

zoo.info_people(people)
zoo.info_animals(animals)


