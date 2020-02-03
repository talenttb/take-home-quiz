# import json
# import yaml
# from app import log
from flask import Blueprint
from flask import jsonify
# , current_app as app
# from app.database import db
# from app.view_model import ma
# from flask_apispec import use_kwargs, marshal_with

short_url = Blueprint('short_url', __name__)


@short_url.route('/')
def short_url_root():
    return jsonify({'test': 'ok'})
