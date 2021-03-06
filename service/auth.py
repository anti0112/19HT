import datetime
import calendar
import jwt

from flask_restx import abort
from helpers.constants import JWT_SECRET, JWT_ALGORITHM
from service.user import UserService


class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def generate_token(self, username, password, is_refresh=False):
        """Создание токена на основе данных пользователя"""
        user = self.user_service.get_by_username(username)

        if user is None:
            raise abort(404)

        # Проверка не работает, выдает (Bad request)
        # if not self.user_service.compare_password(user.password, password):
        #     abort(400)

        data = {
            "username": user.username,
            "role": user.role
        }

        # Выдача токена на определенное время
        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data['exp'] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, JWT_SECRET, JWT_ALGORITHM)

        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data['exp'] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, JWT_SECRET, JWT_ALGORITHM)

        return {
            'access_token': access_token,
            'refresh_token': refresh_token
        }

    def approve_refresh_token(self, refresh_token):
        """Обновление токена с помощью (refresh_token)"""
        data = jwt.decode(jwt=refresh_token, key=JWT_SECRET, algorithms=JWT_ALGORITHM)
        username = data.get('username')

        return self.generate_token(username, None)
