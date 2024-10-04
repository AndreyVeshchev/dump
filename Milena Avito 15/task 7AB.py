import pandas as pd

# Загружаем данные из CSV файла
data = pd.read_csv('StudentsPerformance.csv')

# Фильтруем данные для девочек
girls_data = data[data['gender'] == 'female']

# Вычисляем средний балл по чтению
average_reading_score = girls_data['reading score'].mean()

# Округляем до трех знаков после запятой
average_reading_score_rounded = round(average_reading_score, 3)

# Выводим результат
print(average_reading_score_rounded)


# Определяем функцию для обработки каждой строки
def categorize(row):
    lunch_count = row['lunch'].count('r')  # Считаем количество букв "r" в столбце 'lunch'

    if lunch_count > 1:
        if row['gender'] == 'female':
            return "1 cat"
        else:
            return "2 cat"
    else:
        return "3 cat"


# Применяем функцию ко всему DataFrame и создаем новый столбец 'category'
data['category'] = data.apply(lambda row: categorize(row), axis=1)

# Выводим результат
print(data[['gender', 'lunch', 'category']])
