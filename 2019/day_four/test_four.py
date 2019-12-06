import four


def test_is_six_digits():
    x = 100000
    assert four.is_six_digits(x) == True


def test_is_not_six_digits():
    x = 1
    assert four.is_six_digits(x) == False


def test_within_range():
    lo = 1
    hi = 100
    x = 50
    assert four.within_range(x, lo, hi) == True


def test_not_within_range():
    lo = 1
    hi = 100
    x = 5000
    assert four.within_range(x, lo, hi) == False


def test_has_adjacent_double():
    x = 9900
    assert four.has_adjacent_double(x) == True


def test_does_not_have_adjacent_double():
    x = 123456789
    assert four.has_adjacent_double(x) == False


def test_has_adjacent_double_v2():
    x = 112233
    assert four.has_adjacent_double_v2(x) == True


def test_does_not_have_adjacent_double_v2():
    x = 123444
    assert four.has_adjacent_double_v2(x) == False


def test_has_adjacent_double_v2_with_long_run():
    x = 111122
    assert four.has_adjacent_double_v2(x) == True

def test_should_abend():
    x = 212
    assert four.has_adjacent_double_v2(x) == False

def test_digits_never_decrease():
    x = 12345
    assert four.digits_never_decrease(x) == True


def test_digits_stay_the_same():
    x = 11111
    assert four.digits_never_decrease(x) == True


def test_digits_do_decrease():
    x = 223450
    assert four.digits_never_decrease(x) == False
