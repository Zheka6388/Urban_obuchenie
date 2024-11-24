from datetime import datetime
import multiprocessing


def read_info(name): # функция read_info(name), где name - название файла
    all_data = [] # локальный список all_data.
    with open(name, 'r', encoding='utf-8') as file: # контекстный менеджер with для открытия файла name в режиме чтения.
        while True: #
            line = file.readline() # Считывать информацию построчно (readline)
            all_data.append(line) # Во время считывания добавлять каждую строку в список all_data.
            if not line: # если считанная строка окажется пустой.
                break # остановка программы


if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

#    start_time = datetime.now()
#    for name in filenames:
#        read_info(name)
#    print(datetime.now() - start_time, '(линейный)')
# 0:00:10.602864 (линейный)            # данные при каждом запуске меняются в пределах 1 секунды

    start_time = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    print(datetime.now() - start_time, '(многопроцессный)')
# 0:00:04.568335 (многопроцессный)     # данные при каждом запуске меняются в пределах 1 секунды