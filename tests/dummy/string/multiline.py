# Triple quote strings should be ignored

foo = """(a=10"""

foo = """(a=10
)
"""

foo = """
(a=10
 )
"""

foo = '''(a=10'''

foo = '''(a=10
)
'''

foo = '''
(a=10
 )
'''
