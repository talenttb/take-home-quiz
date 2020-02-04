import logging
from flask import Blueprint, jsonify
from flask import request
import time
import pendulum

from app.cache import redis_srv
from app.model import req_log as req_log_model

req_log = Blueprint('req_log', __name__)
logger = logging.getLogger(__name__)


@req_log.route('/logs/<identity>', methods=['POST'])
def collect_logs(identity):
    logger.info(request.json['data'])
    data = request.json['data']
    # TODO
    # should use async task
    req_log_model.save_req_logs(identity, data)
    return jsonify({}), 200
