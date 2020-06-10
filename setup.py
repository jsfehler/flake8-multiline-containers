import os

import setuptools


def read(filename):
    path = os.path.join(os.path.dirname(__file__), filename)
    with open(path, 'r') as f:
        return f.read()


setuptools.setup(
    name="flake8-multiline-containers",
    license="MIT",
    version="0.0.11",
    description="Ensure a consistent format for multiline containers.",
    long_description=read('README.rst'),
    author="Joshua Fehler",
    author_email="jsfehler@gmail.com",
    url="https://github.com/jsfehler/flake8-multiline-containers",
    py_modules=["flake8_multiline_containers"],
    install_requires=[
        "flake8 >= 3.7.9",
        "attrs >= 19.3.0",
    ],
    entry_points={
        'flake8.extension': [
            'JS = flake8_multiline_containers:MultilineContainers',
        ],
    },
    classifiers=[
        "Framework :: Flake8",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
    ],
)
