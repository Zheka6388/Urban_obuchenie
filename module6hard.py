class Figure: # класс Figure(родительский)
    __sides = [] # список сторон (целые числа)
    __color = [] # список цветов в формате RGB
    filled = False # изначально незакрашена, bool

    def __init__(self, rgb, *side):  # палитра(в формате RGB) и стороны
            self.color = list(rgb) # список цветовой палитры
            self.side = side[0]  # берём только первое значение
            self.filled = True  # принята палитра (rgb), фигура закрашена

    def get_color(self): # Метод get_color, возвращает список RGB цветов
        self.__color = self.color
        self.filled = True
        return self.__color

    def _is_valid_color(self, r, g, b): # Метод __is_valid_color - служебный, принимает параметры r, g, b, который
        # проверяет корректность переданных значений перед установкой нового цвета. Корректным цвет: все
        # значения r, g и b - целые числа в диапазоне от 0 до 255 (включительно).
        self.r = r
        self.g = g
        self.b = b
        if 0 <= self.r <= 255 and 0 <= self.g <= 255 and 0 <= self.b <= 255: # если параметры r, g и b находятся
            # в диапозоне палитры цветов от 0 до 255
            return True
        else: # иначе
            return False

    def set_color(self, r, g, b): # Метод set_color принимает параметры r, g, b - числа и изменяет атрибут __color
        # на соответствующие значения, предварительно проверив их на корректность. Если введены некорректные данные,
        # то цвет остаётся прежним.
        if self._is_valid_color(r, g, b):
            self.color = [self.r, self.g, self.b]

    def __is_valid_sides(self, *args): # Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон,
        # возвращает True если все стороны целые положительные числа и кол-во новых сторон совпадает с текущим,
        # False - во всех остальных случаях.
        for side in self.sides:
            if len(self.sides) == self.sides_count and side > 0 and type(side) == int:
                return True
            else:
                return False

    def set_sides(self, *new_sides): # Метод set_sides(self, *new_sides) должен принимать новые стороны,
        # если их количество не равно sides_count, то не изменять, в противном случае - менять.
        massive_lst = []
        self.sides = list(new_sides)
        if self.__is_valid_sides(self, *new_sides):
            self.get_sides()
        else:
            for i in range(self.sides_count):
                 massive_lst.append(self.side)  # если делать как указано в примере выполнения задания (вывод на консоль)
                # massive_lst.append(1)       # если делать как в ТЗ, где выводится массив из 1 числом в кол-во сторон
            self.sides = massive_lst
            self.get_sides()

    def get_sides(self): # Метод get_sides возвращаeт значение атрибута __sides
        self.__sides = self.sides
        return self.__sides

    def __len__(self): # Метод __len__ возвращаeт периметр фигуры
        if self.sides_count == 0:
            return 0
        else:
            sum = 0
            for item in self.__sides:
                sum += item
            return sum


class Circle(Figure):
    sides_count = 1 # кол-во сторон
    __radius = None

    def set_radius(self): # рассчитать исходя из длины окружности (одной единственной стороны)
        self.__radius = self.__len__() / (2 * 3.141569)
        return self.__radius

    def get_square(self): #  возвращает площадь круга
        self.set_radius()
        return (self.__radius ** 2) * 3.141569

class Triangle(Figure):
    sides_count = 3 # кол-во сторон
    __height = None

    def get_square(self): # возвращает площадь треугольника
        sides = self.get_sides()
        p = (sides[0] + sides[1] + sides[2]) / 2
        return (p * (p - sides[0]) * (p - sides[1]) * (p - sides[2])) ** 0.5


class Cube(Figure):
    sides_count = 12 # кол-во сторон

    def set_side_lst(self): #
        set_side_lst = []
        for element in range(self.sides_count):
            set_side_lst.append(self.side)
        self.__sides = set_side_lst
        return self.__sides

    def get_volume(self): # Метод get_volume, возвращает объём куба
        return self.side ** 3


#Код для проверки:
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())


