import two


def test_read_program():
    raw_program = "1,9,10,3,2,3,11,0,99,30,40,50"
    actual = two.read_program(raw_program)
    expected = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
    assert actual == expected


def test_simple_sum():
    program = [1, 0, 0, 0, 99]
    expected = [2, 0, 0, 0, 99]
    actual = two.compute(program)
    assert actual == expected


def test_simple_product():
    program = [2, 3, 0, 3, 99]
    expected = [2, 3, 0, 6, 99]
    actual = two.compute(program)
    assert actual == expected


def test_simple_product_2():
    program = [2, 4, 4, 5, 99, 0]
    expected = [2, 4, 4, 5, 99, 9801]
    actual = two.compute(program)
    assert actual == expected


def test_overwrite_halt_code():
    program = [1, 1, 1, 4, 99, 5, 6, 0, 99]
    expected = [30, 1, 1, 4, 2, 5, 6, 0, 99]
    actual = two.compute(program)
    assert actual == expected


def test_compute_total():
    program = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
    actual = two.compute(program)
    expected = [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
    assert actual == expected
