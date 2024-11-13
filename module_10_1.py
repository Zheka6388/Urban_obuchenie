from time import sleep # импорт функции sleep из модуля time для установки паузы
from datetime import datetime #  Модуль предоставляет метод now(), который возвращает текущие дату и время
# с учетом локальных настроек.
from threading import Thread # модуль для создания и управления потоками.
'''import time
current_time = time.time()'''


def write_words(word_count, file_name): # функция write_words с аргументами: word_count - количество записываемых
    # слов и file_name - название файла, куда будут записываться слова
    with open(file_name, 'a+', encoding="utf-8") as file: # открыть файл в режиме "чтение - запись"
        for i in range(word_count): # цикл for для i в последовательности количества записываемых слов
            file.write(f'Какое-то слово № {i + 1}\n') # запись в файл с переходом на новую строку согласно
            # заданному количеству записываемых слов
            sleep(0.1) # прерывание после записи каждого на 0.1 секунду.
    print(f'Завершилась запись в файл {file_name}')


t_start = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
print('Продолжительность последовательной работы', datetime.now() - t_start) # вывод времени, затраченного на запись
# файлов от старта до остановки потока

t_start = datetime.now()
thread1 = Thread(target=write_words, args=(10, 'example5.txt'))
thread2 = Thread(target=write_words, args=(30, 'example6.txt'))
thread3 = Thread(target=write_words, args=(200, 'example7.txt'))
thread4 = Thread(target=write_words, args=(100, 'example8.txt'))

# запуск потоков методом start
thread1.start()
thread2.start()
thread3.start()
thread4.start()

# остановка основного потока при помощи join.
thread1.join()
thread2.join()
thread3.join()
thread4.join()
print('Продолжительность работы потоков', datetime.now() - t_start) # вывод времени, затраченного на запись
# файла от старта до остановки потоков
