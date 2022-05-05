import os


# BaseConfigクラスを作成する
class BaseConfig:
    SECRET_KEY = "neeyoNio8UGhidoo"
    WTF_CSRF_SECRET_KEY = "toomichohmiwai0J"


# BaseConfigクラスを継承してLocalConfigクラスを作成する
class LocalConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://{user}:{passwd}@{host}:{port}/{dbname}?charset=utf8'.format(**{
        'user': os.getenv('MYSQL_USER'),
        'passwd': os.getenv('MYSQL_PASSWORD'),
        'host': 'localhost',
        'port': 3306,
        'dbname': os.getenv('MYSQL_DATABASE')
    })
    SQLALCHEMY_TRACK_MODIFICATIONS = False,
    SQLALCHEMY_ECHO = True,


# BaseConfigクラスを継承してTestingConfigクラスを作成する
class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://{user}:{passwd}@{host}:{port}/{dbname}?charset=utf8'.format(**{
        'user': os.getenv('MYSQL_USER'),
        'passwd': os.getenv('MYSQL_PASSWORD'),
        'host': 'localhost',
        'port': 3306,
        'dbname': os.getenv('MYSQL_DATABASE')
    })
    SQLALCHEMY_TRACK_MODIFICATIONS = False,
    WTF_CSRF_ENABLED = False


# Config辞書にマッピングする
config = {
    "testing": TestingConfig,
    "local": LocalConfig,
}
