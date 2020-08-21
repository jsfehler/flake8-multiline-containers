import os

from flake8.api import legacy as flake8

import pytest


@pytest.fixture
def multiple_opening_file_path(dummy_file_path):
    return f'{dummy_file_path}/multiple_opening.py'


def test_js101_multiple_opening(multiple_opening_file_path):
    style_guide = flake8.get_style_guide(
        select=['JS101'],
    )

    p = os.path.abspath(multiple_opening_file_path)
    r = style_guide.check_files([p])

    assert 2 == r.total_errors


def test_js102_multiple_opening(multiple_opening_file_path):
    style_guide = flake8.get_style_guide(
        select=['JS102'],
    )

    p = os.path.abspath(multiple_opening_file_path)
    r = style_guide.check_files([p])

    assert 1 == r.total_errors
