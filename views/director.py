from flask import request
from flask_restx import Resource, Namespace
from dao.model.director import DirectorSchema
from implemented import director_service

directors_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@directors_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        director = director_service.get_all()
        return directors_schema.dump(director), 200

    def post(self):
        data = request.get_json()
        director_service.create(data)
        return "Успешно создано", 201


@directors_ns.route("/<int:did>")
class DirectorView(Resource):
    def get(self, did):
        director = director_service.get_one(did)
        return director_schema.dump(director), 200

    def put(self, did):
        data = request.get_json()
        data['id'] = did

        director_service.update(data)

        return "Успешно обновлено"

    def delete(self, did):
        director_service.delete(did)

        return "Удалено", 204
