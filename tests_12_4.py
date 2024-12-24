import logging
import unittest
from test_12_3 import Runner

class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name

class RunnerTest(unittest.TestCase):  # класс RunnerTest, наследуемый от TestCase из модуля unittest
    is_frozen = False

    @classmethod
    def setUpClass(cls):
        logging.basicConfig(filename='runner_tests.log', filemode='w', level=logging.INFO, encoding='utf-8',
                            format='%(asctime)s - %(levelname)s - %(module)s - %(message)s')#'%(asctime)s | %(levelname)s | %(message)s')

    @unittest.skipIf(is_frozen, '')
    def test_walk(self):  # метод, в котором создаётся объект класса Runner с произвольным именем.
        #sprinter = Runner("Спринтер")
        try:
            sprinter = Runner(name="Спринтер", speed=-100)
            for i in range(10):  # вызов методa walk у этого объекта 10 раз.
                sprinter.walk()
            self.assertEqual(sprinter.distance, 50)  # методом assertEqual сравнить distance этого объекта
            # со значением 50.
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    @unittest.skipIf(is_frozen, '')
    def test_run(self):  # метод, в котором создаётся объект класса Runner с произвольным именем.
        try:
            sprinter = Runner(name=50, speed=100)
            for i in range(10):  # вызов метода run у этого объекта 10 раз.
                sprinter.run()
            self.assertEqual(sprinter.distance, 100)  # методом assertEqual сравнить distance этого объекта
            # со значением 100.
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner',
                            exc_info=True)

    @unittest.skipIf(is_frozen, '')
    def test_challenge(self):  # метод в котором создаются 2 объекта класса Runner с произвольными именами.
        sprinter = Runner("Спринтер1")
        begun = Runner('Бегун')
        for i in range(10):  # 10 раз у объектов вызываются методы run и walk соответственно
            sprinter.run()  #
            begun.walk()  #
        self.assertNotEqual(sprinter.distance, begun.distance)  # Т.к. дистанции должны быть разными,
        # используем метод assertNotEqual, чтобы убедится в неравенстве результатов.

if __name__ == '__main__':
    unittest.main()