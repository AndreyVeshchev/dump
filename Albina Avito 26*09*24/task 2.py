# Импортируем библиотеку Pandas для работы с файлами формата .csv
import pandas as pd

# Записываем в переменную data все данные из файла football.csv для дальнейшей работы
data = pd.read_csv('football.csv')
print(data)

# Находим максимальное число забитых пенальти среди всех игроков
max_penalties = data['Penalties'].max()
print(max_penalties)

# Находим игроков, которые забили максимальное число пенальти
players_with_max_penalties = data[data["Penalties"] == max_penalties]
print(players_with_max_penalties)

# Вычисляем среднюю зарплату игроков, забивающих максимальное число пенальти
average_wage_max_penalties = players_with_max_penalties["Wage"].mean()
print(average_wage_max_penalties)

# Находим максимальную точность удара головой среди всех игроков
max_heading_accuracy = data["HeadingAccuracy"].max()
print(max_heading_accuracy)

# Находим игроков с максимальной точностью удара головой
players_with_max_heading_accuracy = data[data["HeadingAccuracy"] == max_heading_accuracy]
print(players_with_max_heading_accuracy)

# Вычисляем среднюю зарплату игроков, имеющих максимальную точность удара головой
average_wage_max_heading_accuracy = players_with_max_heading_accuracy["Wage"].mean()
print(average_wage_max_heading_accuracy)

# Рассчитываем, во сколько раз средняя зарплата игроков, забивающих максимальное число пенальти, выше средней
# зарплаты игроков с максимальной точностью удара головой
ratio = average_wage_max_penalties / average_wage_max_heading_accuracy
print("Средняя зарплата игроков, забивающих максимальное число пенальти, в", ratio, "раз выше средней зарплаты игроков с максимальной точностью:", average_wage_max_penalties)
