first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable'] # список, состоящих из строк
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler'] # список, состоящих из строк

first_result = [len(x) for x in first_strings if len(x) > 5] # В переменной first_result: список,
# созданный при помощи сборки состоящий из длин строк списка first_strings, при условии, что длина строк
# не менее 5 символов.
print(first_result)
second_result = [(x, y) for x in first_strings for y in second_strings if len(x) == len(y)] # переменная
# second_result: список, созданный при помощи сборки состоящий из пар слов(кортежей) одинаковой длины. Каждое
# слово из списка first_strings должно сравниваться с каждым из second_strings. (два цикла)
print(second_result)
third_result = [{x: len(x)} for x in first_strings + second_strings if len(x) % 2 == 0] # переменная
# third_result: словарь, созданный при помощи сборки, где парой ключ-значение будет строка-длина строки.
# Значения строк будут перебираться из объединённых вместе списков first_strings и second_strings.
# Условие записи пары в словарь - чётная длина строки.
print(third_result)