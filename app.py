from flask import Flask
from flask_restx import Api
from helpers.config import Config
from dao.model.user import User
from helpers.setup_db import db
from views.director import directors_ns
from views.genre import genres_ns
from views.movie import movies_ns
from views.user import users_ns
from views.auth import auth_ns


def create_app(config_object):
    """Создание Flask app и применение конфига """
    application = Flask(__name__)
    application.config.from_object(config_object)
    application.app_context().push()
    register_extensions(application)
    return application


def create_data(app, db):
    with app.app_context():
        db.create_all()

        u1 = User(username="vasya", password="my_little_pony", role="user")
        u2 = User(username="oleg", password="qwerty", role="user")
        u3 = User(username="oleg", password="P@ssw0rd", role="admin")

        with db.session.begin():
            db.session.add_all([u1, u2, u3])


def register_extensions(application):
    """Подключение Api и создание namespace"""
    db.init_app(application)
    api = Api(application)
    api.add_namespace(movies_ns)
    api.add_namespace(directors_ns)
    api.add_namespace(genres_ns)
    api.add_namespace(users_ns)
    api.add_namespace(auth_ns)


if __name__ == '__main__':
    app = create_app(Config())
    app.run(port=8080)
