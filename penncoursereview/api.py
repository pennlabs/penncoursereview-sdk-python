import abc
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


class Resource(object):
    """Abstract base class wrapper for a dict to give it an object interface.

    >>> d = {'foo': 1, 'bar': {'a': 3, 'b': 4}}
    >>> MyResource = type('MyResource', (Resource,), {'_load': lambda: 0})
    >>> o = MyResource(d)
    >>> o
    {foo : 1, bar : {a : 3, b : 4}}
    >>> o.foo
    1
    >>> o["foo"]
    1
    >>> o.bar.a
    3

    Heavily inspired by: http://stackoverflow.com/a/6573827/577199
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self, d):
        self._update(d)

    @abc.abstractmethod
    def _load(self):
        """Populate the object with additional data.
        This should retrieve the relevant data needed to respond to a valid
        getattr and then call _update."""
        pass

    def _update(self, data):
        """Update the object with new data."""
        for k, v in data.iteritems():
            new_value = v
            if isinstance(v, dict):
                new_value = type(self)(v)
            elif isinstance(v, list):
                new_value = [(type(self)(e) if isinstance(e, dict) else e)
                             for e in v]
            setattr(self, k, new_value)

    def __getattr__(self, val):
        """Try to get an attribute. On failure, load the object in full
        and try again."""
        try:
            return self.__dict__[val]
        except KeyError:
            self._load()
            return self.__dict__[val]

    def __getitem__(self, val):
        return self.__dict__[val]

    def __repr__(self):
        """Make the resource appear like a dict."""
        return '{%s}' % str(', '.join('%s : %s' % (k, repr(v)) for
            (k, v) in self.__dict__.iteritems()))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
