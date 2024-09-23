import numpy as np

n = int(input("Введите размер матрицы n: "))

# Генерируем случайную вещественную (числа с дробной частью, вместо -10 и 10 можно поставить любые значения) матрицу A[n, n]
A = np.random.uniform(-10, 10, (n, n))

print("Сгенерированная матрица :", A)

# Находим наименьший элемент на побочной диагонали
# Элементы побочной диагонали имеют индексы (i, n-i-1)

# Инициализируем с помощью бесконечности. Не может дать переменной значения меньше нуля, т.к. в матрице могут быть отрицательыне числа
min_element = float('inf')

# Делаем проход по матрице
for i in range(n):
    # Вычисляем индекс побочной диагонали
    j = n - i - 1
    if A[i][j] < min_element:
        min_element = A[i][j]

print("Наименьший элемент на побочной диагонали:", min_element)

# Извлекаем элементы побочной диагонали и записываем их в переменную
secondary_diagonal = []
for i in range(n):
    secondary_diagonal.append(A[i][n - i - 1])
print(secondary_diagonal)

# Способ 1: использование стандартной функции из библиотеки NumPy для вычисления дисперсии
variance_std = np.var(secondary_diagonal)
print("Дисперсия побочной диагонали с использованием стандартной функции:", round(variance_std, 2))

# Способ 2: программирование формулы дисперсии 
# Находим среднее значение, необходимое по формуле
mean = np.mean(secondary_diagonal)

#  Находим дисперсию по формуле: сумма квадратов отклонений от среднего, делённая на количество элементов.
variance = []
for x in secondary_diagonal:
    variance.append((x - mean) ** 2)
variance_manual = sum(variance) / n
print("Дисперсия побочной диагонали с использованием формулы:", round(variance_manual, 2))
