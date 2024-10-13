from time import sleep # импорт функции sleep из модуля time.

class User: # класс для сбора данных пользователя

    def __init__(self, nickname, password, age): # Атрибуты: nickname(имя пользователя, строка), password(в
        # хэшированном виде, число), age(возраст, число)
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname

    def __hash__(self):
        return hash(self.password)

class Video: # класс для характеристик видео

    def __init__(self, title, duration, adult_mode = False): # Атрибуты: title(заголовок, строка),
        # duration(продолжительность, секунды), time_now(секунда остановки (изначально 0)), adult_mode(ограничение
        # по возрасту, bool (False по умолчанию))
        self.title = title # заголовок, строка
        self.duration = duration # продолжительность, секунды
        self.time_now = 0# секунда остановки (изначально 0)
        self.adult_mode = adult_mode # ограничение по возрасту

    def __str__(self):
        return f'{self.title}'

    def __eq__(self, other):
        return self.title == other.title

    def __contains__(self, item):
        return item in self.title


class UrTube(User, Video): # класс, собирающий все данные
    def __init__(self):
        self.users = []  # список объектов класса User
        self.videos = []  # список объектов класса Video
        self.current_user = None  # текущий пользователь

    def register(self, nickname, password, age): # Метод register, который принимает три аргумента: nickname,
        # password, age
        password = hash(password) # сравнивается по хэшу.
       # new_user = User(nickname, password, age) # регистрация нового пользователя
       # self.users.append(new_user) # добавить в список объектов класса User
       # self.current_user = new_user # текущий пользователь
        for user in self.users: # цикл для поиска пользователя в списке объектов класса User
            if user.nickname == nickname: # если пользователь есть в списке объектов класса User
                print(f"Пользователь {nickname} уже существует")
                return

        new_user = User(nickname, password, age) # регистрация нового пользователя
        self.users.append(new_user) # добавить в список объектов класса User
        self.current_user = new_user # текущий пользователь

    def log_in(self, nickname, password): # Метод log_in, который принимает на вход аргументы: nickname, password
        for user in self.users: # цикл для поиска пользователя в списке объектов класса User
            if nickname == user.nickname and password == user.password: # если логин и пароль совпадают с логином
                # и паролем из списка объектов класса User
                self.current_user = user # Если такой пользователь существует, то current_user меняется на найденного

    def log_out(self): # Метод log_out для сброса текущего пользователя на None
        self.current_user = None

# ur = UrTube()
# ur.register('vasya_pupkin', 'lolkekcheburek', 13)
# ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
# ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
# print(ur.current_user)

    def add(self, *videos): # Метод add, который принимает неограниченное кол-во объектов класса Video и все
        # добавляет в videos, если с таким же названием видео ещё не существует.
        for video in videos: # цикл проверки наличия видео в videos
            if video not in self.videos: # если видео нет в списоке объектов класса Video
                self.videos.append(video) # добавляет видео в список объектов класса Video

    def get_videos(self, word): # Метод get_videos, который принимает поисковое слово и возвращает список названий
        # всех видео, содержащих поисковое слово.
        list_1 = [] # список названий всех видео
        for video in self.videos: # цикл проверки наличия видео в списоке объектов класса Video
            if word.upper() in video.title.upper(): # если поисковое слово в верхнем регистре есть в названии
                # видео в верхнем регистре, то
                list_1.append(video.title) # добавить название видео в список названий всех видео
        return list_1


    def watch_video(self, film): # Метод watch_video, который принимает название фильма
        if not self.current_user: # если текущего пользователя нет
            print('Войдите в аккаунт, чтобы смотреть видео.')
            return

        for video in self.videos: # цикл для проверки видео на ограничение по возрасту
            if video.title == film:
                if video.adult_mode and self.current_user.age < 18: # если ограничение по возрасту и возраст
                    # пользователя < 18
                    print('Вам нет 18 лет, пожалуйста, покиньте страницу!')
                    return

                for i in range( video.duration): # присваиваем переменной i последовательность протяженности видео
                    print(i + 1, end = ' ') # вывод на экран продолжительности видео
                    sleep(1) # с паузой между выводами секунд воспроизведения
                    video.time_now += 1 # ведётся отчёт в консоль на какой секунде ведётся просмотр
                video.time_now = 0 # После текущее время просмотра данного видео сбрасывается.
                print('Конец видео.')
                sleep(2) # пауза после вывода 'Конец видео.'


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 год')
