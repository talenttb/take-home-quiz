import importlib
import settings
import logging
from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from app import database, view_model, log, api_doc
# from flask_marshmallow import Marshmallow


def create_app():
    app = Flask(__name__)

    with app.app_context():
        # init_db()
        from app.views.short_url import short_url
        app.register_blueprint(short_url)

    return app


# def create_app():
#     app = Flask(__name__)
#     # app.config.from_envvar(config)
#     # app.config.from_object('app.config.dev.Config')
#     # print(app.config)
#     # app.config.from_pyfile(f'config/dev.py')

#     # initialize_extensions(app)
#     # app = register_blueprints(app)
#     from app.views.short_url import short_url
#     app.register_blueprint(short_url)

#     return app


# def initialize_extensions(app):
#     # Since the application instance is now created, pass it to each Flask
#     # extension instance to bind it to the Flask application instance (app)
#     # db = SQLAlchemy(app)
#     database.init_app(app)
#     # ma = Marshmallow(app)
#     view_model.init_app(app)
#     log.init_app(app)
#     # api_doc.init_app(app)
#     # return app


def register_blueprints(app):
    blueprints = [
        'app.views.short_url',
    ]

    for bp_name in blueprints:
        bp = importlib.import_module(bp_name)
        app.register_blueprint(bp.bp())

    return app


if __name__ == '__main__':
    app.run()
