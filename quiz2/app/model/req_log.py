from app.model.db import get_conn
from psycopg2 import sql, DatabaseError, IntegrityError
import pendulum
import json
import logging
logger = logging.getLogger(__name__)


def save_req_logs(short_url, req_id, data):
    with get_conn() as conn:
        with conn.cursor() as cur:
            insert_sql = """
            INSERT INTO req_logs
            (req_id,short_url, user_data, created_at)
            VALUES(%s,%s, %s, %s)
            """
            try:
                cur.execute(
                    sql.SQL(insert_sql),
                    [req_id, short_url, json.dumps(data), pendulum.now()]
                )
            except DatabaseError as error:
                logger.error(error)
                conn.rollback()
                return False
            else:
                conn.commit()
                return True
