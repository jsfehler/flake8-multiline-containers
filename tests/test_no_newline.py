import os

from flake8.api import legacy as flake8

import pytest


@pytest.fixture
def no_newline_file_path(dummy_file_path):
    return f'{dummy_file_path}/no_newline.py'


def test_js101_no_newline(no_newline_file_path):
    """When a file has no blank line at EOF
    And a container ends correctly on the last line
    Then the linter should not detect an error.
    """
    style_guide = flake8.get_style_guide(
        select=['JS101'],
    )

    p = os.path.abspath(no_newline_file_path)
    r = style_guide.check_files([p])

    assert 0 == r.total_errors


def test_js102_no_newline(no_newline_file_path):
    """When a file has no blank line at EOF
    And a container ends correctly on the last line
    Then the linter should not detect an error.
    """
    style_guide = flake8.get_style_guide(
        select=['JS102'],
    )

    p = os.path.abspath(no_newline_file_path)
    r = style_guide.check_files([p])

    assert 0 == r.total_errors
