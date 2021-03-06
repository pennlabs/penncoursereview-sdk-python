"""
Convenience wrapper for the Penn Course Review (PCR) API.

Note, when using fetch be careful to use strings for 0-prefixed numbers.
"""
import os

from .api import fetch, Resource


DOMAIN = "http://api.penncoursereview.com/v1/"


def fetch_pcr(*args, **kwargs):
    """Wrapper for fetch to automatically parse results from the PCR API."""
    # Load user's token from `PCR_AUTH_TOKEN`, use public token as default if missing
    kwargs['token'] = os.getenv("PCR_AUTH_TOKEN", "public")
    return fetch(DOMAIN, *args, **kwargs)['result']


class PCRResource(Resource):
    """Concrete Resource that fetches data from the PCR API as needed."""

    def _load(self):
        # PCR Resources are guaranteed to have a 'path' attribute
        # We can use that to update the object
        self._update(fetch_pcr(*self.path.split("/")))


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


def ReviewHistory(chid):
    """Instantiate a CourseHistory of reviews.
    * chid - The id of the coursehistory or its alias

    >>> ReviewHistory("CIS-160")['values'][0].num_reviewers
    84
    """
    return PCRResource(fetch_pcr("coursehistories", chid, "reviews"))


def Department(did):
    """Instantiate a Department.
    *  did - The id of the Department

    >>> Department("ASTR").name
    u'ASTRONOMY'
    """
    return PCRResource(fetch_pcr("depts", did))
