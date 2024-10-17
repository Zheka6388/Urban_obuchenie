
def custom_write(file_name, strings): # Функция записывает строки из strings в file_name.
        # Возвращает словарь с ключом в виде кортежа с номером строки и байтом начала
        # строки и значением в виде строки из strings.   file_name - название файла для записи
        # strings - список строк для записи
        strings_positions = {}  # Создаем пустой словарь strings_positions
        num_string = 0
        file = open(file_name, 'w', encoding='utf-8')
        for string in strings:
            start = file.tell()
            file.write(string + '\n')
            num_string += 1
            strings_positions[(num_string, start)] = string
        file.close()
        return strings_positions

#Пример выполняемого кода:
if __name__ == '__main__':
    info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)