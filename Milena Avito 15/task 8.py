import pandas as pd


def filter_comedy_movies(df):
    """Фильтровать фильмы жанра 'комедия'."""
    # функция формирует новый датафрейм, оставляя только те данные, которые имеют в столбце 'genres' значение 'Comedy'
    # .str переводит значение из столбца 'genres' в строку, а .contains проверяет на наличие в строке 'Comedy'
    # параметр case = False отвечает за то, что проверка не будет привязана к регистру (заглавные или строчные буквы)
    # параметр na = False отвечает за то, что если значенеи из столбца будет пустым, на это место будет добавлено False
    return df[df['genres'].str.contains('Comedy', case=False, na=False)]


def explode_companies(df):
    """Разделить строки с несколькими студиями и создать новый DataFrame."""
    # Разделяем студии по символу '|' и разворачиваем DataFrame
    # создаём копию датафрейма с помощью copy(), включая туда только столцы 'production_companies' и 'revenue'
    exploded = df[['production_companies', 'revenue']].copy()
    # разделяем компании из столбца 'production_companies' на основе нахлждения символа '|'
    # перед этим переводим значение столбца в строку. По итогу, если в значении было несколько компаний,
    # они будут сохранены списком
    exploded['production_companies'] = exploded['production_companies'].str.split('|')
    # разделяем все компании из полученных списков в новые строки в датафрейме, используя .explode
    exploded = exploded.explode('production_companies')
    return exploded


def get_top_studio_in_comedy(df):
    """Определить студию с наибольшими сборами в жанре комедии."""
    # Создаем сводную таблицу с сборами по студиям
    # с помощью метода groupby объединяем строки, относящиеся к одинаковым компаниям в одну на компанию,
    # суммируя при этом доходы от фильмов с помощью .sum()
    # reset_index() возвращает нумерацию датафрейма с нуля
    studio_revenue = df.groupby('production_companies')['revenue'].sum().reset_index()
    # Находим студию с максимальными сборами
    # при помощи loc находим номер строки с максимальным значением дохода (.idxmax)
    top_studio = studio_revenue.loc[studio_revenue['revenue'].idxmax()]
    return top_studio


films_data = pd.read_csv('films.csv')

# Фильтруем комедийные фильмы
comedy_movies = filter_comedy_movies(films_data)

# Разворачиваем студии
exploded_movies = explode_companies(comedy_movies)

# Находим студию с наибольшими сборами
top_studio = get_top_studio_in_comedy(exploded_movies)

print(f"Студия с наибольшими сборами в жанре комедии: {top_studio['production_companies']} "
      f"с общими сборами: ${top_studio['revenue']:,.2f}")
