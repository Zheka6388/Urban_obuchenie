class StepValueError(ValueError): # пользовательский класс исключения, который наследуется от ValueError.
    pass


class Iterator:
    def __init__(self, start, stop, step=1): # принимающий значения старта и конца итерации, а также шага.
        if step == 0: #  в первую очередь проверяется step на равенство 0. Если равно, то выбрасывается
            # исключение StepValueError('шаг не может быть равен 0')
            raise StepValueError('шаг не может быть равен 0')
        self.start = start # целое число с которого начинается итерация.
        self.stop = stop  # целое число на котором заканчивается итерация.
        self.step = step  # шаг с которой совершается итерация.
        self.pointer = start # указывает на текущее число в итерации (изначально start)
        if step > 0: # если шаг итерации > 0
            self.step_designation = 1 # обозначаем шаг итерации = 1
        else: # иначе
            self.step_designation = -1 # обозначаем шаг итерации = -1

    def __iter__(self): # метод, сбрасывающий значение pointer на start и возвращающий сам объект итератора.
        self.pointer = self.start
        return self # возврат самого объекта итератора.

    def __next__(self): # метод, увеличивающий атрибут pointer на step
        if self.pointer * self.step_designation > self.stop * self.step_designation: #  В зависимости от
            # знака атрибута step итерация завершится либо когда pointer станет больше stop, либо меньше stop
            raise StopIteration() # признак того, что возвращать нечего
        pointer = self.pointer # переменная для указания значения
        self.pointer += self.step # прибавить к указанному значению шаг итерации
        return pointer # возврат атрибута pointer

# блок проверки на ошибки
try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1: # для i в iter1
        print(i, end=' ') # Значение по умолчанию для end — '\n', что означает, что print() будет
        # выводить символ новой строки после печати аргументов.
except StepValueError: # выбрасывается исключение ( из-за шага = 0)
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print() # -5 -4 -3 -2 -1 0 1: перебор значений от -5 до 1 по стопу

for i in iter3:
    print(i, end=' ')
print() # 6 8 10 12 14:  перебор значений от 6 до 14 по стопу в 15 из-за шага 2

for i in iter4:
    print(i, end=' ')
print() # 5 4 3 2 1:  перебор значений от 5 до 1 по стопу с шагом -1

for i in iter5:
    print(i, end=' ')
print()