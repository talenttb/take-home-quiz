import os
import psycopg2


def get_conn():

    # url = urlparse.urlparse(os.environ.get('DATABASE_URL'))
    # db = "dbname=%s user=%s password=%s host=%s " % (
    #     url.path[1:], url.username, url.password, url.hostname)
    # schema = "schema.sql"
    # conn = psycopg2.connect(db)
    # cur = conn.cursor()
    # - *dbname*: the database name
    # - *database*: the database name(only as keyword argument)
    # - *user*: user name used to authenticate
    # - *password*: password used to authenticate
    # - *host*: database host address(defaults to UNIX socket if not provided)
    # - *port*: connection port number(defaults to 5432 if not provided)

    conn = psycopg2.connect(
        host=os.environ.get('POSTGRES_HOST'),
        port=os.environ.get('POSTGRES_PORT'),
        user=os.environ.get('POSTGRES_USER'),
        password=os.environ.get('POSTGRES_PASSWORD'))

    return conn
