# Right: Opens and closes on same line
foo = ['hello', 'world']


# Right: Line break after parenthesis, closes on same column
foo = [
    'hello',
    'world',
]


# Right: Line break after parenthesis, closes on same column
foo = [
    'hello', 'world',
]


# Wrong: JS101
foo = ['hello',
       'world',
]

# Wrong: JS102
foo = [
    'hello', 'world']


# Wrong: JS101, JS102
foo = ['hello',
       'world']


# Wrong: JS101, JS102
foo = ['hello',
       'world',
      ]


# Right: List with callables that have optional arguments is ignored
foo = [foobar(baz=False), foobar(baz=True)]

# Right: Multiline list with callables that have optional arguments is ignored
foo = [
    foobar(baz=False),
    foobar(baz=True),
]

# Right: Multiline list with callables with optional arguments with callables is ignored
foo = [
    foobar(baz=[bazbin(a=True)]),
    foobar(baz=[bazbin(a=False)]),
]

# Function calls in containers should be ignored
foo['a'] = [
    [
        baz,
        baz,
    ],
    [
        baz,
        baz,
    ],
]


foo['a'] = [
    [
        baz(x=True),
        baz(foobar='barfoo'),
    ],
    [
        baz(z=[1,2,3]),
        baz(z=(1, 2, 3)),
    ],
]