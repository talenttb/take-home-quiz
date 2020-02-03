import importlib
import settings
import logging
import logging.handlers
import os
from flask import Flask


def create_app(config_name):
    app = Flask(__name__)
    # app.config.from_object(config[config_name])

    register_logging(app)
    from app.views.short_url import short_url
    app.register_blueprint(short_url)
    app.logger.info(f'Project version: {os.getenv("PRJ_VERSION")}')
    return app


def register_logging(app):
    app.logger.name = 'app'

    rootLogger = logging.getLogger(__name__)
    rootLogger.setLevel(logging.DEBUG)


if __name__ == '__main__':
    app.run()
