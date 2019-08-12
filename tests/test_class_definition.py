import os

from flake8.api import legacy as flake8

import pytest


@pytest.fixture
def class_def_file_path():
    return 'tests/dummy/class_def_examples.py'


def test_js101_function_def_ignored(class_def_file_path):
    """Function calls should not trigger JS101."""
    style_guide = flake8.get_style_guide(
        select=['JS101'],
    )

    p = os.path.abspath(class_def_file_path)
    r = style_guide.check_files([p])

    assert 0 == r.total_errors


def test_js102_function_def_ignored(class_def_file_path):
    """Function calls should not trigger JS102."""
    style_guide = flake8.get_style_guide(
        select=['JS102'],
    )

    p = os.path.abspath(class_def_file_path)
    r = style_guide.check_files([p])

    assert 0 == r.total_errors
