from dao.movie import MovieDAO
from dao.genre import GenreDAO
from dao.director import DirectorDAO

from service.genre import GenreService
from service.director import DirectorService
from service.movie import MovieService

from setup_db import db

movie_dao = MovieDAO(session=db.session)
movie_service = MovieService(movie_dao=movie_dao)

genre_dao = GenreDAO(session=db.session)
genre_service = GenreService(genre_dao=genre_dao)

director_dao = DirectorDAO(session=db.session)
director_service = DirectorService(director_dao=director_dao)