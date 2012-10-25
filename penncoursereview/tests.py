from penncoursereview import Department


def test_PCRStruct_known_key():
    d = Department("MKSE")
    assert d.reviews


def test_PCRStruct_load_key():
    d = Department("MKSE")
    print d
    print type(d.reviews)
    print d.path
    print d.reviews.values
    return True
