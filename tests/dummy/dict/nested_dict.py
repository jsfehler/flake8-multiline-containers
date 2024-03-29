# Right: Opens and closes on same line
foo = {'a': {'x': 'hello', 'y': 'world'}, 'b': {'x': 'hello', 'y': 'world'}}

# Right
foo = {
    'a': {'x': 'hello', 'y': 'world'},
    'b': {
        'x': 'hello',
        'y': 'world',
    },
}


# Dict has child with a child dict
# Wrong: JS101
foo = {'a': {'one': 'hello'}, 'b': {'two': 'world'},
       'c': {'three': 'hello'}, 'd': {'four': 'world'},
}


# Wrong: JS101, JS102
foo = {
    'a': {'x': 'hello', 'y': 'world'},
    'b': {'x': 'hello',
          'y': 'world'},
}


# Wrong: JS102
foo = {
    'a': {'x': 'hello', 'y': 'world'},
    'b': {'x': 'hello', 'y': 'world'},
      }


# Right: Function call in dict that's in a tuple
foo = ({'a': object()})
