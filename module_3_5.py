def get_multiplied_digits(number): # функция "получение множенных значений" с параметром "число".
    str_number = str(number) # переменная со строковым "числом".
    first = int(str_number[0]) # переменная с первой цифрой в "числе".
    if len(str_number) > 1: # если длина str_number больше 1, то

        return first * get_multiplied_digits(int(str_number[1:])) # возвращать значение со срезом с
        # первого элемента и до конечного элемента.

    else: # иначе

        return int(str_number) # вернуть оставшуюся цифру first.


result = get_multiplied_digits(40203) # (20507) ; 25172
print(result) # (70 - перемножаются первое, третье и пятое числа, нолевые значения не берутся в расчёт)
              # 140 - перемножаются все числа последовательно

#get_multiplied_digits(40203) -> 4 * get_multiplied_digits(203) ->
# 4 * 2 * get_multiplied_digits(3) -> 4 * 2 * 3 ; значит,при первом вызове получается число 4 ,при следуещем
# вызове - цифра 0203, из которой в числовом значении берётся число 2 и т.д.