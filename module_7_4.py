# Заданные переменные
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2

# Рассчитываем результат соревнования
if score_1 > score_2 or (score_1 == score_2 and team1_time < team2_time):
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or (score_1 == score_2 and team1_time > team2_time):
    challenge_result = 'Победа команды Волшебники данных!'
else:
    challenge_result = 'Ничья!'

# Форматируем строки с использованием оператора %
team1_str = "В команде Мастера кода участников: %d !" % team1_num
teams_str = "Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num)

# Выводим результат для метода %
print(team1_str)
print(teams_str)

# Форматируем строки с использованием метода format()
team2_score_str = "Команда Волшебники данных решила задач: {} !".format(score_2)
team2_time_str = "Волшебники данных решили задачи за {} с !".format(team2_time)

print(team2_score_str)
print(team2_time_str)

# Форматируем строки с использованием f-строк
teams_score_str = f"Команды решили {score_1} и {score_2} задач."
challenge_result_str = f"Результат битвы: {challenge_result}"
tasks_info_str = f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!"


print(teams_score_str)
print(challenge_result_str)
print(tasks_info_str)
