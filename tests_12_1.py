import unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase): # класс RunnerTest, наследуемый от TestCase из модуля unittest
    def test_walk(self): # метод, в котором создаётся объект класса Runner с произвольным именем.
        sprinter = Runner("Спринтер")
        # for i in range(9): # проверка неуспешного теста
        # Ran 3 tests in 0.029s
        # FAILED(failures=1)
        # 50 != 45
        # Expected: 45
        # Actual: 50
        for i in range(10): # вызов методa walk у этого объекта 10 раз.
            sprinter.walk()
        self.assertEqual(sprinter.distance, 50) # методом assertEqual сравнить distance этого объекта
        # со значением 50.

    def test_run(self): # метод, в котором создаётся объект класса Runner с произвольным именем.
        sprinter = Runner("Спринтер")
        for i in range(10): # вызов метода run у этого объекта 10 раз.
            sprinter.run()
        self.assertEqual(sprinter.distance, 100) # методом assertEqual сравнить distance этого объекта
        # со значением 100.

    def test_challenge(self): # метод в котором создаются 2 объекта класса Runner с произвольными именами.
        sprinter = Runner("Спринтер1")
        begun = Runner('Бегун')
        for i in range(10): # 10 раз у объектов вызываются методы run и walk соответственно
            sprinter.run() #
            begun.walk() #
        self.assertNotEqual(sprinter.distance, begun.distance) # Т.к. дистанции должны быть разными,
        # используем метод assertNotEqual, чтобы убедится в неравенстве результатов.

if __name__ == '__main__': # Запуск тестов
    unittest.main()