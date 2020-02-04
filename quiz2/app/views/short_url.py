from app.cache import redis_srv
import logging
from flask import Blueprint, jsonify
from app.service import short_url as short_url_service
from flask import request
import time
import pendulum
from app.model import short_url as short_url_model
short_url = Blueprint('short_url', __name__)
logger = logging.getLogger(__name__)


@short_url.route('/')
def short_url_root():
    logger.info('in short url root')
    # with get_conn() as conn:
    #     cur = conn.cursor()
    #     cur.execute('SELECT version()')
    #     cursor.execute(
    #         "INSERT INTO url_mapping (c1, c2, c3) VALUES(%s, %s, %s)", (v1, v2, v3))
    #     version = cur.fetchone()[0]
    #     logger.info(version)

    return jsonify({'test': 'ok'})


@short_url.route('/urls/<u>')
def get_short_url(u):
    ori_url = redis_srv.get(u)
    logger.info(ori_url)
    return jsonify({'r': ori_url})


@short_url.route('/urls', methods=['POST'])
def create_short_url():
    logger.info(request.json['original'])
    original_url = request.json['original']
    now = pendulum.now()
    for i in range(2):
        short_url = short_url_service.gen_rdm_base_str()

        if short_url_model.save_url_mapping(
                short_url, original_url, now, now.add(days=150)):

            redis_srv.set(short_url, original_url, 150*24*60*60)
            return jsonify({'original_url': original_url,
                            'short_url': short_url,
                            'expired_at': now.add(days=150)
                            })
            break
        time.sleep(3)
    else:
        return 'service is busy.', 400
