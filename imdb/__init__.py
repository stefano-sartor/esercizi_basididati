from sqlalchemy import Column, Float, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

# declarative base class
Base = declarative_base()

class Actor(Base):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    gender = Column(String(1))

    roles = relationship('Role',back_populates='actor')


class Director(Base):
    __tablename__ = 'directors'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(100))
    last_name = Column(String(100))

    genres = relationship('DirectorsGenres', back_populates='director')
    movies = relationship('MoviesDirectors', back_populates='director')


class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    year = Column(Integer)
    quality = Column(Integer)

    directors = relationship('MoviesDirectors', back_populates='movie')
    genres = relationship('MoviesGenres', back_populates='movie')
    roles = relationship('Role', back_populates='movie')


class DirectorsGenres(Base):
    __tablename__ = 'directors_genres'

    id = Column(Integer, primary_key=True)
    genre = Column(String(100))
    prob = Column(Float)

    director_id  = Column(ForeignKey("directors.id"))

    director = relationship('Director',back_populates='genres')


class MoviesDirectors(Base):
    __tablename__ = 'movies_directors'

    id = Column(Integer, primary_key=True)

    director_id  = Column(ForeignKey("directors.id"))
    movie_id     = Column(ForeignKey("movies.id"))

    director = relationship('Director',back_populates='movies')
    movie = relationship('Movie',back_populates='directors')

   

class MoviesGenres(Base):
    __tablename__ = 'movies_genres'

    id = Column(Integer, primary_key=True)
    genre = Column(String(100))

    movie_id     = Column(ForeignKey("movies.id"))

    movie = relationship('Movie',back_populates='genres')



class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    role = Column(String(100))

    actor_id     = Column(ForeignKey("actors.id"))
    movie_id     = Column(ForeignKey("movies.id"))

    movie = relationship('Movie',back_populates='roles')
    actor = relationship('Actor',back_populates='roles')

