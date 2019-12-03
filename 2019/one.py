from math import floor
import os

def get_fuel_v1(mass: int) -> int:
    return floor(mass / 3) - 2


def get_total_fuel_v1(filepath: str) -> int:
    with open(filepath, "r") as infile:
        masses = [int(mass.strip()) for mass in infile.readlines()]

    return sum([get_fuel_v1(mass) for mass in masses])


if __name__ == "__main__":
    this_path = os.path.dirname(__file__)
    inpath = os.sep.join([this_path, "one_input.txt"])
    print(get_total_fuel_v1(inpath))
