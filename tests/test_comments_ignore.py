import os

from flake8.api import legacy as flake8

import pytest


@pytest.fixture
def comments_file_path():
    return 'tests/dummy/comments.py'


def test_js101_comments_ignore(comments_file_path):
    """Comment lines should not trigger JS101."""
    style_guide = flake8.get_style_guide(
        select=['JS101'],
    )

    p = os.path.abspath(comments_file_path)
    r = style_guide.check_files([p])

    assert 0 == r.total_errors


def test_js102_comments_ignored(comments_file_path):
    """Comment lines should not trigger JS102."""
    style_guide = flake8.get_style_guide(
        select=['JS102'],
    )

    p = os.path.abspath(comments_file_path)
    r = style_guide.check_files([p])

    assert 0 == r.total_errors
