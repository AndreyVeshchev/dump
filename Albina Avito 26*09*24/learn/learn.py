import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Загрузка данных
file_path = 'movies.csv'  # Укажите путь к вашему файлу
data = pd.read_csv(file_path)

"""Первичный анализ"""
# Выводим на экран первые 5 строк датафрейма для предварительного просмотра данных.
print(data.head())
# Показываем информацию о количестве строк, их типах данных и количестве отсутствующих (NaN) в строках значений.
print(data.info())
# Вычисляем и выводим базовые статистики для количественных переменных,
# такие как среднее, стандартное отклонение, минимумы и максимумы.
print(data.describe())

"""Проверка на наличие NaN значений"""
# Вычисляем и отображаем количество отсутствующих значений в каждом столбце.
missing_values = data.isnull().sum()
print("Отсутствующие значения:\n", missing_values[missing_values > 0])

"""Проверка типов данных"""
# Выводим типы данных для каждого столбца в датафрейме.
print(data.dtypes)

"""Визуализация при помощи boxplot
Используя визуализацию, мы выявляем выбросы в таких переменных,
как "score", "votes" и других количественных переменных."""
# Выбросы (аномальные значения) - наблюдения в датафрейме, которые существенно отличаются от остальных данных.
plt.figure(figsize=(12, 6))
sns.boxplot(data=data[['score', 'votes']])
plt.title('Boxplot для обнаружения выбросов')
plt.show()


# Выбор необходимых характеристик для модели
features = data[['director', 'writer', 'star', 'budget']]
target = data['score']

print("Характеристики для предсказания:\n", features.head())
print("Целевая переменная:\n", target.head())

# Проверим наличие пропущенных значений
print("Проверка на пропущенные значения:")
print(data.isnull().sum())

# Заполним пропущенные значения (например, пользователь может выбрать подходящий способ обработки)
# В данном случае мы просто удалим строки с NaN
data = data.dropna(subset=['director', 'writer', 'star', 'budget', 'score'])

# Теперь выберем необходимые характеристики и целевую переменную
features = data[['director', 'writer', 'star', 'budget']]
target = data['score']

# Кодирование категориальных переменных
features_encoded = pd.get_dummies(features, drop_first=True)

# Разделение данных на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(features_encoded, target, test_size=0.2, random_state=42)

# Создание модели линейной регрессии
model = LinearRegression()
model.fit(X_train, y_train)

# Предсказание на тестовой выборке
y_pred = model.predict(X_test)

# Оценка качества модели
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Среднеквадратичная ошибка:", mse)
print("Коэффициент детерминации R^2:", r2)
