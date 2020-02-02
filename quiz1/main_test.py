import main


def test_nagetive_number():
    assert main.count_digit_v1(-1) == 0


def test_positive_number():
    assert main.count_digit_v1(9) == 1
    assert main.count_digit_v1(20) == 2
    assert main.count_digit_v1(50) == 5
    assert main.count_digit_v1(70) == 7
    assert main.count_digit_v1(80) == 18
    assert main.count_digit_v1(120) == 22
