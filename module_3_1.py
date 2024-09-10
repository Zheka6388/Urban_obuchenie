calls = 0 # переменная вне функции (глобальная)

def count_calls(): # функция "количество вызовов" глобальной переменной
    global calls # вызов  глобальной переменной внутри функции
    calls += 1 # подсчёт количества вызовов функции
    return calls # возврат к глобальной переменной

def string_info(string): # функция "информационная строка"
    global calls # вызов  глобальной переменной внутри функции
    calls += 1 # подсчёт количества вызовов функции
    a = [] # переменная для списка значений
    a.append(len(string)) # подсчёт количества символов значений в списке "а"
    a.append(string.upper()) # перевод строчного значения в списке в верхний регистр
    a.append(string.lower()) # перевод строчного значения в списке в нижний регистр
    return tuple(a) # возврат последовательности элементов (len(string),string.upper(),
    # string.lower()),которые разделены между собой запятой и заключены в скобки
    # (неизменяемый упорядоченный тип данных)

#print(string_info('Abbreviation'))
#print(string_info('Pineapple'))


def is_contains(string , list_to_search):#
    global calls # вызов  глобальной переменной внутри функции
    calls += 1 # подсчёт количества вызовов функции
    contains = [] # # переменная для списка значений
    #list_to_search = ["Urban" , 'Abbreviation']
    string.upper()
    for i in list_to_search:
        if contains.append(i.upper()):

            return True

        return False

print(string_info('Abbreviation'))
print(string_info('Pineapple'))
print(is_contains("Преобразование" , ["про" , "брод"]))
print(is_contains("Остаток" , ["ост" , "коста" , "копр"]))
print(is_contains("Urban" , ["ban" , "BaNaN" , "urBAN"]))
print(calls)

#'Urban', ['ban', 'BaNaN', 'urBAN']-ЗНАЧЕНИЕ ДОЛЖНО БЫТЬ True ИЛИ False ?????

#Как проверить в питоне если в списке есть элемент?
#Чтобы проверить есть ли элемент в списке, мы можем применить оператор in.
# При этом, если элемент в наличии - нам вернется булевое значение. True,
# в противном случае - False: lst = [1, 2, 3] res = 1 in lst print (res) # выведет True.
#code.mu