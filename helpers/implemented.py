from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.movie import MovieDAO
from dao.user import UserDAO
from service.auth import AuthService
from service.director import DirectorService
from service.genre import GenreService
from service.movie import MovieService
from service.user import UserService
from helpers.setup_db import db

# Создание переменных для соединения Dao и Service классов
movie_dao = MovieDAO(session=db.session)
movie_service = MovieService(movie_dao)

director_dao = DirectorDAO(session=db.session)
director_service = DirectorService(director_dao)

genre_dao = GenreDAO(session=db.session)
genre_service = GenreService(genre_dao)

user_dao = UserDAO(session=db.session)
user_service = UserService(user_dao)

auth_service = AuthService(UserService(user_dao))
