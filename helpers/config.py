class Config:
    """config для работы с Flask"""
    DEBUG = True
    SECRET_HERE = '249y823r9v8238r9u'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///movies.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ENSURE_AS_ASCII = False
    RESTX_JSON = {'ensure_ascii': False, 'indent': 4}

