"""Дана матрица A(N,M), которая вводится из файла, и число k, вводимое с клавиатуры.
В k-ой строке найти максимальный элемент.
В том столбце, где этот элемент находится, найти сумму отрицательных элементов.
Каждый этап решать при помощи подпрограммы, работающей с вектором. Вектор «вырезать» из матрицы."""

import pandas as pd
import numpy as np


def load_matrix_from_csv(filename):
    """Загрузить матрицу из CSV файла."""
    # Эта функция принимает имя файла filename как аргумент.
    # Использует функцию pd.read_csv для чтения содержимого CSV файла.
    # Параметр header=None указывает, что в файле нет заголовков, и все строки считаются данными.
    return pd.read_csv(filename, header=None).values


def find_max_in_row(matrix, k):
    """Найти максимальный элемент в k-ой строке матрицы."""
    # Эта функция принимает матрицу matrix и индекс строки k.
    # Метод matrix[k].max() извлекает максимальное значение в строке с индексом k,
    # а matrix[k].argmax() находит индекс этого максимума в строке.
    # Функция возвращает кортеж, состоящий из максимального значения и его индекса.
    return matrix[k].max(), matrix[k].argmax()


def sum_negative_in_column(matrix, column_index):
    """Найти сумму отрицательных элементов в указанном столбце."""
    # Эта функция принимает матрицу matrix и индекс столбца column_index.
    # Она использует условие matrix[:, column_index] < 0,
    # чтобы получить массив всех отрицательных значений в указанном столбце.
    # Затем, с помощью np.sum(), суммируются все эти значения, и результат возвращается.
    return np.sum(matrix[matrix[:, column_index] < 0, column_index])


def main():
    """Основная функция программы"""
    # Внутри функции main() задается имя CSV файла, откуда будет загружаться матрица.
    # Далее мы загружаем матрицу с помощью функции load_matrix_from_csv().
    filename = 'matrix.csv'  # Укажите имя вашего CSV файла
    matrix = load_matrix_from_csv(filename)

    # Затем запрашиваем у пользователя номер строки k, используя input().
    # С помощью matrix.shape[0] проверяем количество строк в матрице.
    k = int(input(f"Введите номер строки (0-{matrix.shape[0] - 1}): "))

    # Если пользователь ввел неверный индекс строки, выводим сообщение об ошибке и завершаем программу.
    if k < 0 or k >= matrix.shape[0]:
        print("Неверный номер строки")
        return

    # Мы вызываем функцию find_max_in_row(), чтобы получить максимальное значение и индекс его местоположения в строке.
    max_value, column_index = find_max_in_row(matrix, k)
    print(f"Максимальный элемент в строке {k}: {max_value}")

    # Находим сумму отрицательных элементов в указанном столбце
    negative_sum = sum_negative_in_column(matrix, column_index)
    print(f"Сумма отрицательных элементов в столбце {column_index}: {negative_sum}")

# Запускаем программу
main()
