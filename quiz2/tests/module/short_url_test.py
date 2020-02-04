import re

from app.service import short_url


def test_rdm_base_str():
    s = short_url.gen_rdm_base_str()

    assert re.match(r"\w+", s[:2])
    assert re.search(r"[A-Za-z0-9]+", s)
