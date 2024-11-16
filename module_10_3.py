from threading import Lock, Thread
from time import sleep
from random import randint


class Bank:

    def __init__(self):
        self.balance = 0 # Атрибуты объекта: баланс банка (int)
        self.lock = Lock() # Атрибуты объекта: объект класса Lock для блокировки потоков.

    def deposit(self): # Метод deposit:

        for i in range(100): # цикл будет совершать 100 транзакций пополнения средств.
            replenishment = randint(50, 500) # пополнение, случайное число (сумма пополнения) от 50 до 500
            self.balance += replenishment # прибавить пополнение к балансу
            print(f'Пополнение: {replenishment}. Баланс: {self.balance}')

            if self.balance >= 500 and self.lock.locked(): # Если баланс больше или равен 500 и замок lock
                # заблокирован - lock.locked()
                self.lock.release() # то разблокировать его методом release.
                print(f'Пополнен: {replenishment}. Баланс: {self.balance}')

    sleep(0.001) # пауза между операциями

    def take(self): # Метод take:

        for i in range(100): # цикл будет совершать 100 транзакций снятия средств
            withdrawal = randint(50, 500) # снятие, случайное число (сумма снятия) от 50 до 500
            print(f'Запрос на {withdrawal}')

            if withdrawal <= self.balance: # если случайное число меньше или равно текущему балансу, то
                # произвести снятие,
                self.balance = self.balance - withdrawal # уменьшив balance на соответствующее число
                print(f'Снятие: {withdrawal}. Баланс: {self.balance}')

            else: # иначе
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire() # заблокировать поток методом acquire.

        sleep(0.001) # пауза между операциями

bk = Bank()
#th1 = threading.Thread(target=Bank.deposit, args=(bk,))
#th2 = threading.Thread(target=Bank.take, args=(bk,))
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
