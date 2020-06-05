# Right: Extra whitespace doesn't cause function to be registered as a tuple
bizbat ( "Hello",
         "World")

bizbat        ( "Hello",
         "World")

# Right
# Function call containing parens around a long string
func(
    (
        "long string such that we use parens"
    ),
)

# Right: Nested function call is ignored
bizbat(bazbin("""
"""))


# Right: Nested function call is ignored
bizbat(bazbin('a',
'b'))


# Right: Opens and closes on same line
foo = bizbat('hello', 'world')

# Right: Line break after parenthesis, closes on same column
foo = bizbat(
    'hello',
    'world',
)


# Right: Line break after parenthesis, closes on same column
foo = bizbat(
    'hello', 'world',
)


# Wrong: JS103
foo = bizbat('hello',
       'world',
)

# Wrong: JS103
foo = bizbat(
    'hello', 'world')


# Wrong: JS103, JS104
foo = bizbat('hello',
       'world')


# Wrong: JS103, JS104
foo = bizbat('hello',
       'world',
      )


# Right
# Function call with tuple inside
foo = bizbat(
    (
        'hello',
        'world',
    )
)


# Wrong: JS103
# Function call with tuple inside
foo = bizbat((
    'hello',
    'world',
)
)