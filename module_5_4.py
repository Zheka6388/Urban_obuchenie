
class House: # класс "House".

    houses_history = [] # создаём пустой список, который будет хранить названия созданных объектов.

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0]) # Название строения можно взять из args по индексу.
        return object.__new__(cls) # возврат к объектам в списке

    def __init__(self, name, num_f): # функция "метод __init__" с параметрами: "название и кол-во этажей".
        self.name = name                # атрибут со значением "имя" (название).
        self.number_of_floors = num_f   # атрибут со значением "кол-во этажей".

    '''def go_to(self, new_floor): # функция "метод go_to" с параметром "new_floor".

        if int(new_floor) > int(self.number_of_floors) or int(new_floor) < 1: # если число "new_floor" > числа
            # "атрибут со значением "кол-во этажей"" или < 1, то f'Такого этажа не существует: {new_floor}'
                print(f'Такого этажа не существует: {new_floor}')

        else: # иначе

            for i in range(1, new_floor + 1): # присваиваем i последовательность от 1 с шагом +1.
                print(i)

    def __len__(self): #
        return self.number_of_floors # возврат кол-ва этажей здания "self.number_of_floors".
'''
    def __str__(self): #
        return (f'Название: {self.name}, '
            f'Кол-во этажей: {self.number_of_floors}') # возврат строки: "Название: <название>,
        # кол-во этажей: <этажи>"

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')



h1 = House('Вавилон', 12)
print(House.houses_history)
h2 = House('Шалаш', 2)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)


