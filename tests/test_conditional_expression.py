import os

from flake8.api import legacy as flake8

import pytest


@pytest.fixture
def conditional_expression_file_path(dummy_file_path):
    return f'{dummy_file_path}/conditional_expression.py'


@pytest.mark.doit1
def test_js101_conditional_block(conditional_expression_file_path):
    """Conditional blocks should not trigger JS101."""
    style_guide = flake8.get_style_guide(
        select=['JS101'],
    )

    p = os.path.abspath(conditional_expression_file_path)
    r = style_guide.check_files([p])

    assert 0 == r.total_errors


def test_js102_conditional_block(conditional_expression_file_path):
    """Conditional blocks should not trigger JS102."""
    style_guide = flake8.get_style_guide(
        select=['JS102'],
    )

    p = os.path.abspath(conditional_expression_file_path)
    r = style_guide.check_files([p])

    assert 0 == r.total_errors
