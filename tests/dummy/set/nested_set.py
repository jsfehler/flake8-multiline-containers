# Right
foo = {
    {'hello', 'world'},
    {
        'hello',
        'world',
    },
}


# Wrong: JS101, JS102
foo = {
    {'hello', 'world'},
    {'hello',
     'world'},
}


# Wrong: JS102
foo = {
    {'hello', 'world'},
    {'hello', 'world'},
      }


# Right: Function call in set that's in a tuple
foo = ({object()})
