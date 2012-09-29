import nose

from api import *
from models import *


def test_PCRStruct():
    d = Department("MKSE")
    print d
    print type(d.reviews)
    print d.path
    print d.reviews.values
    return True
