import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgres://%s:%s@%s:%s/%s' % (os.environ['BILLS_API_DB_USER'],
                                                            os.environ['BILLS_API_DB_PASS'],
                                                            os.environ['BILLS_API_DB_URL'],
                                                            os.environ['BILLS_API_DB_PORT'],
                                                            'auth_dev_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgres://%s:%s@%s:%s/%s' % (os.environ['BILLS_API_DB_USER'],
                                                            os.environ['BILLS_API_DB_PASS'],
                                                            os.environ['BILLS_API_DB_URL'],
                                                            os.environ['BILLS_API_DB_PORT'],
                                                            'auth_test_db')
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgres://%s:%s@%s:%s/%s' % (os.environ['BILLS_API_DB_USER'],
                                                            os.environ['BILLS_API_DB_PASS'],
                                                            os.environ['BILLS_API_DB_URL'],
                                                            os.environ['BILLS_API_DB_PORT'],
                                                            'auth_prod_db')


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
