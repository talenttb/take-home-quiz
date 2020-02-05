# from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
import settings
from app.model import req_log as req_log_model

redis_conn = f'redis://{os.environ.get("REDIS_HOST")}:{os.environ.get("REDIS_PORT")}/0'
print(redis_conn)
app = Celery('tasks', broker=redis_conn, backend=redis_conn)

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)


@app.task
def collect_logs_task(short_url, req_id, data):
    req_log_model.save_req_logs(short_url, req_id, data)


if __name__ == '__main__':
    app.start()
