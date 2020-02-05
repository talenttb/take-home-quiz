# from __future__ import absolute_import, unicode_literals
from celery.result import AsyncResult
import os
from celery import Celery
import settings
from app.model import req_log as req_log_model

redis_conn = f'redis://{os.environ.get("REDIS_HOST")}:{os.environ.get("REDIS_PORT")}/0'
print(redis_conn)
app = Celery('tasks', broker=redis_conn, backend=redis_conn)

res = AsyncResult('8ad49791-faf3-4259-9b46-467ced261159', app=app)
print(res.state)
print(res.get())
# res.get()
