# Right: Opens and closes on same line
foo = {'a': 'hello', 'b': 'world'}


# Right: Line break after parenthesis, closes on same column
foo = {
    'a': 'hello',
    'b': 'world',
}

# Right: Line break after parenthesis, closes on same column
foo = {
    'a': 'hello', 'b': 'world',
}


# Wrong: JS101
foo = {'a': 'hello',
       'b': 'world',
}


# Wrong: JS102
foo = {
    'a': 'hello', 'b': 'world'}


# Wrong: JS101, JS102
foo = {'a': 'hello',
       'b': 'world'}


# Wrong: JS101, JS102
foo = {'a': 'hello',
       'b': 'world',
      }


# Function call with dict inside

# Right
foo = bizbat({'a': 'Hello', 'b': 'World'}, True)

# Right
foo = bizbat(
    {'a': 'Hello', 'b': 'World'},
    True,
)

# Right
foo = bizbat(
    {
        'a': 'Hello',
        'b': 'World'
    },
    True,
)

# Wrong: JS101, JS102
foo = bizbat(
    {'a': 'Hello',
     'b': 'World'},
    True,
)