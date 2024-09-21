calls = 0 # переменная вне функции (глобальная)

def count_calls(call): # функция "количество вызовов" глобальной переменной
    global calls # вызов  глобальной переменной внутри функции
    calls += call # подсчёт количества вызовов функции

    return calls # возврат к глобальной переменной

def string_info(string): # функция "информационная строка"
    count_calls(1) # подсчёт количества вызовов функции
    a = [] # переменная для списка значений
    a.append(len(string)) # подсчёт количества символов значений в списке "а"
    a.append(string.upper()) # перевод строчного значения в списке в верхний регистр
    a.append(string.lower()) # перевод строчного значения в списке в нижний регистр

    return tuple(a) # возврат последовательности элементов (len(string),string.upper(),
    # string.lower()),которые разделены между собой запятой и заключены в скобки
    # (неизменяемый упорядоченный тип данных)

def is_contains (string, list_to_search): # Функция принимает два аргумента:
    # строку и список, и возвращает True, если строка находится в
    # этом списке, False - если отсутствует.
    list_to_search_1 = [] # переменная для списка значений
    string.upper() # перевод строчного значения в списке в верхний регистр
    count_calls(1)  # подсчёт количества вызовов функции
    for i in list_to_search:
        list_to_search_1.append(i.upper())


    return (string.upper() in list_to_search_1)


print(string_info('Abbreviation'))
print(string_info('Pineapple'))
print(is_contains("Преобразование" , ["про" , "брод"]))
print(is_contains("Остаток" , ["ост" , "коста" , "копр"]))
print(is_contains("Urban" , ["ban" , "BaNaN" , "urBAN"]))
print(calls)
