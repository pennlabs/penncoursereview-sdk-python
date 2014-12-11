import functools
import six
try:
    import cPickle as pickle
except:
    import pickle


def memoize(func):
    cache = {}

    @functools.wraps(func)
    def memoized(*args, **kwargs):
        hash_ = pickle.dumps((args, set(six.iteritems(kwargs))))
        try:
            return cache[hash_]
        except KeyError:
            try:
                cache[hash_] = func(*args, **kwargs)
            except Exception as e:
                raise e
            return cache[hash_]
    return memoized
