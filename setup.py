from setuptools import setup, find_packages
import taskingai

NAME = "taskingai"
VERSION = taskingai.__version__

REQUIRES = [
    "certifi>=14.05.14",
    "six>=1.10",
    "python_dateutil>=2.5.3",
    "setuptools>=21.0.0",
    "httpx>=0.23.0",
    "pydantic>=2.5.0",
]

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name=NAME,
    version=VERSION,
    description="TaskingAI",
    author_email="support@tasking.ai",
    url="https://www.tasking.ai",
    keywords=["TaskingAI", "LLM", "AI"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "test.*", "examples", "examples.*"]),
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown",
)
