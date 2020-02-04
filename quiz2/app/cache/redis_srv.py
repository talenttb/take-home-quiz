import redis
r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)


def set(key, value, ttl=None):

    if not r.set(key, value):
        return False
    if ttl:
        r.expire(key, ttl)
    return True


def get(key):
    return r.get(key)
