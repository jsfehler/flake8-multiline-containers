import enum
import re

import attr


# Matches anything inside a string.
STRING_REGEX = re.compile(
    r'"([^"\\]*(\\.[^"\\]*)*)"|\'([^\'\\]*(\\.[^\'\\]*)*)\'',
)

# Matches anything that looks like a:
# function call, function definition, or class definition with inheritance
# Actual tuples should be ignored
FUNCTION_CALL_REGEX = r'\w+\s*[(]'

# Matches anything that looks like a conditional block
CONDITIONAL_BLOCK_REGEX = re.compile(
    r'if\s*[(]|elif\s*[(]|or\s*[(]*[(]|and\s*[(]|not\s*[(]')


class ErrorCodes(enum.Enum):
    JS101 = "Multi-line container not broken after opening character"
    JS102 = "Multi-line container does not close on same column as opening"


def _error(line_number: int, column: int, error_code: ErrorCodes) -> tuple:
    """Format error report such that it's usable by flake8's reporting."""
    return (line_number, column, f'{error_code.name} {error_code.value}', None)


def get_left_pad(line: str) -> int:
    """Get the amount of whitespace before the first character in a line."""
    return len(line) - len(line.lstrip(' '))


@attr.s(hash=False)
class MultilineContainers:
    """Ensure the consistency of multiline dict and list style."""

    name = 'flake8_multiline_containers'
    version = '0.0.11'

    tree = attr.ib(default=None)
    filename = attr.ib(default="(none)")
    lines = attr.ib(default=None)

    errors = attr.ib(factory=list)

    # The column where the last line that opened started.
    last_starts_at = attr.ib(factory=list)

    # The number of functions deep we currently are in.
    function_depth = attr.ib(default=0)

    inside_conditional_block = attr.ib(default=0)

    def _number_of_matches_in_line(
            self,
            open_character: str,
            close_character: str,
            line: str) -> tuple:
        """Scan line and check how many times each character appears.

        Characters inside strings are ignored.

        Arguments:
            open_character: Opening character for the container.
            close_character: Closing character for the container.
            line: The line to check.

        Returns:
            tuple

        """
        open_matches_in_string = 0
        close_matches_in_string = 0

        # Whole line is a comment, so ignore it
        if re.search(r'^\s*#', line):
            return 0, 0

        # Find comments and make sure they're ignored
        # Remove strings from temp_line
        temp_line = STRING_REGEX.sub('', line)

        # Find comments in temp_line, remove them from line
        last_line = temp_line
        for match in re.finditer(r'#.*', temp_line):
            i = match.group(0)
            if i is not None:
                last_line = last_line.replace(i, '')

        line = last_line

        # Find strings and make sure they're ignored
        for match in STRING_REGEX.finditer(line):
            i = match.group(0)
            if i is not None:
                open_matches_in_string += i.count(open_character)
                close_matches_in_string += i.count(close_character)

        open_times = line.count(open_character)
        close_times = line.count(close_character)

        # Any time the open or close character appear in a string, ignore them.
        open_times -= open_matches_in_string
        close_times -= close_matches_in_string

        return open_times, close_times

    def _check_opening(
        self,
        open_character: str,
        close_character: str,
        line_number: int,
        line: str,
        error_code: ErrorCodes,
    ):
        """Implementation for JS101.

        If open_character and close_character don't appear the same number of
        times on the line, then open_character should be last character in the
        line.

        Arguments:
            open_character: Opening character for the container.
            close_character: Closing character for the container.
            line_number: The number of the line. Reported back to flake8.
            line: The line to check.
            error_code: The error to report if the validation fails.

        """
        open_times, close_times = self._number_of_matches_in_line(
            open_character, close_character, line,
        )

        # Tuples, functions, and classes all use lunula brackets.
        # Ensure only tuples are caught by JS101.
        if open_character == '(':
            for _ in re.finditer(FUNCTION_CALL_REGEX, line):
                # When inside a function with multiline arguments,
                # ignore the opening bracket
                self.function_depth += 1

            # If detected a conditional block, ignore it
            if CONDITIONAL_BLOCK_REGEX.search(line):
                self.inside_conditional_block += 1

            if open_times != close_times:
                open_times -= self.inside_conditional_block
                open_times -= self.function_depth

        # Multiline container detected
        if open_times >= 1 and open_times != close_times:
            self.last_starts_at.extend(
                [get_left_pad(line)] * open_times,
            )

            # Multiple opening characters
            if open_times > 1:
                e = _error(line_number + 1, 0, error_code)
                self.errors.append(e)

            # One opening character, but content after it.
            else:
                # Last character on a line is newline (\n). Get second to last.
                last_index = len(line) - 2
                if line[last_index] != open_character:
                    e = _error(line_number + 1, last_index, error_code)
                    self.errors.append(e)

    def _get_closing_index(self, line: str, close_character: str) -> int:
        """Get the line index for a closing character.

        The last, second to last, or third to last character on the line should
        be the closing character. Depends if there was a comma and/or newline.

        Arguments:
            line: The line to check.
            close_character: Closing character for the container.

        Returns:
            int

        """
        slices = [-1, -2, -3]
        index = get_left_pad(line)

        for s in slices:
            if line[s] == close_character:
                index = len(line) + s
                break

        return index

    def _check_closing(
        self,
        open_character: str,
        close_character: str,
        line_number: int,
        line: str,
        error_code: ErrorCodes,
    ):
        """Implementation for JS102.

        If open_character and close_character are not on the same line,
        then close_character should be aligned to the opening line.

        Arguments:
            open_character: Opening character for the container.
            close_character: Closing character for the container.
            line_number: The number of the line. Reported back to flake8.
            line: The line to check.
            error_code: The error to report if the validation fails.

        """
        open_times, close_times = self._number_of_matches_in_line(
            open_character, close_character, line,
        )

        if close_times > 0 and self.inside_conditional_block:
            close_times -= 1
            self.inside_conditional_block -= 1

        # When inside a function call,
        # Then if a closing bracket is found and tuples are closed,
        # Assume it's the closing bracket for the call.
        if open_character == '(' and self.function_depth > 0:
            if close_times >= 1 and len(self.last_starts_at) == 0:
                close_times -= 1
                self.function_depth -= 1

        elif close_times > 0 and open_times == 0 and self.last_starts_at:
            index = self._get_closing_index(line, close_character)

            if index != self.last_starts_at[-1]:
                e = _error(line_number + 1, index, error_code)
                self.errors.append(e)

            # Remove the last start location
            self.last_starts_at.pop()

    def check_for_js101(self, line_number: int, line: str):
        """Validate JS101 for a single line.

        When a line opens a container
        And the container isn't closed on the same line
        Then the line should break after the opening brackets
        """
        self._check_opening('{', '}', line_number, line, ErrorCodes.JS101)
        self._check_opening('[', ']', line_number, line, ErrorCodes.JS101)
        self._check_opening('(', ')', line_number, line, ErrorCodes.JS101)

    def check_for_js102(self, line_number: int, line: str):
        """Validate JS102 for a single line.

        When a line closes a container
        And the container isn't closed on the opening line
        Then the closing character must be on the same column as the
        opening line
        """
        self._check_closing('{', '}', line_number, line, ErrorCodes.JS102)
        self._check_closing('[', ']', line_number, line, ErrorCodes.JS102)
        self._check_closing('(', ')', line_number, line, ErrorCodes.JS102)

    def docstring_status(self, line: str, quote: str, last_status: int) -> int:
        """Check if a line is part of a docstring.

        Arguments:
            line: The line to scan
            quote: The kind of quotation mark to check
            last_status: The state of the previous line scanned

        Returns:
            0 if outside a docstring
            1 if inside
            2 if exiting, next line should be outside

        """
        new_status = last_status
        if last_status == 2:
            new_status = 0

        strip = line.strip()

        # If a line starts with a triple quotation mark, it's either:
        if strip.startswith(quote):
            # A single line docstring
            if strip.endswith(quote) and len(strip) > 3:
                new_status = 2

            # Entering multiline docstring
            elif last_status != 1:
                new_status = 1

            # Exiting docstring where closing is on separate line.
            elif last_status == 1:
                new_status = 2

        # Exiting multiline docstring where closing is on same line as text.
        elif strip.endswith(quote) and last_status == 1:
            new_status = 2

        return new_status

    def run(self):
        """Entry point for the plugin."""
        single_quote_status = 0
        double_quote_status = 0

        for index, line in enumerate(self.lines):
            # Ensure docstrings are ignored
            single_quote_status = self.docstring_status(
                line, "'''", single_quote_status,
            )
            double_quote_status = self.docstring_status(
                line, '"""', double_quote_status,
            )

            if single_quote_status == 0 and double_quote_status == 0:
                self.check_for_js101(index, line)
                self.check_for_js102(index, line)

        for e in self.errors:
            yield e
