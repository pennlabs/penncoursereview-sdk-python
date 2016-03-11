import requests

from .memoize import memoize


@memoize
def fetch(domain, *args, **kwargs):
    assert domain.endswith("/"), "BAD DOMAIN: %s" % domain
    path = "/".join(str(arg) for arg in args)
    uri = domain + path
    r = requests.get(uri, params=kwargs)
    return r.json()
