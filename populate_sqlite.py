from sqlalchemy.orm import Session
import csv
import sys
from pathlib import Path

import imdb as db


db.Base.metadata.create_all(db.engine)


base_path = Path('data')

entity_list = [
    (base_path / 'actors.csv',  db.Actor),
    (base_path / 'directors.csv', db.Director),
    (base_path / 'movies.csv', db.Movie),
    (base_path / 'roles.csv', db.Role),
    (base_path / 'directors_genres.csv', db.DirectorsGenres),
    (base_path / 'movies_directors.csv', db.MoviesDirectors),
    (base_path / 'movies_genres.csv', db.MoviesGenres)]


def populate_table(path, Class):
    try:
        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            with Session(db.engine) as session:
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

