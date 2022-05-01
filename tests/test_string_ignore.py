import os

from flake8.api import legacy as flake8

import pytest


@pytest.fixture
def string_file_path(dummy_file_path):
    return f'{dummy_file_path}/string/string.py'


@pytest.fixture
def string_brackets_file_path(dummy_file_path):
    return f'{dummy_file_path}/string/string_brackets.py'


@pytest.fixture
def multiline_string_file_path(dummy_file_path):
    return f'{dummy_file_path}/string/multiline.py'


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


def test_js101_string_brackets_ignore(string_brackets_file_path):
    """When opening and closing characters are in a string
    Then the linter should not detect them.
    """
    style_guide = flake8.get_style_guide(
        select=['JS101'],
    )

    p = os.path.abspath(string_brackets_file_path)
    r = style_guide.check_files([p])

    assert 0 == r.total_errors


def test_js102_string_brackets_ignore(string_brackets_file_path):
    """When opening and closing characters are in a string
    Then the linter should not detect them.
    """
    style_guide = flake8.get_style_guide(
        select=['JS102'],
    )

    p = os.path.abspath(string_brackets_file_path)
    r = style_guide.check_files([p])

    assert 1 == r.total_errors


def test_js101_multiline_string_ignore(multiline_string_file_path):
    """When opening and closing characters are in a string
    Then the linter should not detect them.
    """
    style_guide = flake8.get_style_guide(
        select=['JS101'],
    )

    p = os.path.abspath(multiline_string_file_path)
    r = style_guide.check_files([p])

    assert 0 == r.total_errors


def test_js102_multiline_string_ignore(multiline_string_file_path):
    """When opening and closing characters are in a string
    Then the linter should not detect them.
    """
    style_guide = flake8.get_style_guide(
        select=['JS102'],
    )

    p = os.path.abspath(multiline_string_file_path)
    r = style_guide.check_files([p])

    assert 0 == r.total_errors
