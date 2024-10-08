def print_params (a = 1, b = 'Строка', c = True): # функция с тремя параметрами со значениями по
    # умолчанию (например сейчас это: 1, 'строка', True).
    print(a, b, c)


print_params() # Вызов функции print_params без аргументов (значений)
print_params(7) # Вызов функции print_params с одним аргументом (значением),применяется
# сначала к первому параметру "а", последующие параметры - без изменений.
print_params('Time', 11) # Вызов функции print_params с двумя аргументами (значением),
# применяется последовательно к параметрам функции, третий параметр - без изменений.
print_params(11, 'time', False) # Вызов функции print_params с изменёнными
# значениями параметров.
print_params(b = 25) # Вызов функции print_params, при котором меняется значение указанного
# параметра "b", остальные параметры без изменений.
print_params(c = [1, 2, 3]) # Вызов функции print_params, при котором меняется значение указанного
# параметра "с", остальные параметры без изменений.

values_list = [33, 'Aplle', True] # список с тремя элементами разных типов
values_dict = {'a': 21, 'b': "fruits", 'c': False} # словарь с тремя ключами, соответствующими
# параметрам функции print_params, и значениями разных типов.

print_params(*values_list) # Вызов функции print_params, с распаковкой для списка.
print_params(**values_dict) # Вызов функции print_params, с распаковкой для словаря.

values_list_2 = [19.91, 'Hello World'] # список с двумя элементами разных типов

print_params(*values_list_2, 42) # Вызов функции print_params, с распаковкой для списка и
# указанием третьего значения (в списке их всего два), иначе третье значение будет первоначальным - True