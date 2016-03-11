"""
Convenience wrapper for the Penn Course Review (PCR) API.

Note, when using fetch be careful to use strings for 0-prefixed numbers.
"""
import os
import trees
from .api import fetch


DOMAIN = "http://api.penncoursereview.com/v1/"


def fetch_pcr(*args, **kwargs):
    """Wrapper for fetch to easily parse results from the PCR API."""
    # Load user's token from `PCR_AUTH_TOKEN`
    # Use public token as default if missing
    kwargs['token'] = os.getenv("PCR_AUTH_TOKEN", "public")
    return fetch(DOMAIN, *args, **kwargs)['result']


class PCRResource(trees.ObjectifiedDict):
    """Concrete Resource that fetches data from the PCR API as needed."""

    def __missing__(self, key):
        # PCR Resources are guaranteed to have a 'path' attribute
        # We can use that to update the object
        return fetch_pcr(*self.path.split("/"))


# Convenience classes

def Review(cid, sid, iid):
    """Instantiate a Review.
    *   cid - The id of the course
    *   sid - The id of the section
    *   iid - The id of the instructor

    >>> Review("24765", "001", "1356-MICHAEL-KEARNS").num_students
    88
    """
    return PCRResource(fetch_pcr("courses", cid,
                                 "sections", sid,
                                 "reviews", iid))


def Instructor(iid):
    """Instantiate an Instructor.
    *  iid - The id of the instructor

    >>> Instructor("1356-MICHAEL-KEARNS").first_name
    u'MICHAEL J.'
    """
    return PCRResource(fetch_pcr("instructors", iid))


def Section(cid, sid):
    """Instantiate a Section.
    *  cid - The id of the course
    *  sid - The id of the section

    >>> Section(2795, 401).name
    u'INTRO COGNITIVE SCIENCE'
    """
    return PCRResource(fetch_pcr("courses", cid, "sections", sid))


def Course(cid):
    """Instantiate a Course.
    *  id - The id of the course

    >>> Course(2795).name
    u'INTRO COGNITIVE SCIENCE'
    """
    return PCRResource(fetch_pcr("courses", cid))


def CourseHistory(chid):
    """Instantiate a CourseHistory.
    *  chid - The id of the coursehistory or its alias

    >>> CourseHistory(177).aliases[0]
    u'ASTR-150'
    >>> CourseHistory("ASTR-150").aliases[0]
    u'ASTR-150'
    """
    return PCRResource(fetch_pcr("coursehistories", chid))


def Department(did):
    """Instantiate a Department.
    *  did - The id of the Department

    >>> Department("ASTR").name
    u'ASTRONOMY'
    """
    return PCRResource(fetch_pcr("depts", did))
