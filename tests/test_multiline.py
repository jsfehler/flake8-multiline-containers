import os

from flake8.api import legacy as flake8

import pytest


@pytest.fixture
def dict_file_path(dummy_file_path):
    return f'{dummy_file_path}/dict/dict.py'


@pytest.fixture
def list_file_path(dummy_file_path):
    return f'{dummy_file_path}/list/list.py'


@pytest.fixture
def set_file_path(dummy_file_path):
    return f'{dummy_file_path}/set/set.py'


@pytest.fixture
def tuple_file_path(dummy_file_path):
    return f'{dummy_file_path}/tuple/tuple.py'


def test_js101_dict(dict_file_path):
    style_guide = flake8.get_style_guide(
        select=['JS101'],
    )

    p = os.path.abspath(dict_file_path)
    r = style_guide.check_files([p])

    assert 4 == r.total_errors


def test_js102_dict(dict_file_path):
    style_guide = flake8.get_style_guide(
        select=['JS102'],
    )

    p = os.path.abspath(dict_file_path)
    r = style_guide.check_files([p])

    assert 4 == r.total_errors


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

    assert 3 == r.total_errors


def test_js101_set(set_file_path):
    style_guide = flake8.get_style_guide(
        select=['JS101'],
    )

    p = os.path.abspath(set_file_path)
    r = style_guide.check_files([p])

    assert 3 == r.total_errors


def test_js102_set(set_file_path):
    style_guide = flake8.get_style_guide(
        select=['JS102'],
    )

    p = os.path.abspath(set_file_path)
    r = style_guide.check_files([p])

    assert 3 == r.total_errors


def test_js101_tuple(tuple_file_path):
    style_guide = flake8.get_style_guide(
        select=['JS101'],
    )

    p = os.path.abspath(tuple_file_path)
    r = style_guide.check_files([p])

    assert 3 == r.total_errors


def test_js102_tuple(tuple_file_path):
    style_guide = flake8.get_style_guide(
        select=['JS102'],
    )

    p = os.path.abspath(tuple_file_path)
    r = style_guide.check_files([p])

    assert 3 == r.total_errors
