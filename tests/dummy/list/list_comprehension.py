# Right: Opens and closes on same line

foo = ['a', 'b', 'a', 'c']
x = [i for i in foo if i == 'a']

# Right: Equality comparison isn't misidentified as an assignment
x = [i for i in foo['bar'] if i['baz'] == ex['baz']]
