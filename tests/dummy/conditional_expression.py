# Conditional expression where the third part of the expression is a
# multiline container
bar = 0


foo = {} if bar == 1 else {
    "foo": 42,
}


foo = [] if bar == 1 else [
    42,
}


foo = () if bar == 1 else (
    42, 42,
}
