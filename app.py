from flask import Flask
from flask_restx import Api
from config import Config
from setup_db import db
from views.director import directors_ns
from views.genre import genres_ns
from views.movie import movies_ns


def create_app(config_object):
    """Создание Flask app и применение конфига """
    application = Flask(__name__)
    application.config.from_object(config_object)
    application.app_context().push()
    register_extensions(application)
    return application


def register_extensions(application):
    """Подключение Api и создание namespace"""
    db.init_app(application)
    api = Api(application)
    api.add_namespace(movies_ns)
    api.add_namespace(directors_ns)
    api.add_namespace(genres_ns)


if __name__ == '__main__':
    app = create_app(Config())
    app.run()
