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

In order to fetch data, the `penncoursereview` library needs your PCR token. To help ensure that you never have to worry about committing your credentials and posting them somewhere public, the module will only check for `PCR_AUTH_TOKEN` inside of the current environment.

## Making Calls 

```python
>>> import penncoursereview
>>> cis110 = penncoursereview.CourseHistory("CIS-110")
>>> cis110.courses[0].description
u'How do you program computers to accomplish tasks? How do you break down a complex task into simpler ones? CIS 110 is a "Java lite" course that covers the fundamentals of object-oriented programming such as objects, classes, state, methods, loops, arrays, inheritance, and recursion using the Java programming language. \n\n'
```

To learn more, visit the official [PennCourseReview docs](http://pennapps.com/console/docs.html).
