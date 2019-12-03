from one import get_fuel_v1


def test_fuel_when_mass_is_12():
    assert get_fuel_v1(12) == 2


def test_fuel_when_mass_is_14():
    assert get_fuel_v1(14) == 2


def test_fuel_when_mass_is_1969():
    assert get_fuel_v1(1969) == 654


def test_fuel_when_mass_is_100756():
    assert get_fuel_v1(100756) == 33583
