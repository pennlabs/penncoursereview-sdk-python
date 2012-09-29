import nose

from penncoursereview import *


def test_PCRStruct():
    d = Department("MKSE")
    print d
    print type(d.reviews)
    print d.path
    print d.reviews.values
    return True
