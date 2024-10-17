
def custom_write(file_name, strings): # Функция записывает строки из strings в file_name.
        # Возвращает словарь с ключом в виде кортежа с номером строки и байтом начала
        # строки и значением в виде строки из strings.   file_name - название файла для записи
        # strings - список строк для записи
        strings_positions = {}  # Создаем пустой словарь strings_positions
        num_string = 0 # переменная для нумерации строк
        file = open(file_name, 'w', encoding='utf-8') 
        for string in strings:
            start = file.tell()# Для получения номера байта начала строки используется метод tell() перед записью.
            file.write(string + '\n') # Записываем строку и переходим на новую строку
            num_string += 1 # увеличиваем номер строки
            strings_positions[(num_string, start)] = string # Создаем словарь strings_positions, где ключом будет кортеж
            # (<номер строки>, <байт начала строки>), а значением - записываемая строка.
        file.close() # закрыть файл
        return strings_positions# Возвращаем словарь strings_positions

#Пример выполняемого кода:
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)