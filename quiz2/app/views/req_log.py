import os
from celery import Celery
import logging
from flask import Blueprint, jsonify
from flask import request
import time
import pendulum

from app.cache import redis_srv
from app.model import req_log as req_log_model
from app.celery import collect_logs_task

req_log = Blueprint('req_log', __name__)
logger = logging.getLogger(__name__)


@req_log.route('/logs/<short_url>/<req_id>', methods=['POST'])
def collect_logs(short_url, req_id):
    logger.info(request.json['data'])
    data = request.json['data']

    logger.info(collect_logs_task.delay(short_url, req_id, data))
    # req_log_model.save_req_logs(short_url, req_id, data)
    return jsonify({}), 200
