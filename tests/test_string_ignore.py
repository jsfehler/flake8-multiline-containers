import os

from flake8.api import legacy as flake8

import pytest


@pytest.fixture
def string_file_path():
    return 'tests/dummy/string_examples.py'


def test_js101_string_ignore(string_file_path):
    """When opening and closing characters are in a string
    Then the linter should not detect them.
    """
    style_guide = flake8.get_style_guide(
        select=['JS101'],
    )

    p = os.path.abspath(string_file_path)
    r = style_guide.check_files([p])

    assert 0 == r.total_errors


def test_js102_string_ignore(string_file_path):
    """When opening and closing characters are in a string
    Then the linter should not detect them.
    """
    style_guide = flake8.get_style_guide(
        select=['JS102'],
    )

    p = os.path.abspath(string_file_path)
    r = style_guide.check_files([p])

    assert 0 == r.total_errors
