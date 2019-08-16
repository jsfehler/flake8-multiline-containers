import os

from flake8.api import legacy as flake8

import pytest


@pytest.fixture
def function_calls_file_path():
    return 'tests/dummy/function_call_examples.py'


def test_js101_function_calls_ignored(function_calls_file_path):
    """Function calls should not trigger JS101."""
    style_guide = flake8.get_style_guide(
        select=['JS101'],
    )

    p = os.path.abspath(function_calls_file_path)
    r = style_guide.check_files([p])

    assert 0 == r.total_errors


def test_js102_function_calls_ignored(function_calls_file_path):
    """Function calls should not trigger JS102."""
    style_guide = flake8.get_style_guide(
        select=['JS102'],
    )

    p = os.path.abspath(function_calls_file_path)
    r = style_guide.check_files([p])

    assert 0 == r.total_errors
