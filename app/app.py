from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

from app.config import config

# SQLAlchemyをインスタンス化する
db = SQLAlchemy()

csrf = CSRFProtect()


# configのキーを渡す
def create_app(config_key):
    app = Flask(__name__)
    print(app)

    # config_keyにマッチする環境のコンフィグクラスを読み込む
    app.config.from_object(config[config_key])

    csrf.init_app(app)

    # SQLAlchemyとアプリを連携する
    db.init_app(app)

    # Migrateとアプリを連携する
    Migrate(app, db)

    # crudパッケージからviewsをimportする
    from app.booknos_main import views

    # register_blueprintを使いviewsをアプリへ登録する
    app.register_blueprint(views.booknos_main, url_prefix="/")

    return app


if __name__ == "__main__":
    create_app().run(debug=True, host='0.0.0.0')
