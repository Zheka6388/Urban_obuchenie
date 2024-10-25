team1 = 'Мастера кода'
team2 = 'Волшебники данных'

def num(team1_num, team2_num):
    print('В команде %s участников: %s !' % (team1, team1_num)) # количество участников первой команды (Мастера кода)
    print('Итого сегодня в командах участников: %s и %s !' % (team1_num, team2_num)) # количество участников в обеих
    # командах
num(team1_num=5, team2_num=6)

def time(team1_time, team2_time, tasks_total=0):
    time_1 = team1_time
    time_2 = team2_time

    print('Команда {} решила задач: {}!'.format(team2, score_2)) # количество задач решённых командой 2
    print('{} решили задачи за {} cек. !'.format(team2, time_2)) #  время за которое команда 2 решила задачи
score_1 = 40
score_2 = 42
time(team1_time=1552.512, team2_time=2153.31451)

def challenge_result(tasks_total, time_avg): # количество решённых задач по командам
    print(f'Команды решили {score_1} и {score_2} задач')
    if score_1 > score_2: # если кол-во решённых задач первой командой > чем кол-во решённых задач второй командой
        print(f'Результат битвы: победа команды {team1} !') # исход соревнования (challenge_result)
    else: # иначе
        print(f'Результат битвы: победа команды {team2} !') # исход соревнования (challenge_result)

    print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу') # количество задач
    # (tasks_total) и среднее время решения (time_avg)
challenge_result(tasks_total=82, time_avg=45.2)