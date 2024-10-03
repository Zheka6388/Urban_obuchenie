
class House:                                       # класс "House".



    def __init__(self, name, num_f): # функция "метод __init__" с параметрами: "название и кол-во этажей".
        self.name = name                # атрибут со значением "имя" (название).
        self.number_of_floors = num_f   # атрибут со значением "кол-во этажей".

    def go_to(self, new_floor): # функция "метод go_to" с параметром "new_floor".

        if int(new_floor) > int(self.number_of_floors) or int(new_floor) < 1: # если число "new_floor" > числа
            # "атрибут со значением "кол-во этажей"" или < 1, то f'Такого этажа не существует: {new_floor}'
                print(f'Такого этажа не существует: {new_floor}')

        else: # иначе

            for i in range(1, new_floor + 1): # присваиваем i последовательность от 1 с шагом +1.
                print(i)

    def __len__(self): #
        return self.number_of_floors # возврат кол-ва этажей здания "self.number_of_floors".

    def __str__(self): #
        return (f'Название: {self.name}, '
            f'Кол-во этажей: {self.number_of_floors}') # возврат строки: "Название: <название>,
        # кол-во этажей: <этажи>"

    def __eq__(self, other):  # метод сравнения __eq__, возвращает True, если количество
        # этажей одинаковое у self и у other
        if isinstance(other.number_of_floors, int) and isinstance(other, House): # если атрибут со
            # значением "кол-во этажей" - тип int и указывает на объект типа House
            return self.number_of_floors == other.number_of_floors # возврат результата сравнения


    def __lt__(self, other):  # метод сравнения __lt__(<)
        if isinstance(other.number_of_floors, int) and isinstance(other, House): # если атрибут со
            # значением "кол-во этажей" - тип int и указывает на объект типа House
            return self.number_of_floors < other.number_of_floors # возврат результата сравнения


    def __le__(self, other): # метод сравнения __le__(<=)
        if isinstance(other.number_of_floors, int) and isinstance(other, House): # если атрибут со
            # значением "кол-во этажей" - тип int и указывает на объект типа House
            return self.number_of_floors <= other.number_of_floors # возврат результата сравнения


    def __gt__(self, other): # метод сравнения __gt__(>)
        if isinstance(other.number_of_floors, int) and isinstance(other, House): # если атрибут со
            # значением "кол-во этажей" - тип int и указывает на объект типа House
            return self.number_of_floors > other.number_of_floors # возврат результата сравнения


    def __ge__(self, other): # метод сравнения __ge__(>=)
        if isinstance(other.number_of_floors, int) and isinstance(other, House): # если атрибут со
            # значением "кол-во этажей" - тип int и указывает на объект типа House
            return self.number_of_floors >= other.number_of_floors # возврат результата сравнения


    def __ne__(self, other): # метод сравнения  __ne__(!=)
        if isinstance(other.number_of_floors, int) and isinstance(other, House): # если атрибут со
            # значением "кол-во этажей" - тип int и указывает на объект типа House
            return self.number_of_floors != other.number_of_floors # возврат результата сравнения


    def __add__(self, value): # метод сравнения __add__(+)- увеличивает кол-во этажей на
        # переданное значение value, возвращает сам объект self
        if isinstance(value, int): #
            self.number_of_floors = self.number_of_floors + value # прибавляет к начальному значению число
        return self # возврат значения self


    def __radd__(self, value): # метод сравнения __radd__(+), прибавляет числовое значение к предидущей
        # операции __add__
         return self.__add__(value) # возврат значения self.__add__


    def __iadd__(self, value): # метод сравнения __iadd__(+=), прибавляет числовое значение к предидущей
        # операции __radd__
        if isinstance(value, int): #
            self.number_of_floors += value # прибавляет числовое значение к предидущей операции __radd__
        return self #


h1 = House('Вавилон', 42)
h2 = House('Шалаш', 2)

print(h1)
print(h2)

print(h1 == h2) # __eq__
print(h1 < h2) # __lt__(<)
print(h1 <= h2) # __le__(<=)
print(h1 > h2) # __gt__(>)
print(h1 >= h2) # __ge__(>=)
print(h1 != h2) #  __ne__(!=)

print(h1.__add__(3)) # прибавляет к начальному значению число 3
print(h2.__add__(4)) # прибавляет к начальному значению число 4
print(h1.__radd__(7)) # прибавляет числовое значение к предидущей операции __add__ (h1)
print(h2.__radd__(8)) # прибавляет числовое значение к предидущей операции __add__ (h2)
print(h1.__iadd__(5)) # прибавляет числовое значение к предидущей операции __radd__ (h1)
print(h2.__iadd__(6)) # прибавляет числовое значение к предидущей операции __radd__ (h2)
