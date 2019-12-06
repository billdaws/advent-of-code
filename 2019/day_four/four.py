import os
this_path = os.path.dirname(__file__)
inpath = os.sep.join([this_path, "four_input.txt"])


def is_six_digits(x: int) -> bool:
    """This function isn't actually necessary given how I'll be generating the
    input.

    Oh well.
    """
    return len(str(x)) == 6


def within_range(x: int, lo: int, hi: int) -> bool:
    """This function isn't actually necessary given how I'll be generating the
    input.

    Oh well.
    """
    return lo <= x <= hi


def has_adjacent_double(x: int) -> bool:
    x_str = str(x)
    for i in range(len(x_str) - 1):
        if x_str[i] == x_str[i + 1]:
            return True

    return False


def has_adjacent_double_v2(x: int) -> bool:
    """Like has_adjacent_double, but this time makes sure that the adjacent
    double is not actually part of a longer run of the same digit.
    
    Note that this approach only works on values that passed part 1's 
    constraints.
    """
    x_str = str(x)
    for n in x_str:
        if x_str.count(n) == 2:
            return True
        
    return False


"""
Note that 'has_adjacent_double' and 'digits_never_decrease' could be
done in the same pass, but I prefer the small simple function given
that the range of inputs and the size of each input is small.

If performance were a concern, this would be an obvious target for optimization.
"""


def digits_never_decrease(x: int) -> bool:
    while x > 0:
        lsd = x % 10
        x = int(x / 10)  # int conversion just to deal with mypy warning
        # this operation shouldn't cause any problems
        # because an int divided by 10 should not encounter
        # round-off issues
        if lsd < x % 10:
            return False

    return True


if __name__ == "__main__":
    with open(inpath, "r") as f:
        str_lo, str_hi = f.read().split("-")
        lo = int(str_lo)
        hi = int(str_hi)

    part_one_accepted = 0
    part_two_accepted = 0
    for x in range(lo, hi + 1):
        if digits_never_decrease(x):
            if has_adjacent_double(x):
                part_one_accepted += 1
                if has_adjacent_double_v2(x):
                    part_two_accepted += 1
        
    print(f"Part one has {part_one_accepted} acceptable answers.")
    print(f"Part two has {part_two_accepted} acceptable answers.")
