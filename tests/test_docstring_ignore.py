import os

from flake8.api import legacy as flake8

import pytest


@pytest.fixture
def docstring_file_path():
    return 'tests/dummy/docstrings.py'


def test_docstring_ignore(docstring_file_path):
    """Docstrings should be ignored.

    Code after a docstring should not be ignored.
    """
    style_guide = flake8.get_style_guide(
        select=['JS101'],
    )

    p = os.path.abspath(docstring_file_path)
    r = style_guide.check_files([p])

    assert 6 == r.total_errors
