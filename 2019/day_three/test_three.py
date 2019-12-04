import three

def test_init_grid_gives_correct_dimensions():
    wires = ["R8,U5,L5,D3"]
    expected = [
        "...........",
        "...........",
        "...........",
        "...........",
        "...........",
        "...........",
        "...........",
        "...........",
        "..........."
    ]
    actual = three.init_grid(wires)
    assert len(expected) == len(actual)
    for i in range(len(expected)):
        assert len(expected[i]) == len(actual[i])

def test_manhattan_1():
    wires = """R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83"""
    expected = 159
    actual = three.manhattan(wires)
    assert expected == actual

def test_manhattan_2():
    wires = """R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"""
    expected = 135
    actual = three.manhattan(wires)
    assert expected == actual
