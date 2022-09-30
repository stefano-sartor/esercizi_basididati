from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import csv
from pathlib import Path

from imdb import *

engine = create_engine("sqlite:///database.sqlite", echo=True, future=True)

Base.metadata.create_all(engine)



path = Path('data')

path_actors = path / 'actors.csv'
path_directors = path / 'directors.csv'
path_movies = path / 'movies.csv'

path_roles = path / 'roles.csv'
path_dir_gen = path / 'directors_generes.csv'
path_movie_dire = path / 'movies_directors.csv'



with open(path / 'actors.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    with Session(engine) as session:
        for row in reader:
            session.add( Actor(**row))
        session.commit()

with open(path / 'directors.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    with Session(engine) as session:
        for row in reader:
            session.add( Director(**row))
        session.commit()

with open(path / 'movies.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    with Session(engine) as session:
        for row in reader:
            session.add( Movie(**row))
        session.commit()

with open(path / 'roles.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    with Session(engine) as session:
        for row in reader:
            session.add( Role(**row))
        session.commit()

with open(path / 'directors_genres.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    with Session(engine) as session:
        for row in reader:
            session.add( DirectorsGenres(**row))
        session.commit()

with open(path / 'movies_directors.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    with Session(engine) as session:
        for row in reader:
            session.add( MoviesDirectors(**row))
        session.commit()

with open(path / 'movies_genres.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    with Session(engine) as session:
        for row in reader:
            session.add( MoviesGenres(**row))
        session.commit()