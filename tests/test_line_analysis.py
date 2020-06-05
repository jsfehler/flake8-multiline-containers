from typing import List, Tuple

from flake8_multiline_containers import analyse_line

import pytest


@pytest.mark.parametrize('line,expected', [
    ("foo", []),
    ("'[]'", []),
    ("foo()", [('(', 3), (')', 4)]),
    ("()", [('(', 0), (')', 1)]),
    ("({)}", [('(', 0), ('{', 1), (')', 2), ('}', 3)]),
    ("(('abc', 'def')", [('(', 0), ('(', 1), (')', 14)]),
    ("('}')", [('(', 0), (')', 4)]),
    ("('\"', \"'\")", [('(', 0), (')', 9)]),
    ("(#)", [('(', 0)]),
])
def test_line_analysis(line: str, expected: List[Tuple[str, int]]) -> None:
    actual = analyse_line('{([])}', line)
    assert actual == expected
