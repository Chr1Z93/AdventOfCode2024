# Problem description:
# Each antenna is tuned to a specific frequency indicated by a single lowercase letter, uppercase letter, or digit.
# You create a map (your puzzle input) of these antennas.
# An antinode occurs at any point that is perfectly in line with two antennas of the same frequency -
# but only when one of the antennas is twice as far away as the other.
# After updating your model, it turns out that an antinode occurs at any grid position exactly in line
# with at least two antennas of the same frequency, regardless of distance.
# How many unique locations within the bounds of the map contain an antinode?

from pathlib import Path
import time
import re
import math

# get correct subfolder path
script_path = Path(__file__).resolve()
script_dir = script_path.parent
input_path = script_dir / "input.txt"
input_file = open(input_path)


def get_matching_antennas(f_data, v):
    matching_antennas = []

    for row, r_data in f_data.items():
        for col, c_data in r_data.items():
            if row > v["row"]:
                matching_antennas.append({"row": row, "col": col})

    return matching_antennas


def get_antinodes(grid, v1, v2):
    antinodes = []
    row_distance = v2["row"] - v1["row"]
    col_distance = v2["col"] - v1["col"]

    for i in range(math.ceil(len(grid) / abs(row_distance))):
        pos1 = {
            "row": v1["row"] - row_distance * i,
            "col": v1["col"] - col_distance * i,
        }
        if is_inside_grid(grid, pos1):
            antinodes.append(pos1)

    for i in range(math.ceil(len(grid) / abs(col_distance))):
        pos2 = {
            "row": v2["row"] + row_distance * i,
            "col": v2["col"] + col_distance * i,
        }
        if is_inside_grid(grid, pos2):
            antinodes.append(pos2)

    return antinodes


def is_inside_grid(grid, v):
    return (
        v["row"] > -1
        and v["col"] > -1
        and len(grid) > v["row"]
        and len(grid[v["row"]]) > v["col"]
    )


def get_answer():
    answer = 0

    # make grid
    grid = []
    for line in input_file:
        string = line.strip()
        grid.append(string)

    # get antenna positions
    antennas = {}
    for row in range(len(grid)):
        for m in re.finditer("[^.]", grid[row]):
            frequency = m.group()
            col = m.start()

            if frequency not in antennas:
                antennas[frequency] = {}

            if row not in antennas[frequency]:
                antennas[frequency][row] = {}

            antennas[frequency][row][col] = True

    # check for antinodes
    antinodes = {}
    for frequency, f_data in antennas.items():
        for row, r_data in f_data.items():
            for col, c_data in r_data.items():
                antenna1 = {"row": row, "col": col}
                for antenna2 in get_matching_antennas(f_data, antenna1):
                    for antinode in get_antinodes(grid, antenna1, antenna2):
                        if antinode["row"] not in antinodes:
                            antinodes[antinode["row"]] = {}
                        antinodes[antinode["row"]][antinode["col"]] = True

    # count antinodes
    for row, r_data in antinodes.items():
        for col, c_data in r_data.items():
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
