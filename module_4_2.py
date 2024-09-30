
def test_function(): # внешняя функция "test_function".

    def inner_function(): # внутреняя функция "inner_function".
        print('Я в области видимости функции test_function')
    inner_function() # ничего не выводит в консоль, не вызвана внешняя функция "test_function".

test_function() # вызов внешней функции "test_function". Выводит значение внутренней функции "inner_function"
                # функция "inner_function" поподает в область видимости функции "test_function".

#inner_function() # не выводит значение внутренней функции "inner_function", возникает ошибка.
                 # Вызов функции "inner_function" невозвожен, т.к. она является внутринней
                 # фукцией "test_function". Функция "inner_function" находится
                 # не в области видимости функции "test_function".
