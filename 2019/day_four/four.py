import os
this_path = os.path.dirname(__file__)
inpath = os.sep.join([this_path, "four_input.txt"])

def is_six_digits(x: int) -> bool:
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

"""
Note that 'has_adjacent_double' and 'digits_never_decrease' could be
done in the same pass, but I prefer the small simple function given
that the range of inputs and the size of each input is small.

If performance were a concern, this would be an obvious target for optimization.
"""

def digits_never_decrease(x: int) -> bool:
    while x > 0:
        lsd = x % 10
        x = int(x / 10) # int conversion just to deal with mypy warning
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

    accepted = 0
    for x in range(lo, hi + 1):
        if is_six_digits(x) and \
            has_adjacent_double(x) and \
            digits_never_decrease(x):
            accepted += 1

    print(accepted)