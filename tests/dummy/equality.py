# Equality checks should behave the same way as assignment

# Variable equality check
bar == {'a': 1, 'b':2}

bar == {
    'a': 1,
    'b': 2,
}

# Function equality check
foo() == {
    'a': 1,
    'b': 2,
    'c': 3,
}


foo(1, 2, 3) == {
    'a': 1,
    'b': 2,
    'c': 3,
}
