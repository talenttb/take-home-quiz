import redis
import os

r = redis.Redis(host=os.environ.get("REDIS_HOST"), port=os.environ.get(
    "REDIS_PORT"), db=0, decode_responses=True)


def set(key, value, ttl=None):

    if not r.set(key, value):
        return False
    if ttl:
        r.expire(key, ttl)
    return True


def get(key):
    return r.get(key)
