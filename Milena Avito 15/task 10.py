import pandas as pd
import numpy as np

def read_matrix_from_csv(file_name):
    """Функция для чтения матрицы из CSV файла."""
    # Благодаря .values данная функция передаёт лишь значения матрицы, заголовок отсутствует
    return pd.read_csv(file_name, header=None).values  # Чтение без заголовка

def sum_of_absolute_values(column):
    """Функция для вычисления суммы модулей элементов в векторе (столбце)."""
    # Метод .sum() позволяет высчитать сумму вектора, в нашем случае столбца
    № Метод .abs() возвращает модули всех чисел в столбце
    return np.sum(np.abs(column))

def get_column(matrix, col_index):
    """Функция для извлечения столбца из матрицы."""
    # Двоеточие указывает на то, что будет срезан весь столбец, от начала и до конца
    # col_index указывает номер (индекс) столбца, который мы срезаем
    return matrix[:, col_index]

def find_min_col_sum(matrix):
    """Функция для поиска столбца с наименьшей суммой модулей элементов."""
    # Переменная min_sum будет использоваться для хранения суммы минимального столбца.
    # Сам минимальный столбец будет определяться через сравнение с данной переменной, поэтому изначально даём ей бесконечность ('inf'), т.е. отсутствие отпределённого значения
    min_sum = float('inf')
    # Переменная min_col_index нужна для определения номера (индекса) столбца с минимальной суммой. 
    # Изначально даём ей значение -1, чтобы указать отсутствие индекса в начале программы, т.к. минимальный возможный индекс - 0
    min_col_index = -1

    # Цикл проходит по всем столбцам матрицы (используя matrix.shape[1] для получения числа столбцов).
    for col_index in range(matrix.shape[1]):
        column = get_column(matrix, col_index) # Извлекаем из матрицы столбец и сохраняем в переменную column
        curr_sum = sum_of_absolute_values(column) # Вычисляем сумму модулей и созраняем её

        # Если текущая сумма меньше минимальной (min_sum), перезаписываем переменную min_sum и индекс столбца (min_col_index).
        if curr_sum < min_sum:
            min_sum = curr_sum
            min_col_index = col_index
            
    return min_col_index

def display_column(matrix, col_index):
    """Функция для вывода элементов указанного столбца."""
    print("Столбец с наименьшей суммой модулей элементов:")
    print(get_column(matrix, col_index))

def main():
    # Чтение матрицы из файла
    file_name = 'matrix.csv'  # Название вашей матрицы
    matrix = read_matrix_from_csv(file_name)

    # Поиск и вывод столбца с наименьшей суммой модулей
    min_col_index = find_min_col_sum(matrix)
    display_column(matrix, min_col_index)


main()
