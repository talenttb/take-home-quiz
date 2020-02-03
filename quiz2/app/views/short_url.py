# import json
# import yaml
# from app import log
import logging
from flask import Blueprint, jsonify

short_url = Blueprint('short_url', __name__)
logger = logging.getLogger(__name__)


def record():
    logger.info('logged by logging module of functions')
    return True


@short_url.route('/')
def short_url_root():
    logger.info('in short url root')
    return jsonify({'test': 'ok'})
