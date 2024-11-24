import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Загрузка данных
file_path = 'spotify_songs.csv'  # Укажите путь к вашему файлу
data = pd.read_csv(file_path)

# Первичный анализ
print(data.head())  # Первые 5 строк
print(data.info())  # Информация о типах данных и NaN значениях
print(data.describe())  # Статистический анализ количественных переменных

# Проверка на наличие NaN значений
missing_values = data.isnull().sum()
print("Отсутствующие значения:\n", missing_values[missing_values > 0])

# Проверка типов данных
print(data.dtypes)

# Визуализация при помощи boxplot
"""Используя визуализацию, мы можем выявить выбросы в таких переменных, 
как "danceability", "energy", "loudness" и других количественных переменных."""
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
filtered_data = data[(data['danceability'] > danceability_threshold) & (data['energy'] > energy_threshold)]
print("Отфильтрованные данные:\n", filtered_data.head())

"""Предположим, мы хотим предсказать уровень популярности трека (например, popularity) 
на основе его характеристик, таких как danceability, energy, loudness и других параметров."""

# Выбираем необходимые характеристики
features = data[['danceability', 'energy', 'loudness', 'valence', 'tempo']]
target = data['track_popularity']  # Целевая переменная

# Разделяем данные на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Создаем и обучаем модель
model = LinearRegression()
model.fit(X_train, y_train)

# Предсказание
y_pred = model.predict(X_test)

# Оценка качества модели
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("R^2 Score:", r2)

# Получаем коэффициенты модели
coefficients = pd.DataFrame(model.coef_, features.columns, columns=['Coefficient'])
print("\nКоэффициенты модели:")
print(coefficients)

# Сравниваем предсказанные значения с реальными
results = pd.DataFrame({'Реальные': y_test, 'Предсказанные': y_pred})
print("\nСравнение фактических и предсказанных значений:")
print(results.head())
