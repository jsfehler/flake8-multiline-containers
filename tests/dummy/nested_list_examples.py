# Right
foo = [['hello', 'world'], ['sun', 'moon']]

# Right
foo = [
    ['hello', 'world'],
    [
        'hello',
        'world',
    ],
]


# list has child list that ends on same line as opening
# Wrong: JS101
foo = [['earth', 'mars'],
       ['sun', 'moon'],
]


# list has child with a child list that ends on same line as opening
# Wrong: JS101
foo = [{'a': 'hello', 'b': ['earth', 'mars']},
       {'c': 'good night', 'd': 'moon'},
]


# Nested list contains a container that doesn't break on the opening
# Wrong: JS101, JS102
foo = [
    ['hello', 'world'],
    ['hello',
     'world'],
]


# Nested list closes on wrong column
# Wrong: JS102
foo = [
    ['hello', 'world'],
    ['hello', 'world'],
      ]
