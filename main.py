from flask import Flask
from flask_restx import Api
from config import Config
from setup_db import db
from views.movie.movie_view import movies_ns
from views.genre.genre_view import genre_ns
from views.director.director_view import director_ns


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movies_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    create_data(app, db)


def create_data(app, db):
    with app.app_context():
        db.create_all()


app = create_app(Config())
app.debug = True

if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)
