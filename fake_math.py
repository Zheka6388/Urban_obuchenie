
def divide(first, second): # функция "divide" со значениями: "first", "second"

    if second != 0: # если second не равен 0, то
        f = first/second # результат деления first на second

        return f # возврат результата деления first на second

    else: # иначе

        return 'Ошибка' # возврат значения 'Ошибка'


result1 = divide(69, 3)
result2 = divide(3, 0)
print(result1)
print(result2)