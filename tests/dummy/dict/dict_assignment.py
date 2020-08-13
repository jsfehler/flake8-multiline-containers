# Right: Opens and closes on same line
foo = {}

# Assign list as value
foo['a'] = ['b', 'c']

# Assign dict as value
foo['a'] = {'b': 'hello', 'c': 'world'}

# Assign set as value
foo['a'] = {'b', 'c'}

# Assign tuple as value
foo['a'] = ('b', 'c',)

# Right: Line break after parenthesis, closes on same column

# Assign list as value
foo['a'] = [
    'b',
    'c',
    'd',
    'e',
]

# Assign dict as value
foo['a'] = {
    'b': 'hello',
    'c': 'world',
    'd': 'goodbye',
    'e': 'sky',
}

# Assign set as value
foo['a'] = {
    'b',
    'c',
    'd',
    'e',
}

# Assign tuple as value
foo['a'] = (
    'b',
    'c',
    'd',
    'e',
)

# Ridiculous
foo['a'][42] = [
    'You',
    'Do',
    'You',
]

bar = foo['a'] = [
    'Technically',
    'Valid',
    'But',
    'Still',
    'Bizarre',
]
