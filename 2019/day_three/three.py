import os
from typing import List
this_path = os.path.dirname(__file__)
inpath = os.sep.join([this_path, "three_input.txt"])

example = [
    "...........",
    "...........",
    "...........",
    "....+----+.",
    "....|....|.",
    "....|....|.",
    "....|....|.",
    ".........|.",
    ".o-------+.",
    "..........."
]

longest = {
    "R": 0,
    "L": 0,
    "U": 0,
    "D": 0
}

def init_grid(wires: List[str]) -> List[str]:
    # TODO start here
    for wire in wires:
        directions = wire.split(",")
        for direction in directions:
            point = direction[0] # up down left right
            magnitude = int(direction[1:])
            longest[point] = max(longest[point], magnitude)
            
    max_width = longest["L"] + longest["R"] + 1
    max_height = longest["U"] + longest["D"] + 1

    grid = ["." * max_width] * max_height
    return grid
    


def draw_wire(wire: str) -> List[str]:
    directions = wire.split(",")
    return [""]


def draw_grid(wires: List[str]) -> List[str]:
    grid = init_grid(wires)
    
    for wire in wires:
        grid = draw_wire(wire)
    return grid

def manhattan(wires: str):
    wires_list = wires.split("\n")
    grid = draw_grid(wires_list)
    return "foo"