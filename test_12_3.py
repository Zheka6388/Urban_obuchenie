import unittest
from tests_12_2 import Tournament
from tests_12_1 import Runner


class RunnerTest(unittest.TestCase):  # класс RunnerTest, наследуемый от TestCase из модуля unittest
    is_frozen = False
    #@frozen
    @unittest.skipIf(is_frozen, '')
    def test_walk(self):  # метод, в котором создаётся объект класса Runner с произвольным именем.
        sprinter = Runner("Спринтер")
        # for i in range(9): # проверка неуспешного теста
        # Ran 3 tests in 0.029s
        # FAILED(failures=1)
        # 50 != 45
        # Expected: 45
        # Actual: 50
        for i in range(10):  # вызов методa walk у этого объекта 10 раз.
            sprinter.walk()
        self.assertEqual(sprinter.distance, 50)  # методом assertEqual сравнить distance этого объекта
        # со значением 50.

    @unittest.skipIf(is_frozen, '')
    def test_run(self):  # метод, в котором создаётся объект класса Runner с произвольным именем.
        sprinter = Runner("Спринтер")
        for i in range(10):  # вызов метода run у этого объекта 10 раз.
            sprinter.run()
        self.assertEqual(sprinter.distance, 100)  # методом assertEqual сравнить distance этого объекта
        # со значением 100.

    @unittest.skipIf(is_frozen, '')
    def test_challenge(self):  # метод в котором создаются 2 объекта класса Runner с произвольными именами.
        sprinter = Runner("Спринтер1")
        begun = Runner('Бегун')
        for i in range(10):  # 10 раз у объектов вызываются методы run и walk соответственно
            sprinter.run()  #
            begun.walk()  #
        self.assertNotEqual(sprinter.distance, begun.distance)  # Т.к. дистанции должны быть разными,
        # используем метод assertNotEqual, чтобы убедится в неравенстве результатов.


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls): # метод, где создаётся атрибут класса all_results.
        cls.all_results = {} # словарь в который будут сохраняться результаты всех тестов.

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self): # метод, где создаются 3 объекта:
        self.Usein = Runner("Usein", 10) # Бегун по имени Усэйн, со скоростью 10.
        self.Andrey = Runner("Andrey", 9) # Бегун по имени Андрей, со скоростью 9.
        self.Nik = Runner("Nik", 3) # Бегун по имени Ник, со скоростью 3.

    @classmethod
    def tearDownClass(cls): # метод, где выводятся all_results по очереди в столбец.
        for result in cls.all_results.values():
            show_result = {} # словарь для сохранения результатов забегов
            for place, runner in result.items(): # для места и бегуна в результате забега
                show_result[place] = runner.name # вывести место и имя бегуна, участников забега
            print(show_result) # печать результата забега

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_1(self): # Усэйн и Ник
        self.tournament = Tournament(90, self.Usein, self.Nik)
        self.all_results = self.tournament.start() # метод start, который возвращает словарь в
        # переменную all_results.
        last_runner_name = self.all_results[max(self.all_results.keys())].name # сравниваются последний
        # объект из all_results (брать по наибольшему ключу) и предполагаемое имя последнего бегуна.
        self.assertTrue(last_runner_name == "Nik") # метод assertTrue и предполагаемое имя последнего бегуна.
        TournamentTest.all_results[1] = self.all_results # вывод результата теста

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_2(self): # Андрей и Ник
        self.tournament_2 = Tournament(90, self.Andrey, self.Nik)
        self.all_results = self.tournament_2.start()
        last_runner_name = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(last_runner_name == "Nik")
        TournamentTest.all_results[2] = self.all_results

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_3(self): # Усэйн, Андрей и Ник
        self.tournament_3 = Tournament(90, self.Usein, self.Andrey, self.Nik)
        self.all_results = self.tournament_3.start()
        last_runner_name = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(last_runner_name == 'Nik')
        TournamentTest.all_results[3] = self.all_results


if __name__ == '__main__':
    unittest.main()