from math import inf # импорт из встроенной библиотеки math бесконечности inf.

def divide(first, second): # функция "деления" с параметрами "первый", "второй".

    if second != 0: # если second не равен 0, то
        f = first/second # результат деления first на second

        return f # возврат результата деления first на second

    else: # иначе

        return inf # возврат бескогнчности


result3 = divide(49, 7)
result4 = divide(15, 0)
print(result3)
print(result4)