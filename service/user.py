import base64
import hashlib
import hmac

from helpers.constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS


class UserService:
    def __init__(self, dao):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_by_username(self, name):
        return self.dao.get_by_username(name)

    def create(self, data):
        data['password'] = self.generete_password(data['password'])
        return self.dao.create(data)

    def delete(self, uid):
        return self.dao.delete(uid)

    def generete_password(self, password):
        hash_pass = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS)
        return base64.b64encode(hash_pass)

    def compare_password(self, hash_password, password):
        decoded_password = base64.b64decode(hash_password)

        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS)

        return hmac.compare_digest(decoded_password, hash_digest)




