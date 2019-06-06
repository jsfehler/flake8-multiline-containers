s = '{', '}', "foo={a\n", 'bar'
s = '{', '}', "foo=}a\n", 'bar'

string_only_opens_sq = '[foobar'
string_only_closes_sq = 'foobar]'

string_only_opens_dq = "[foobar"
string_only_closes_dq = "foobar]"

has_escape_characters = '[The cold echo of his master\'s laugh]'
