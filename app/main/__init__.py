from flask import Flask

from app.main.database import init_db, db
from app.main.models import Book


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    init_db(app)

    @app.route('/')
    def index():
        res = db.session.query(
            Book.title
        ).all()

        # Name-Districtの文字列のlistを作成
        name_district = ['-'.join(r) for r in res]
        return '< br>'.join(name_district)

    return app
