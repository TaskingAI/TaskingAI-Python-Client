# coding: utf-8

"""
    TaskingAI

    OpenAPI spec version: 0.1.0
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "client"
VERSION = "0.0.2"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="TaskingAI",
    author_email="support@tasking.ai",
    url="http://www.tasking.ai",
    keywords=["TaskingAI", "LLM", "AI"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    No description provided 
    """
)
