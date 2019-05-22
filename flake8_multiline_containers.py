import enum

import attr


class ErrorCodes(enum.Enum):
    JS101 = "Multi-line container not broken after opening character"
    JS102 = "Multi-line container does not close on same column as opening"


def _error(line_number: int, column: int, error_code: ErrorCodes) -> tuple:
    """Format error report such that it's usable by flake8's reporting.
    """
    return (line_number, column, f'{error_code.name} {error_code.value}', None)


def get_left_pad(line: str) -> int:
    """Get the amount of whitespace before the first character in a line."""
    return len(line) - len(line.lstrip(' '))


@attr.s(hash=False)
class MultilineContainers:
    """Ensure the consistency of multiline dict and list style.
    """

    name = 'flake8_multiline_containers'
    version = '0.0.1'

    tree = attr.ib(default=None)
    filename = attr.ib(default="(none)")
    lines = attr.ib(default=None)

    errors = attr.ib(factory=list)

    # The column where the last line that opened started
    last_starts_at = attr.ib(factory=list)

    def _check_opening(
        self,
        open_character: str,
        close_character: str,
        line_number: int,
        line: str,
        error_code: ErrorCodes,
    ):
        """Implementation for JS101.

        If open_character and close_character are not on the same line,
        then open_character should be last character in line.

        Arguments:
            open_character: Opening character for the container.
            close_character: Closing character for the container.
            line_number: The number of the line. Reported back to flake8.
            line: The line to check.
            error_code: The error to report if the validation fails.

        """
        line_opens = True if open_character in line else False
        line_closes = True if close_character in line else False

        if line_opens and not line_closes:
            self.last_starts_at.append(get_left_pad(line))

            # Last character on a line is a newline (\n). Get second to last.
            last_index = len(line) - 2
            if line[last_index] != open_character:
                e = _error(line_number + 1, last_index, error_code)
                self.errors.append(e)

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
        line_opens = True if open_character in line else False
        line_closes = True if close_character in line else False

        if line_closes and not line_opens:
            for index, i in enumerate(line):
                if i == close_character:
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

    def check_for_js102(self, line_number: int, line: str):
        """Validate JS102 for a single line.

        When a line closes a container
        And the container isn't closed on the opening line
        Then the closing character must be on the same column as the
        opening line
        """
        self._check_closing('{', '}', line_number, line, ErrorCodes.JS102)
        self._check_closing('[', ']', line_number, line, ErrorCodes.JS102)

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
