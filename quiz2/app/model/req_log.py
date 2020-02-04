from app.model.db import get_conn
from psycopg2 import sql, DatabaseError, IntegrityError
import logging
logger = logging.getLogger(__name__)


def save_req_logs(data):
    with get_conn() as conn:
        with conn.cursor() as cur:
            insert_sql = """
            INSERT INTO req_logs
            (identity, data, created_at)
            VALUES(%s, %s, %s)
            """
            try:
                cur.execute(
                    sql.SQL(insert_sql),
                    [short_url, ori_url, created_at, expired_at]
                )
            except IntegrityError as error:
                if 'duplicate key' in str(error):
                    logger.info('handle duplicate error')
                logger.error(error)
                conn.rollback()
                return False
            else:
                conn.commit()
                return True
