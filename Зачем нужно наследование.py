# Родительский класс для животных
class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False

    # Общий метод для всех животных
    def eat(self, food):
        if isinstance(food, Plant):  # Проверяем, что еда является растением
            if food.edible:
                print(f"{self.name} съел {food.name}")
                self.fed = True
            else:
                print(f"{self.name} не стал есть {food.name}")
                self.alive = False  # Животное погибает от несъедобного растения

# Родительский класс для растений
class Plant:
    def __init__(self, name):
        self.name = name
        self.edible = False

# Класс для млекопитающих, наследуется от Animal
class Mammal(Animal):
    pass

# Класс для хищников, наследуется от Animal
class Predator(Animal):
    pass

# Класс для цветков, наследуется от Plant
class Flower(Plant):
    pass

# Класс для фруктов, наследуется от Plant
class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True  # Фрукты съедобные

# Пример работы программы
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

# Выводим имена животных и растений
print(a1.name)  # Волк с Уолл-Стрит
print(p1.name)  # Цветик семицветик

# Проверяем начальные значения alive и fed
print(a1.alive)  # True
print(a2.fed)    # False

# Попытка хищника съесть цветок и млекопитающего съесть фрукт
a1.eat(p1)       # Волк с Уолл-Стрит не стал есть Цветик семицветик
a2.eat(p2)       # Хатико съел Заводной апельсин

# Проверяем, что произошло с животными после попыток еды
print(a1.alive)  # False (хищник погиб от несъедобного растения)
print(a2.fed)    # True (млекопитающее насытилось съедобным фруктом)
