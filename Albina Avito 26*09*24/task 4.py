import pandas as pd  # Импортируем библиотеку pandas для работы с данными в таблицах

# Загружаем данные из файла films.csv в датафрейм df
df = pd.read_csv('films.csv')


# Определяем (создаём) функцию для вычисления прибыльных фильмов
def profitable_genre(data):
    # Вычисляем прибыль: разность между сборами и бюджетом
    data['profit'] = data['revenue'] - data['budget']

    # Оставляем только прибыльные фильмы (где прибыль больше 0)
    profitable_movies = data[data['profit'] > 0]

    # Создаём словарь для хранения количества прибыльных фильмов по жанрам
    # Каждый жанр будет хранить количество прибыльных фильмов в этом жанре
    genre_counts = {}

    # Подсчёт количества прибыльных фильмов по каждому жанру
    for genres in profitable_movies['genres']:  # Проходим по всем жанрам прибыльных фильмов с помощью цикла
        for genre in genres.split('|'):  # Разделяем жанры по символу '|'
            genre = genre.strip()  # Убираем лишние пробелы перед и после названия жанра
            if genre in genre_counts:  # Если жанр уже есть в словаре, то делаем следующее:
                genre_counts[genre] += 1  # Увеличиваем счётчик для этого конкретного жанра (например "комедия")
            else:
                genre_counts[genre] = 1  # В противном случае, создаём новый ключ с начальным значением 1

    # Находим жанр с максимальным количеством прибыльных фильмов (key обозначает, что определять будем через значения в
    # словаре, т.е. через количество фильмов в определённом жанре)
    return max(genre_counts, key=genre_counts.get)


# Вызов функции для определения жанра с наибольшим количеством прибыльных фильмов
most_profitable_genre = profitable_genre(df)

# Выводим результат
print('Жанр с наибольшим количеством прибыльных фильмов:', most_profitable_genre)
