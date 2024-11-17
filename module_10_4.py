from threading import Thread
import random
import time
from queue import Queue


class Table: # стол, хранит информацию о находящемся за ним гостем (Guest)
    def __init__(self, number):
        self.number = number # номер стола
        self.guest = None # гость, который сидит за этим столом (по умолчанию None)

class Guest(Thread): # гость, поток, при запуске которого происходит задержка от 3 до 10 секунд.
    def __init__(self, name):
        super().__init__() # вызов родительского класса Thread и его дополняем
        self.name = name # имя гостя.

    def run(self): # метод run
        time.sleep(random.randint(3, 10)) # ожидание случайным образом от 3 до 10 секунд.

class Cafe: # кафе, в котором есть определённое кол-во столов и происходит имитация прибытия
# гостей (guest_arrival) и их обслуживания (discuss_guests).
    def __init__(self, *tables: Table):
        self.tables = tables # столы в этом кафе(любая коллекция).
        self.queue = Queue() # очередь (объект класса Queue)




    def guest_arrival(self, *guests: Guest): # методам guest_arrival: (прибытие гостей)
        for guest in guests: # цикл for для гостя из списка гостей
            vacant_table = False # изначально свободных столов нет
            for table in self.tables: # цикл for для стола в списке столов кафе
                if vacant_table: #  если есть свободный стол
                    table.guest = guest # то садить гостя за стол (назначать столу guest)
                    guest.start() #  запуск потокa гостя
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    vacant_table = True # изменение значения свободного стола
                    break # прерывание выполнения цикла, переход к следующему цыклу
            if not vacant_table: # Если же свободных столов для посадки не осталось
                self.queue.put(guest) # то помещать гостя в очередь queue
                print(f'{guest.name} в очереди')

    def discuss_guests(self): # метод имитирует процесс обслуживания гостей
        while not (self.queue.empty() and self.empty_cafe()): # пустая очередь и
            for table in self.tables: # цикл for для стола в списке столов кафе
                if not table.guest: # если текущему столу не присвоен гость
                    if not self.queue.empty(): # если очередь не пустая
                        table.guest = self.queue.get() # то текущему столу присваивается гость, взятый из
                        # очереди (queue.get()).
                        print(f'{table.guest.name} вышел(-ла) из очереди',
                            f'и сел(-а) за стол номер {table.number}')
                        table.guest.start() # запустить поток этого гостя (start)
                else: # иначе
                    if not table.guest.is_alive(): 
                        print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                        print(f'Стол номер {table.number} свободен')
                        table.guest = None

    def empty_cafe(self): # кафе пустое
        return not any(table.guest for table in self.tables) # возврат пока очередь не пустая
        # (метод empty) или хотя бы один стол занят.

#Выполняемый код:

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
