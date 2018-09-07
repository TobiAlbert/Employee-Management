import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """
    Common Configurations
    """
    SECRET_KEY = 'fesrgwvregf24tfcw#'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or f'sqlite:///{os.path.join(basedir, "app.db")}'

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):

    """
    Development configurations
    """
    DEBUG=True
    SQLALCHEMY_ECHO=True


class ProductionConfig(Config):
    """
    Production Configurations
    """
    DEBUG=False


class TestingConfig(Config):
    """
    Testing Configurations
    """
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or f'sqlite:///{os.path.join(basedir, "test.db")}'


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}