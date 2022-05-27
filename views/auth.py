from flask import request
from flask_restx import Resource, Namespace
from helpers.implemented import auth_service

auth_ns = Namespace('auth')


@auth_ns.route('/')
class AuthsView(Resource):
    def post(self):
        """Получение токена по данным пользователя"""
        data = request.json

        username = data.get('username', None)
        password = data.get('password', None)
        print(username, password)
        if None in [username, password]:
            return "", 400

        token = auth_service.generate_token(username, password)
        return token

    def put(self):
        """Запрос на обновление токена с помощью 'refresh_token'"""
        data = request.get_json()
        token = data.get('refresh_token')

        tokens = auth_service.approve_refresh_token(token)

        return tokens, 201
