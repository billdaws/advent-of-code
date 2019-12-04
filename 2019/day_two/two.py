from typing import Tuple, Optional, List
from sys import exit
from math import floor
import os
this_path = os.path.dirname(__file__)
part_one_inpath = os.sep.join([this_path, "two_part_one_input.txt"])
part_two_inpath = os.sep.join([this_path, "two_part_two_input.txt"])

funcs = {
    1: lambda x, y: x + y,
    2: lambda x, y: x * y
}


def read_program(raw_program: str) -> List[int]:
    return [int(opcode) for opcode in raw_program.split(",")]


def compute(program: List[int]) -> List[int]:
    for i in range(0, len(program), 4):
        # an opcode sequence is either 4 ints or 1 int long,
        # so we can iterate safely
        instruction = program[i]
        if instruction == 99:
            return program

        operand_1 = program[program[i + 1]]
        operand_2 = program[program[i + 2]]
        write_idx = program[i + 3]

        func = funcs[instruction]
        result = func(operand_1, operand_2)
        program[write_idx] = result

    return program

def compute_v2(program: List[int], noun: int, verb: int) -> List[int]:
    intermediate = program.copy()
    intermediate[1] = noun
    intermediate[2] = verb
    return compute(intermediate)

def solve_part_two(program: List[int]) -> List[int]:
    """To solve part two, we might want to use binary search.
    TODO:
        this solution is O(n^2), how to do it better?
        multivariate binary search?
    """
    target = 19690720
    for n in range(0, 100):
        for v in range(0, 100):
            result = compute_v2(program, n, v)
            if result[0] == target:
                return result

    raise ValueError(
        """Tried all combinations of noun and verb values without
        achieving the desired result.""")
    

def solve(inpath: str, part: int) -> List[int]:
    with open(inpath, "r") as f:
        program = read_program(f.read())

    if part == 1:
        print("Solving part one...")
        return compute(program)
    elif part == 2:
        print("Solving part two...")
        return solve_part_two(program)
    else:
        raise ValueError(f"Computation for part {part} not provided.")


if __name__ == "__main__":
    part_one_solution = solve(part_one_inpath, 1)
    print(f"part_one_solution={part_one_solution}")
    part_two_solution = solve(part_two_inpath, 2)
    print(f"part_two_solution full program={part_two_solution}")
    print("part_two_solution[0] == 19690720:")
    print(part_two_solution[0] == 19690720)
    part_two_answer = part_two_solution[1] * 100 + part_two_solution[2]
    print(f"part_two_solution answer={part_two_answer}")
