import os
import psycopg2


def get_conn():
    conn = psycopg2.connect(
        host=os.environ.get('POSTGRES_HOST'),
        port=os.environ.get('POSTGRES_PORT'),
        user=os.environ.get('POSTGRES_USER'),
        password=os.environ.get('POSTGRES_PASSWORD'),
        dbname='postgres')

    return conn
