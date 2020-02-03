import logging
from flask import Blueprint, jsonify
from app.db import get_conn

short_url = Blueprint('short_url', __name__)
logger = logging.getLogger(__name__)


def record():
    logger.info('logged by logging module of functions')
    return True


@short_url.route('/')
def short_url_root():
    logger.info('in short url root')
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute('SELECT version()')

        version = cur.fetchone()[0]
        logger.info(version)

    return jsonify({'test': 'ok'})
