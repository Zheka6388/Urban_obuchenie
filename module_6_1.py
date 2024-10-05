
class Animal: # родительский класс Animal
    alive = True # атрибут класса (живой)
    fed = False # атрибут класса (накормленный)

    def __init__(self, name): # функция "метод __init__" для  индивидуального названия каждого животного.
        self.name = name # атрибут со значением "имя" (название)

    def eat(self, food): # функция с методом  eat с параметром food (принимающий объекты классов растений).

        if food.edible == True: # если переданное растение (food) съедобное
            print(f'{self.name} съел {food.name}') #  выводит на экран "<self.name> съел <food.name>"
            self.fed = True # меняется атрибут fed на True

        else: # иначе

            self.alive = False # меняется атрибут alive на False
            print(f'{self.name} не стал есть {food.name}') # выводит на экран "<self.name> не стал есть <food.name>".

class Plant: # родительский класс Plant

    def __init__(self, name): # функция "метод __init__" 
        self.name = name # атрибут со значением "имя" (название)

    edible = False # переменный параметр "съедобный",находится в зоне видимости функции "метод __init__"

class Mammal(Animal): # наследуемый класс Mammal для Animal

    def eat(self, food): # обращение к функции def eat класса Animal

        return Animal.eat(self, food) # возврат к функции def eat класса Animal

class Predator(Animal): # наследуемый класс Predator для Animal

    def eat(self, food): # обращение к функции def eat класса Animal

        return Animal.eat(self, food) # возврат к функции def eat класса Animal

class Flower(Plant): # наследуемый класс Flower для Plant

     pass  # заглушка, чтобы не было ошибки при обращении к a1.eat(p1), можно будет дополнить условием позже

class Fruit(Plant): # наследуемый класс Fruit для Plant

    edible = True # атрибут edible = True для каждого объекта Fruit, для изменения значения
    # edible по отношению к  методу __init__ class Plant


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive) # по условию атрибутов class Animal
print(a2.fed) # по условию атрибутов class Animal
a1.eat(p1) # обращение к функции  def eat
a2.eat(p2) # обращение к функции  def eat
print(a1.alive) # по условию функции def eat
print(a2.fed) # по условию функции def eat

# (параметр self для обращения к атрибутам объекта текущего класса)
