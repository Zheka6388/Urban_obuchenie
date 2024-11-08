from random import choice

#Даны 2 строки:
first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda x, y: x == y, first, second))) # лямда-функция для х (элемент first) и у (элемент second),
# создаёт список совпадения букв в той же позиции (где True - совпало, False - не совпало.)

def get_advanced_writer(file_name): # функция, принимающая название файла для записи.
    def write_everything(*data_set): # внутреняя функция, где *data_set - параметр принимающий неограниченное
        # количество данных любого типа.
        with open(file_name, 'a+', encoding='utf-8') as file: # открыть файл в режиме «a+» (открывает файл на
            # чтение и запись)
            for i in data_set: # цикл for: для i в data_set
                file.write(str(i) + '\n') # Записываем строку и переходим на новую строку
    return write_everything # возвращает функцию write_everything.


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


class MysticBall:

    def __init__(self, *words): #
        self.words = words # атрибут words, хранящий коллекцию строк.

    def __call__(self): #  метод __call__,который будет случайным образом выбирать слово из words и возвращать его.
        return choice(self.words) # возврат функции choice к атрибуту words


first_ball = MysticBall('Да', 'Нет', 'Возможно')
print(first_ball())
print(first_ball())
print(first_ball())
