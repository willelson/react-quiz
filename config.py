class Config(object):
    DEBUG = False
    PORT = 8080
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/reactquiz'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    # SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/todotest'