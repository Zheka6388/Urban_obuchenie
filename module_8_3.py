class Car:

    def __init__(self, model, vin, numbers):
        self.model = model # название автомобиля (строка)
        if self.__is_valid_vin(vin):
            self.__vin = vin #  vin номер автомобиля (целое число). Уровень доступа private
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers # номера автомобиля (строка)

    def __is_valid_vin(self, vin_number): # Метод __is_valid_vin(vin_number) - принимает vin_number
        # и проверяет его на корректность
        if not isinstance(vin_number, int): # если vin_number не является целым числом
            raise IncorrectVinNumber("Некорректный тип vin номер")
        if vin_number < 1000000 or vin_number >= 9999999: # если vin_number не входит в диапозон чисел
            # от 1000000 до 9999999 вклбчительно
            raise IncorrectVinNumber("Неверный диапазон для vin номера'")
        return True # Возвращает True, если исключения не были выброшены.

    def __is_valid_numbers(self, numbers): # Метод __is_valid_numbers(numbers) - принимает numbers и проверяет
        # его на корректность.
        if not isinstance(numbers, str): # если numbers не является строкой
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(numbers) != 6: # если количество символов в numbers не равняется 6
            raise IncorrectCarNumbers('Неверная длина номера')
        else: # иначе
            return True # Возвращает True, если корректный

class IncorrectCarNumbers(Exception): # Выбрасывает исключение с сообщением для __is_valid_numbers
    def __init__(self, message):
        self.message = message


class IncorrectVinNumber(Exception): # Выбрасывает исключение с сообщением для __is_valid_vin
    def __init__(self, message):
        self.message = message

# блок проверки на ошибки
try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc: # Выбрасывает исключение с сообщением для __is_valid_vin
    print(exc.message)
except IncorrectCarNumbers as exc: # Выбрасывает исключение с сообщением для __is_valid_numbers
    print(exc.message)
else: # иначе
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')