import os

from flake8.api import legacy as flake8

import pytest


@pytest.fixture
def eq_file_path(dummy_file_path):
    return f'{dummy_file_path}/equality.py'


def test_js101_eq(eq_file_path):
    style_guide = flake8.get_style_guide(
        select=['JS101'],
    )

    p = os.path.abspath(eq_file_path)
    r = style_guide.check_files([p])

    assert 0 == r.total_errors


def test_js102_eq(eq_file_path):
    style_guide = flake8.get_style_guide(
        select=['JS102'],
    )

    p = os.path.abspath(eq_file_path)
    r = style_guide.check_files([p])

    assert 0 == r.total_errors
