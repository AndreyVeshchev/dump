import pandas as pd
import numpy as np

def read_matrix_from_csv(file_name):
    """Функция для чтения матрицы из CSV файла."""
    return pd.read_csv(file_name, header=None).values  # Чтение без заголовка

def sum_of_absolute_values(column):
    """Функция для вычисления суммы модулей элементов в векторе (столбце)."""
    return np.sum(np.abs(column))

def get_column(matrix, col_index):
    """Функция для извлечения столбца из матрицы."""
    return matrix[:, col_index]

def find_min_col_sum(matrix):
    """Функция для поиска столбца с наименьшей суммой модулей элементов."""
    min_sum = float('inf')
    min_col_index = -1
    
    for col_index in range(matrix.shape[1]):
        column = get_column(matrix, col_index)
        curr_sum = sum_of_absolute_values(column)

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
    file_name = 'matrix.csv'  # Замените на имя вашего файла
    matrix = read_matrix_from_csv(file_name)

    # Поиск и вывод столбца с наименьшей суммой модулей
    min_col_index = find_min_col_sum(matrix)
    display_column(matrix, min_col_index)

if __name__ == '__main__':
    main()
