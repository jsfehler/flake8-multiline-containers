from flake8_multiline_containers import MultilineContainers

import pytest


@pytest.fixture
def linter():
    m = MultilineContainers()
    m.errors = []
    return m
