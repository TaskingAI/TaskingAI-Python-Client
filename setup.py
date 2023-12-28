# coding: utf-8

"""
    TaskingAI

    OpenAPI spec version: 0.1.0
"""

from setuptools import setup, find_packages  # noqa: H301
import taskingai

NAME = "taskingai"
VERSION = taskingai.__version__
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "certifi>=14.05.14",
    "six>=1.10",
    "python_dateutil>=2.5.3",
    "setuptools>=21.0.0",
    "httpx>=0.23.0",
    "pydantic>=2.5.0",
]

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
