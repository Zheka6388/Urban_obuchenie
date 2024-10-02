
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


#h1 = House('Вавилон', 42)
#h2 = House('Шалаш', 2)

    def __len__(self): #
        return self.number_of_floors # возврат кол-ва этажей здания "self.number_of_floors".


    def __str__(self): #
        return (f'Название: {self.name}, '
            f'Кол-во этажей: {self.number_of_floors}') # возврат строки: "Название: <название>,
        # кол-во этажей: <этажи>".

h1 = House('Вавилон', 42)
h2 = House('Шалаш', 2)

print(h1) # __str__
print(h2) # __str__
print(len(h1)) # __len__
print(len(h2)) # __len__
