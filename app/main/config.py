import os
 

class SystemConfig:
    DEBUG = True
 
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://{user}:{passwd}@{host}:{port}/{dbname}?charset=utf8'.format(**{
        'user': os.getenv('MYSQL_USER'),
        'passwd': os.getenv('MYSQL_PASSWORD'),
        'host': 'mysqldb',
        'port': 3306,
        'dbname': os.getenv('MYSQL_DATABASE')
    })
 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


Config = SystemConfig
