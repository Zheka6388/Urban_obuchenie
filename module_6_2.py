
class Vehicle:
    __COLOR_VARIANTS =  ['синий', 'красный', 'зелёный', 'чёрный', 'белый'] # Атрибут класса Vehicle - __COLOR_VARIANTS,
    # в который записан список допустимых цветов для окрашивания.

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner     # владелец транспорта.(владелец может меняться)
        self.__model = model  # модель(марка) транспорта. (мы не можем менять название модели)
        self.__engine_power = engine_power # мощность двигателя. (мы не можем менять мощность двигателя самостоятельно)
        self.__color = color #  название цвета. (мы не можем менять цвет автомобиля своими руками)

    def get_owner(self): # Метод get_owner
        return f'Владелец: \033[36m{self.owner}\033[0m' # возвращает строку: "Владелец: <имя>"

    def get_model(self): # Метод get_model
        return f'Модель: {self.__model}' # возвращает строку: "Модель: <название модели транспорта>"

    def get_horsepower(self): # Метод get_horsepower
        return f'Мощность двигателя: {self.__engine_power}' # возвращает строку: "Мощность
        # двигателя: <мощность>"

    def get_color(self): # Метод get_color
        return f'Цвет: \033[36m{self.__color}\033[0m' # возвращает строку: "Цвет: <цвет транспорта>"

    def print_info(self): # Метод print_info
        print(f'{self.get_model()}\n{self.get_horsepower()}\n{self.get_color()}\n{self.get_owner()}\n') # распечатывает
        # результаты методов: get_model, get_horsepower, get_color,get_owner. "+" добавляем элемент \n в конце, для
        # того, чтобы разделить действия вывода результата

    def set_color(self, new_color): # Метод set_color - принимает аргумент new_color(str)
        list = [] # создаём пустой список
        for i in self.__COLOR_VARIANTS: # присваиваем переменной i атрибут __COLOR_VARIANTS
            list.append(i.lower()) # добавить новый элемент в нижнем регистре в список
        if new_color.lower() in list: # если new_color в нижнем регистре есть в списке
            self.__color = new_color # тогда заменяем действующий цвет на новый
        else: # иначе
            print(f'\033[34mНельзя сменить цвет на {new_color}\n\033[0m') # добавляем элемент \n в конце, для того, чтобы разделить
            # действия вывода результата



class Sedan(Vehicle): # наследуемый класс Vehicle.

    __PASSENGERS_LIMIT = 5 # в седан может поместиться только 5 пассажиров


# Текущие цвета __COLOR_VARIANTS = ['синий', 'красный', 'зелёный', 'чёрный', 'белый']
vehicle1 = Sedan('Егор', 'Kia Rio', 'зелёный', 130)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Борнео')
vehicle1.set_color('Чёрный')
vehicle1.owner = 'Макс'

# Проверяем что поменялось
vehicle1.print_info()

#Цвет           Текст          Фон
#Чёрный           30           40
#Красный          31           41
#Зелёный          32           42
#Жёлтый           33           43
#Синий            34           44
#Фиолетовый       35           45
#Бирюзовый        36           46
#Белый            37           47

#\033[3m - отвечает за стилб текста в данном случае это курсив.
#\033[33m - отвечает за цвет текста.
#\033[41m - отвечает за цвет фона.
#{} - заменит на "Htua_0111100000"
#\033[0m - отвечает за сброс к начальным значениям.
