from day2.solution import valid_passwords_count


def test_passwords_valid():
    assert valid_passwords_count("data/test_input.txt") == 2
