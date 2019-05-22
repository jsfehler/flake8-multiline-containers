from flake8_multiline_containers import get_left_pad


def test_get_left_pad():
    amount = get_left_pad("          test")

    assert 10 == amount
