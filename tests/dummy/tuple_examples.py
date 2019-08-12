# Right: Opens and closes on same line
foo = ('hello', 'world')

# Right: Line break after parenthesis, closes on same column
foo = (
    'hello',
    'world',
)


# Right: Line break after parenthesis, closes on same column
foo = (
    'hello', 'world',
)


# Wrong: JS101
foo = ('hello',
       'world',
)

# Wrong: JS102
foo = (
    'hello', 'world')


# Wrong: JS101, JS102
foo = ('hello',
       'world')


# Wrong: JS101, JS102
foo = ('hello',
       'world',
      )
