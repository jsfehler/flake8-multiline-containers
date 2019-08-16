===========================
flake8-multiline-containers
===========================

.. image:: https://img.shields.io/pypi/v/flake8-multiline-containers.svg
    :target: https://pypi.org/project/flake8-multiline-containers
    :alt: PyPI

.. image:: https://img.shields.io/pypi/pyversions/flake8-multiline-containers.svg
    :alt: PyPI - Python Version
    :target: https://github.com/jsfehler/flake8-multiline-containers

.. image:: https://travis-ci.org/jsfehler/flake8-multiline-containers.svg?branch=master
    :target: https://travis-ci.org/jsfehler/flake8-multiline-containers

A `Flake8 <https://flake8.readthedocs.io/en/latest/index.html>`_ plugin to ensure a consistent format for multiline containers.

Installation
------------

Install from ``pip`` with:

.. code-block:: sh

     pip install flake8-multiline-containers

Rules
-----

===== ====
Code  Rule
===== ====
JS101 Multi-line container not broken after opening character
JS102 Multi-line container does not close on same column as opening
===== ====

Examples
--------

.. code-block:: python

  # Right: Opens and closes on same line
  foo = {'a': 'hello', 'b': 'world'}


  # Right: Line break after parenthesis, closes on same column as opening
  foo = {
      'a': 'hello',
      'b': 'world',
  }

  # Right: Line break after parenthesis, closes on same column as opening
  foo = [
      'hello', 'world',
  ]


  # Wrong: JS101
  foo = {'a': 'hello',
         'b': 'world',
  }


  # Wrong: JS101, JS102
  foo = {'a': 'hello',
         'b': 'world'}


  # Wrong: JS101, JS102
  foo = {'hello',
         'world'
        }
