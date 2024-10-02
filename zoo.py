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

    def add_human(self, human, people):
        people.append(human)
        return print(f'{human.name} успешно добавлен в список сотрудников зоопарка')

    def remove_human(self, human, people):
        people.remove(human)
        return print(f'{human.name} успешно удален из списка сотрудников зоопарка')

vet1 = Veterinarian('Ted', 24)
vet2 = Veterinarian('Arnold', 50)
keeper1 = Zookeeper('Mike', 42)
keeper2 = Zookeeper('Lia', 19)

people = []
zoo = Zoo(keeper1, vet1)
zoo.add_human(vet1, people)
zoo.add_human(vet2, people)
zoo.add_human(keeper1, people)
zoo.add_human(keeper2, people)
zoo.remove_human(vet2, people)

zoo.info_people(people)