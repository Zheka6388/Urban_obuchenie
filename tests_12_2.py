import unittest

 # исходный код
class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants: # участник из списка участников
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers
 # исходный код

class TournamentTest(unittest.TestCase): # класс TournamentTest, наследованный от TestCase.
# cls обращается к классу и используется в методах класса, обозначенных декоратором @classmethod.
# cls применяют для внесения изменений, относящихся ко всему классу, тогда как self предназначен для
# взаимодействия с конкретным экземпляром.
    @classmethod
    def setUpClass(cls): # метод, где создаётся атрибут класса all_results.
        cls.all_results = {} # словарь в который будут сохраняться результаты всех тестов.

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

    def test_1(self): # Усэйн и Ник
        self.tournament = Tournament(90, self.Usein, self.Nik)
        self.all_results = self.tournament.start() # метод start, который возвращает словарь в
        # переменную all_results.
        last_runner_name = self.all_results[max(self.all_results.keys())].name # сравниваются последний
        # объект из all_results (брать по наибольшему ключу) и предполагаемое имя последнего бегуна.
        self.assertTrue(last_runner_name == "Nik") # метод assertTrue и предполагаемое имя последнего бегуна.
        TournamentTest.all_results[1] = self.all_results # вывод результата теста

    def test_2(self): # Андрей и Ник
        self.tournament_2 = Tournament(90, self.Andrey, self.Nik)
        self.all_results = self.tournament_2.start()
        last_runner_name = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(last_runner_name == "Nik")
        TournamentTest.all_results[2] = self.all_results

    def test_3(self): # Усэйн, Андрей и Ник
        self.tournament_3 = Tournament(90, self.Usein, self.Andrey, self.Nik)
        self.all_results = self.tournament_3.start()
        last_runner_name = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(last_runner_name == 'Nik')
        TournamentTest.all_results[3] = self.all_results


if __name__ == '__main__':
    unittest.main()
