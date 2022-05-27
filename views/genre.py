from flask import request
from flask_restx import Resource, Namespace

from dao.model.genre import GenreSchema
from helpers.decorators import auth_required, admin_required
from helpers.implemented import genre_service

genres_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genres_ns.route('/')
class GenresView(Resource):
    @auth_required
    def get(self):
        genre = genre_service.get_all()

        return genres_schema.dump(genre), 200
    @admin_required
    def post(self):
        data = request.get_json()
        genre_service.create(data)

        return "Успешно создано", 201


@genres_ns.route("/<int:gid>")
class GenreView(Resource):
    @auth_required
    def get(self, gid):
        genre = genre_service.get_one(gid)

        return genre_schema.dump(genre), 200

    @admin_required
    def put(self, gid):
        data = request.get_json()
        data['id'] = gid

        genre_service.update(data)

        return "Успешно обновлено"

    @admin_required
    def delete(self, gid):
        genre_service.delete(gid)

        return "Успешно удалено", 204
