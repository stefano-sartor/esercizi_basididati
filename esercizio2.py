from sqlalchemy import create_engine
from imdb import *

engine = create_engine("sqlite:///database.sqlite", echo=True, future=True)

Base.metadata.create_all(engine)

