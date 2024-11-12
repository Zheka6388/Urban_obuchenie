def is_prime(func): # Функция декоратор, которая распечатывает "Простое", если
# результат 1ой функции будет простым числом и "Составное" в противном случае.
    def wrapper(*args): # внутренняя функция wrapper в is_prime
        result = func(*args) # переменная result, в которую передаём переменную func функции  is_prime
        summa = sum(args) # результат функции sum_three
        k = 0 # в k будем хранить количество делителей
        for i in range(2, summa + 1): # цикл for для i в последовательности от 2 до 11 включительно
            if summa % i == 0: # если сумма / i = 0
                k = k +1 # прибавляем делитель
        if k == 1: # простое число делится на 1 и на само себя, значит при прохождении цикла for должен
            # проявиться только один делитель (summa)
            print('Простое')
        else: # иначе
            print('Составное')
        return result # возврат результата работы функции wrapper
    return wrapper # возврат функции wrapper


@is_prime # @is_prime - декоратор для функции sum_three
def sum_three(*args): # Функция, которая складывает 3 числа
    return sum(args) # возврат sum(args)



result = sum_three(2, 3, 6)
print(result)
