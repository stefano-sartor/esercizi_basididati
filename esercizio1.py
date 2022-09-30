import csv
from pathlib import Path

path_data = Path('data')

path_actors = path_data / 'actors.csv'
path_directors = path_data / 'directors.csv'
path_movies = path_data / 'movies.csv'

path_roles = path_data / 'roles.csv'
path_dir_gen = path_data / 'directors_generes.csv'
path_movie_dire = path_data / 'movies_directors.csv'



with open(path_actors) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)