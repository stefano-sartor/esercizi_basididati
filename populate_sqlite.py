from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import csv
import sys
from pathlib import Path

from imdb import *

engine = create_engine("sqlite:///database.sqlite", echo=True, future=True)

Base.metadata.create_all(engine)


base_path = Path('data')

entity_list = [
    (base_path / 'actors.csv',  Actor),
    (base_path / 'directors.csv', Director),
    (base_path / 'movies.csv', Movie),
    (base_path / 'roles.csv', Role),
    (base_path / 'directors_genres.csv', DirectorsGenres),
    (base_path / 'movies_directors.csv', MoviesDirectors),
    (base_path / 'movies_genres.csv', MoviesGenres)]


def populate_table(path, Class):
    try:
        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            with Session(engine) as session:
                for row in reader:
                    session.add(Class(**row))
                session.commit()
        return True
    except Exception as e:
        print(e)
        return False


for path,Class in entity_list:
    if not populate_table(path,Class):
        print("'Errore, il programma terminera'")
        sys.exit(1)
        
print("popolazione delle tabelle entita' eseguita con successo")

