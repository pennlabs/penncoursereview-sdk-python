import json
import urllib
import urllib2

from memoize import memoize


@memoize
def fetch(domain, *args, **kwargs):
    assert domain.endswith("/"), "BAD DOMAIN: %s" % domain
    path = "/".join(str(arg) for arg in args)
    query = urllib.urlencode(kwargs)
    uri = "".join((domain, path, "?", query))
    try:
        response = urllib2.build_opener().open(uri)
    except urllib2.HTTPError:
        raise ValueError("invalid uri: %s", uri)
    return json.loads(response.read())
