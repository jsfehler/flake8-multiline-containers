import os

from flake8.api import legacy as flake8

import pytest


@pytest.fixture
def dict_file_path():
    return 'tests/dummy/nested_dict_examples.py'


@pytest.fixture
def list_file_path():
    return 'tests/dummy/nested_list_examples.py'


@pytest.fixture
def set_file_path():
    return 'tests/dummy/nested_set_examples.py'


def test_js101_dict(dict_file_path):
    style_guide = flake8.get_style_guide(
        select=['JS101'],
    )

    p = os.path.abspath(dict_file_path)
    r = style_guide.check_files([p])

    assert 2 == r.total_errors


def test_js102_dict(dict_file_path):
    style_guide = flake8.get_style_guide(
        select=['JS102'],
    )

    p = os.path.abspath(dict_file_path)
    r = style_guide.check_files([p])

    assert 2 == r.total_errors


def test_js101_list(list_file_path):
    style_guide = flake8.get_style_guide(
        select=['JS101'],
    )

    p = os.path.abspath(list_file_path)
    r = style_guide.check_files([p])

    assert 3 == r.total_errors


def test_js102_list(list_file_path):
    style_guide = flake8.get_style_guide(
        select=['JS102'],
    )

    p = os.path.abspath(list_file_path)
    r = style_guide.check_files([p])

    assert 2 == r.total_errors


def test_js101_set(set_file_path):
    style_guide = flake8.get_style_guide(
        select=['JS101'],
    )

    p = os.path.abspath(set_file_path)
    r = style_guide.check_files([p])

    assert 1 == r.total_errors


def test_js102_set(set_file_path):
    style_guide = flake8.get_style_guide(
        select=['JS102'],
    )

    p = os.path.abspath(set_file_path)
    r = style_guide.check_files([p])

    assert 2 == r.total_errors
