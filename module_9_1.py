def apply_all_func(int_list, *functions): # функция, которая принимает параметры: int_list - список из
    # чисел (int, float), *functions - неограниченное кол-во функций (которые применимы к спискам,
    # состоящим из чисел)
    results = { } # пустой словарь
    for function in functions: # цыкл for для функции в functions
        results[function.__name__] = function(int_list) # словарь с ключом: "название функции" и значением:
        # "результат функции"
    return results # возврат словаря с ключом названия функции и значением результата функции.


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
