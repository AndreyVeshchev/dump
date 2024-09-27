import numpy as np

# Задаем размеры матрицы, создав переменные n и p:
n = int(input("Введите количество строк n: "))
m = int(input("Введите количество столбцов m: "))

# Генерируем целочисленную матрицу A[n, m] с помощью генератора случайных чисел (вместо -10 и 10 можно поставить любые значения, это минимальное и максимальное возможное число в матрице)
A = np.random.randint(-10, 10, size=(n, m))
print("Сгенерированная матрица A:\n", A)

# Находим первый встреченный минимальный элемент и его индекс в матрице
min_value = A.min()
min_index = np.where(A == min_value)

# Получаем индекс первой строки матрицы, в которой найден минимальный элемент
first_min_index = min_index[0][0]

# Вставляем первую строку после строки, содержащей минимальный элемент
new_row = A[0]
A = np.insert(A, first_min_index + 1, new_row, axis=0) # Здесь A - матрица, first_min_index + 1 - индекс строки, куда вставляем первую строку, new_row - что вставляем, в нашем случае первая строка.
#  Параметр "axis" определяет, вдоль какой оси массива следует выполнять вставку значений. Оси всего две - 0 и 1, то есть строки и столбцы. Мы указываем "axis=0", значит вставка будет выполнена по строкам (вдоль первой оси).
# Это означает, что новые строки будут вставляться в массив, сдвигая существующие строки вниз.

print("Матрица после вставки первой строки:\n", A)

# Вычисляем медиану первой строки
first_row = A[0]

# Вычисление медианы с помощью стандартной функции
median_standard = np.median(first_row)

# Вычисление медианы через программирование формулы
#  Медиана - это средний элемент (или среднее двух средних элементов, если количество элементов четное)
Общие шаги для вычисления медианы:
# **Упорядочение данных**: Сначала все элементы должны быть отсортированы в порядке возрастания (или убывания).
# **Определение количества элементов**: Подсчитайте количество чисел в наборе, чтобы определить, четное оно или нечетное.
# **Вычисление медианы**: Если количество нечетное, используйте формулу для нахождения центрального элемента. Если количество четное, найдите два центральных элемента и усредните их.

# Для начала сортируем строку, т.е. выставляем все значения в порядке возрастания
sorted_data = sorted(first_row)

# Находим длину (количество чисел) в строке
n = len(sorted_data)

# Находим индекс (место в строке) элемента посередине строки)
mid = n // 2

if n % 2 == 0:  # если количество элементов чётное
    median_custom = (sorted_data[mid - 1] + sorted_data[mid]) / 2
else:  # если количество элементов нечётное
    median_custom = sorted_data[mid]

print("Медиана первой строки (стандартная функция):", median_standard)
print("Медиана первой строки (через программирование формулы):", median_custom)

# Код без комментариев:
import numpy as np

n = int(input("Введите количество строк n: "))
m = int(input("Введите количество столбцов m: "))
A = np.random.randint(-10, 10, size=(n, m))
print("Сгенерированная матрица A:\n", A)

min_value = A.min()
min_index = np.where(A == min_value)
first_min_index = min_index[0][0]
new_row = A[0]
A = np.insert(A, first_min_index + 1, new_row, axis=0)
print("Матрица после вставки первой строки:\n", A)

first_row = A[0]
median_standard = np.median(first_row)
sorted_data = sorted(first_row)
n = len(sorted_data)
mid = n // 2
if n % 2 == 0:
    median_custom = (sorted_data[mid - 1] + sorted_data[mid]) / 2
else:
    median_custom = sorted_data[mid]

print("Медиана первой строки (стандартная функция):", median_standard)
print("Медиана первой строки (через программирование формулы):", median_custom)

