import os

from flake8.api import legacy as flake8

import pytest


@pytest.fixture
def raw_strings_file_path():
    return 'tests/dummy/raw_strings.py'


def test_js101_raw_strings(raw_strings_file_path):
    """Ensure raw strings don't mess up the string finding regex."""
    style_guide = flake8.get_style_guide(
        select=['JS101'],
    )

    p = os.path.abspath(raw_strings_file_path)
    r = style_guide.check_files([p])

    assert 0 == r.total_errors


def test_js102_raw_strings(raw_strings_file_path):
    """Ensure raw strings don't mess up the string finding regex."""
    style_guide = flake8.get_style_guide(
        select=['JS102'],
    )

    p = os.path.abspath(raw_strings_file_path)
    r = style_guide.check_files([p])

    assert 0 == r.total_errors
