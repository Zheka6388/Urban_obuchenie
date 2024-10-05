
data_structure = [                          # основа для вычесления.!!!!!!
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(data_structure): # функция "вычисление структурной суммы" с
    # параметром "структура данных".
    summa = 0 # переменная для подсчёта сумм всех данных.

    if isinstance(data_structure, dict): # если объект в data_structure является словарём

        for key, value in data_structure.items(): # тогда присваиваем "ключ", "значение" в методе items() для
            # словарей (возвращает все пары «ключ — значение»)
            summa += calculate_structure_sum(key) # прибавить ключи из словарей
            summa += calculate_structure_sum(value) # прибавить значения из словарей

        #print(data_structure) # достаёт словари из data_structure

    if isinstance(data_structure, (list, tuple, set)): # если объект в data_structure является списком,
        # кортежем или множеством

        for i in data_structure: # тогда присваиваем i списки, кортежи и множества из data_structure
            summa += calculate_structure_sum(i) # и прибавляем значения

        #print(data_structure) # достаёт списки, кортежи и множества из data_structure

    if isinstance(data_structure, (int, float)): # если объект в data_structure является целочисленным
        # значением или числом с плавающей запятой
        summa += data_structure # прибавляем значения

        #print(data_structure) # достаёт числовые значения из data_structure; 1, 2, 3, 4, 5, 6, 7, 8, 2,
        # 35 - 73 единицы

    if isinstance(data_structure, str): # если объект в data_structure является строковым значением
        summa += len(data_structure) # прибавляем количество длины строковых значений

        #print(data_structure) # достаёт строковые значения из data_structure; a, b, cube,
        # drum, Hello, Urban, Urban2 -26 единиц

    return summa # возврат к переменной для подсчёта сумм всех данных


result = calculate_structure_sum(data_structure)
print(result)

