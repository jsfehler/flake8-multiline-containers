# Right
foo = {
    'a': {'x': 'hello', 'y': 'world'},
    'b': {
        'x': 'hello',
        'y': 'world',
    },
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
