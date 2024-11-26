import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Загрузка данных
file_path = 'spotify_songs.csv'  # Укажите путь к вашему файлу
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
как "danceability", "energy", "loudness" и других количественных переменных."""
# Выбросы (аномальные значения) - наблюдения в датафрейме, которые существенно отличаются от остальных данных.
plt.figure(figsize=(12, 6))
sns.boxplot(data=data[['danceability', 'energy', 'loudness']])
plt.title('Boxplot для обнаружения выбросов')
plt.show()

"""Мы хотим отфильтровать треки, которые имеют высокую "danceability" и "energy". 
Для этого мы можем установить пороговые значения."""
# Установим пороговое значение
danceability_threshold = 0.7
energy_threshold = 0.7

# Фильтрация данных
# Условная фильтрация датафрейма, где оставлены только те строки,
# где значения "danceability" и "energy" превышают заданные пороги.
filtered_data = data[(data['danceability'] > danceability_threshold) & (data['energy'] > energy_threshold)]
print("Отфильтрованные данные:\n", filtered_data.head())

"""Предположим, мы хотим предсказать уровень популярности трека (например, popularity) 
на основе его характеристик, таких как danceability, energy, loudness и других параметров."""
# Выбираем необходимые характеристики
# Создание двух новых переменных: features — это DataFrame, содержащий независимые переменные
# target — это зависимая переменная, которую мы будем предсказывать.
features = data[['danceability', 'energy', 'loudness', 'valence', 'tempo']]
target = data['track_popularity']

# train_test_split: Разделяет данные на обучающую (80%) и тестовую (20%) выборки.
# Параметр random_state обеспечивает воспроизводимость.
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Создаем и обучаем модель
# LinearRegression(): Создает объект модели линейной регрессии.
# model.fit(X_train, y_train) обучает модель на обучающем наборе данных.
model = LinearRegression()
model.fit(X_train, y_train)

# Предсказание
# model.predict(X_test) генерирует предсказания на основании тестовой выборки.
y_pred = model.predict(X_test)

# Оценка качества модели
# mean_squared_error вычисляет среднюю квадратичную ошибку между реальными значениями и предсказанными.
# r2_score оценивает качество модели: насколько хорошо модель объясняет вариации в целевой переменной.
# R² принимает значения от 0 до 1, где 1 — идеальная модель.
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("Средняя квадратичная ошибка:", mse)
print("Оценка R^2:", r2)

# Получаем коэффициенты модели
# Создается датафрейм, содержащий коэффициенты линейной регрессии для каждой из независимых переменных,
# что показывает их влияние на целевую переменную.
coefficients = pd.DataFrame(model.coef_, features.columns, columns=['Coefficient'])
print("\nКоэффициенты модели:")
print(coefficients)

# Сравниваем предсказанные значения с реальными
# Создается датафрейм для визуального сравнения реальных и предсказанных значений, 
# что позволяет оценить качество предсказания.
results = pd.DataFrame({'Реальные': y_test, 'Предсказанные': y_pred})
print("\nСравнение фактических и предсказанных значений:")
print(results.head())
