from one import get_fuel_v2


def test_fuel_when_mass_is_14():
    assert get_fuel_v2(14) == 2


def test_fuel_when_mass_is_1969():
    assert get_fuel_v2(1969) == 966


def test_fuel_when_mass_is_100756():
    assert get_fuel_v2(100756) == 50346
