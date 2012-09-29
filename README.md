# pcr-python-sdk

A module for using the Penn Course Review (PCR) API.

# Installation

Install from PyPi using [pip](http://www.pip-installer.org/en/latest/), a
package manager for Python.

    $ pip install penncoursereview

Don't have pip installed? Try installing it, by running this from the command
line:

    $ curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python

Or, you can [download the source code
(ZIP)](https://github.com/twilio/twilio-python/zipball/master "twilio-python
source code") for `penncoursereview`, and then run:

    $ python setup.py install

You may need to run the above commands with `sudo`.

# Getting Started

Getting started has been made to be as simple as possible. Set up your application token, and then import `penncoursereview` into your project and your good to go.

## API Credentials

In order to fetch data, the `penncoursereview` client needs your PCR token. To help ensure that you never have to worry about committing your credentials and posting them somewhere public, the module will only check for `PCR_AUTH_TOKEN` inside of the current environment.

## Making Calls 

The `penncoursereview` client gives you six useful tools to interact with the PCR-API.

*   Review(cid, sid, rid)
*   Section(cid, sid)
*   Instructor(iid)
*   Course(cid)
*   CourseHistory(chid)
*   Department(did)

...where `cid` is the id of the Course you are looking for, `did` is the id of the Department you are looking for, etc, etc.

A full description of the parameters can be found in the source.

As expected, each of these will load the data from their corresponding resource page on the PCR-API server.

For example:

```python
>>> import penncoursereview
>>> cis110 = penncoursereview.CourseHistory("CIS-110")
>>> cis110.courses[0].description
u'How do you program computers to accomplish tasks? How do you break down a complex task into simpler ones? CIS 110 is a "Java lite" course that covers the fundamentals of object-oriented programming such as objects, classes, state, methods, loops, arrays, inheritance, and recursion using the Java programming language. \n\n'
```

Furthermore, each object is capable of loading more data as you need it. For example, in the call above, `cis110.courses[0]` is just a short blurb of data representing the basic of a course that looks something like the following:

```javascript
{
    aliases: [
    "CIS-110"
    ],
    id: 13019,
    name: "INTRO TO COMP PROG",
    path: "/courses/13019",
    primary_alias: "CIS-110",
    semester: "2007C"
},
```

But, once you ask it for the description, it automatically loads the rest of the resource at the path specified and supplies you the description just in time!

In this way, you can chain some rather long requests provided you know what will be loaded before the object loads.

## Learning More

To learn more about what data is available, visit the official [PennCourseReview docs](http://pennapps.com/console/docs.html).
