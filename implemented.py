from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.movie import MovieDAO
from service.director import DirectorService
from service.genre import GenreService
from service.movie import MovieService
from setup_db import db

# Создание переменных для соединения Dao и Service классов
movie_dao = MovieDAO(session=db.session)
movie_service = MovieService(movie_dao)

director_dao = DirectorDAO(session=db.session)
director_service = DirectorService(director_dao)

genre_dao = GenreDAO(session=db.session)
genre_service = GenreService(genre_dao)
