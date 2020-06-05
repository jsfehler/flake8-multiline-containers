from flake8_multiline_containers import ErrorCodes


def test_check_opening_contains_error(linter):
    linter._check_opening(
        '{',
        '}',
        0,
        "foo={a\n",
        [('{', 4)],
        ErrorCodes.JS101,
    )
    assert 1 == len(linter.errors)


def test_check_opening_no_error(linter):
    linter._check_opening('{', '}', 0, "foo={\n", [('{', 4)], ErrorCodes.JS101)
    assert 0 == len(linter.errors)
