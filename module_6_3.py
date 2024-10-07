
class Hourse: # класс описывающий лошадь

    def __init__(self): # метод __init__ для class Hourse
        self.x_distance = 0  # пройденный путь.
        self.sound = 'Frrr' # звук, который издаёт лошадь

    def run(self, dx): # функция run с параметром dx
        self.x_distance += dx # изменение дистанции, увеличивает x_distance на dx.

        return self.x_distance # возврат изменённого параметра x_distance

class Eagle: # класс описывающий орла

    def __init__(self): # метод __init__ для class Eagle
        self.y_distance = 0  # высота полёта
        self.sound = 'I train, eat, sleep, and repeat' # звук, который издаёт орёл (отсылка)

    def fly(self, dy): # функция fly с параметром dy
        self.y_distance += dy # изменение дистанции, увеличивает y_distance на dy

        return self.y_distance # возврат изменённого параметра y_distance

class Pegasus(Hourse, Eagle): # класс описывающий пегаса, классы родители: Horse и Eagle

    def __init__(self): # метод __init__ для class Pegasus
        super().__init__() # функция, которая позволяет вызывать методы родительского класса в дочернем классе
        Eagle.__init__(self) # обращение к классу Орла, для видимости второго родительского класса

    def move(self, dx, dy): # метод move, dx и dy изменения дистанции. В этом методе должны запускаться наследованные
        # методы run и fly соответственно.

        return self.fly(dy), self.run(dx) # возврат наследованных методов run и fly

    def get_pos(self): # функция  get_pos, возвращает текущее положение пегаса в виде кортежа - (x_distance,
        # y_distance)в том же порядке.

        return self.x_distance, self.y_distance # вщзврат кортежа x_distance, y_distance. По параметру
        # self.x_distance эта функция обращается к первому родительскому классу Hourse, а параметр self.y_distance
        # не видит (в метод __init__ класса Пегас нужно добавить обращение к классу Орла через __init__(self))

    def voice(self): # метод voice
        print(self.sound) # печатает значение унаследованного атрибута sound.


p1 = Pegasus() # обращение к классу Пегас
print(p1.get_pos()) # вывод начальной дистанции dx и dy
p1.move(7, 15) # изменения дистанции dx и dy
print(p1.get_pos()) # вывод результата
p1.move(-5, 20) # изменения дистанции dx и dy по отношению к предыдущему изменению
print(p1.get_pos()) # вывод нового результата
p1.voice() # Pegasus издаёт звук "I train, eat, sleep, and repeat", т.к. по порядку сначала идёт наследование
# от Horse, а после от Eagle. При обращении через super() методы будут искаться сначала в первом, потом во втором
# и т.д. классах по mro().

print(Pegasus.mro()) # порядок наследования классов