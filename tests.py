import penncoursereview as pcr
from penncoursereview.api import Resource
from nose.tools import assert_equal

MKERNS = "1356-MICHAEL-KEARNS"


class TestPennCourseReview:
    def test_review(self):
        assert_equal(pcr.Review("24765", "001", MKERNS).num_students, 88)

    def test_instructor(self):
        assert_equal(pcr.Instructor(MKERNS).first_name, 'MICHAEL J.')

    def test_section(self):
        assert_equal(pcr.Section(2795, 401).name, 'INTRO COGNITIVE SCIENCE')

    def test_course(self):
        assert_equal(pcr.Course(2795).name, 'INTRO COGNITIVE SCIENCE')

    def test_course_history(self):
        assert_equal(pcr.CourseHistory(177).aliases[0], 'ASTR-150')
        assert_equal(pcr.CourseHistory("ASTR-150").aliases[0], 'ASTR-150')

    def test_department(self):
        assert_equal(pcr.Department("ASTR").name, 'ASTRONOMY')


def test_resource():
    d = {'foo': 1, 'bar': {'a': 3, 'b': 4}}
    MyResource = type('MyResource', (Resource,), {'_load': lambda: 0})
    o = MyResource(d)
    assert_equal(o.foo, 1)
    assert_equal(o["foo"], 1)
    assert_equal(o.bar.a, 3)
