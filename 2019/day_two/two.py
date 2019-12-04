from typing import Tuple, Optional, List
from sys import exit
import os
this_path = os.path.dirname(__file__)
inpath = os.sep.join([this_path, "two_input.txt"])

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
        opcode = program[i]
        if opcode == 99:
            return program
        
        
        operand_1 = program[program[i + 1]]
        operand_2 = program[program[i + 2]]
        write_idx = program[i + 3]

        compute = funcs[opcode]
        result = compute(operand_1, operand_2)
        program[write_idx] = result

    return program

if __name__ == "__main__":
    with open(inpath, "r") as f:
        program = read_program(f.read())

    final_program = compute(program)
    print(final_program)