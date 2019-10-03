# Comments should be ignored entirely

# Technically correct, but would fail JS102 if detected
# 'foobar': {
#     'foo': 'Hello',
#     'bar': 'World',
# },

# JS101, but ignored
# 'foobar': { 'foo': 'Hello',
#             'bar': 'World',
# },


# I'd slap you if you did this in real code, but it's... fine in a comment.

        # 'foobar': {
                    #     'foo': 'Hello',
                    #     'bar': 'World',
        # },

        # 'foobar': { 'foo': 'Hello',
                    #             'bar': 'World',
        #    },


# Why do you do this? Still, ignored.
a = b # a = { 'foobar': 'Hello',
x = y #       'barfoo': 'World' }
