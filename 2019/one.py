from typing import Callable
from math import floor
import os

def get_fuel_v1(mass: int) -> int:
    """Returns the amount of fuel needed for some given mass."""
    return floor(mass / 3) - 2

def get_fuel_v2(mass: int) -> int:
    """Returns the amount of fuel needed for some given mass, this time
    including the fuel required to carry that mass's fuel, and that mass's
    fuel's fuel, and so on."""
    temp_fuel = floor(mass / 3) - 2
    total_fuel = 0
    while temp_fuel > 0:
        total_fuel += temp_fuel
        temp_fuel = floor(temp_fuel / 3) - 2

    return total_fuel
    

def get_total_fuel(filepath: str, fuel_func: Callable[[int], int]) -> int:
    with open(filepath, "r") as infile:
        masses = [int(mass.strip()) for mass in infile.readlines()]

    return sum([fuel_func(mass) for mass in masses])


if __name__ == "__main__":
    this_path = os.path.dirname(__file__)
    inpath = os.sep.join([this_path, "one_input.txt"])
    print(f"get_total_fuel_v1({inpath}) = {get_total_fuel(inpath, get_fuel_v1)}")
    print(f"get_total_fuel_v2({inpath}) = {get_total_fuel(inpath, get_fuel_v2)}")
