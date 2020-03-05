# Right: Extra whitespace doesn't cause function to be registered as a tuple
def foo (a,
         b,
         c,
): pass

def foo     (a,
         b,
         c,
): pass

# Right: Function without any arguments.
def foo():
    pass


# Right: Function with arguments, ends on opening line.
def bar(a, b, c):
    pass


# Function with keyword argument that is a tuple.
# Right
def barb(a, b, c=('Hello', 'World')):
    pass


# Function with keyword argument that is a tuple.
# Right
def baro(a, b, c=(
    'Hello', 'World',
),
):
    pass


# Right: Function with arguments, break after lunula
def biz(
    a,
    b,
    c,
):
    pass


# Wrong: Function with arguments, break after first argument
def baz(a,
        b,
        c,
        ):
    pass


# Wrong: Function with arguments, break after first argument,
# closing bracket after last argument
def bal(a,
        b,
        c):
    pass
