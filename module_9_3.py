first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(x) - len(y) for x, y in zip(first, second) if len(x) != len(y)) # Списковые словарные сборки,
# которые высчитывают разницу длин строк из списков first и second, если их длины не равны.

second_result = (len(first[i]) == len(second[i]) for i in range(len(first))) # Списковые словарные сборки,
# которые содержат результаты сравнения длин строк в одинаковых позициях из списков first и second

print(list(first_result))
print(list(second_result))

