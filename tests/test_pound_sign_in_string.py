import os

from flake8.api import legacy as flake8

import pytest


@pytest.fixture
def pound_file_path(dummy_file_path):
    return f'{dummy_file_path}/mixed.py'


def test_js101_pound(pound_file_path):
    """Pound signs in strings shouldn't be considered the start of comments."""
    style_guide = flake8.get_style_guide(
        select=['JS101'],
    )

    p = os.path.abspath(pound_file_path)
    r = style_guide.check_files([p])

    assert 0 == r.total_errors


def test_js102_pound(pound_file_path):
    """Pound signs in strings shouldn't be considered the start of comments."""
    style_guide = flake8.get_style_guide(
        select=['JS102'],
    )

    p = os.path.abspath(pound_file_path)
    r = style_guide.check_files([p])

    assert 0 == r.total_errors
