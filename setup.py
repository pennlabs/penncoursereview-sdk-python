from distutils.core import setup

from penncoursereview import __version__

# To install the penncoursereview library, open a Terminal shell, then run this
# file by typing:
#
# python setup.py install
#
# You need to have the setuptools module installed. Try reading the setuptools
# documentation: http://pypi.python.org/pypi/setuptools

setup(
    name="penncoursereview",
    version=__version__,
    author="Ceasar Bautista",
    author_email="cbautista2010@gmail.com",
    url="https://github.com/pennappslabs/penncoursereview-sdk-python",
    description="Penn Course Review API client",
    keywords=["penncoursereview", "penn", "upenn"],
    packages=['penncoursereview'],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        ],
    long_description="""\
    Python PennCourseReview Helper Library
    ----------------------------

    DESCRIPTION
    The PCR SDK simplifies the process of making calls to the PCR REST API.
    The PCR REST API lets you gather data about courses at the University of
    Pennnyslyvania. See website for more information.

     LICENSE The Python PennCourseReview Helper Library is distributed under
    the MIT License """)
