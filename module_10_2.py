from threading import Thread
from time import sleep

class Knight(Thread): # класс Knigt, наследуемый от Thread

    def __init__(self, name, power): # метод __init__ с атрибутами; name и power
        self.name_ = name # имя рыцаря
        self.power = power # сила рыцаря
        super().__init__()

    def run(self): # метод run
        days = 0  # счётчик дней сражений
        enemies = 100  # изначальное колличество врагов
        print(f'{self.name_}, на нас напали!')
        while enemies > 0: # цикл while для подсчёта оставшихся врагов и кол-ва дней сражений
            days += 1 # прибавляем 1 день после каждого сражения
            enemies -= self.power # вычитание из общего кол-ва врагов силы рыцаря за 1 сражение
            print(f'{self.name_} сражается {days} день(дня)..., осталось {enemies} воинов')
            sleep(1) # пауза в 1 секунду
        else: # иначе
            print(f'{self.name_} одержал победу спустя {days} дней(дня)!')


# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# запуск потоков
first_knight.start()
second_knight.start()
# остановка текущнго потока
first_knight.join()
second_knight.join()
print("Все битвы закончились!")
