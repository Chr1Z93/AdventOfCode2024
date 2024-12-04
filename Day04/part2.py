# Problem description:
# Word search
# It's an X-MAS puzzle in which you're supposed to find two MAS in the shape of an X

from pathlib import Path
import time
import math
import re

# get correct subfolder path
script_path = Path(__file__).resolve()
script_dir = script_path.parent
input_path = script_dir / "input.txt"
input_file = open(input_path)


def get_char_from_grid(grid, input_v, offset_row=0, offset_col=0):
    v = {"row": input_v["row"] + offset_row, "col": input_v["col"] + offset_col}
    if (
        v["row"] >= 0
        and v["col"] >= 0
        and len(grid) > v["row"]
        and len(grid[v["row"]]) > v["col"]
    ):
        return grid[v["row"]][v["col"]]
    return False


def check_MAS_or_SAM(grid, vector, offset_row1, offset_row2, offset_col1, offset_col2):
    c_1 = get_char_from_grid(grid, vector, offset_row1, offset_col1)
    c_2 = get_char_from_grid(grid, vector, offset_row2, offset_col2)
    return (c_1 == "S" and c_2 == "M") or (c_1 == "M" and c_2 == "S")


def get_answer():
    answer = 0
    grid = []

    # parse input
    for line in input_file:
        grid.append(line.strip())

    # store positions of "A"s
    a_positions = {}
    for row, string in enumerate(grid):
        for m in re.finditer("A", string):
            a_positions[m.start() * 1000 + row] = True

    # check "A"s for eligiblity
    for id, state in a_positions.items():
        vector = {"row": id % 1000, "col": math.floor(id / 1000)}
        if check_MAS_or_SAM(grid, vector, -1, 1, 1, -1):
            if check_MAS_or_SAM(grid, vector, -1, 1, -1, 1):
                answer += 1

    return answer


# start timer and run main code
start_time = time.perf_counter()
answer = get_answer()
execution_time_ms = (time.perf_counter() - start_time) * 1000

# output results
print(f"{script_path.parent.name} - {script_path.name}")
print(f"Timing: {execution_time_ms:.3f} ms")
print(f"Answer: {answer}")
