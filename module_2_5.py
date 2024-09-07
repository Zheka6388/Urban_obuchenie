def get_matrix(n, m, value): # функция get_matrix и в ней параметры n, m и value.
    matrix = [] # пустой список matrix внутри функции get_matrix.

    for i in range(n): # первый(внешний) цикл for для кол-ва строк матрицы, n повторов.
         matrix.append([]) # В первом цикле- пустой список в список matrix.

         for j in range(m):# второй(внутренний) цикл for для кол-ва столбцов матрицы, m повторов.
             # matrix.append(value) # ошибка
             matrix[i].append(value) # пополнение ранее добавленного пустого списока значениями value.

    return  matrix # После всех циклов везврат значения переменной matrix.


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

print(result1)
print(result2)
print(result3)

