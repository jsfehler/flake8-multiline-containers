from flake8_multiline_containers import ErrorCodes


def test_check_opening_contains_error(linter):
    line = "foo={a\n"

    curly_matches = linter._number_of_matches_in_line(
        '{', '}', line,
    )

    linter._check_opening('{', '}', curly_matches, 0, line, ErrorCodes.JS101)
    assert 1 == len(linter.errors)


def test_check_opening_no_error(linter):
    line = "foo={\n"

    curly_matches = linter._number_of_matches_in_line(
        '{', '}', line,
    )

    linter._check_opening('{', '}', curly_matches, 0, line, ErrorCodes.JS101)
    assert 0 == len(linter.errors)
