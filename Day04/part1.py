# Problem description:
# Word search
# horizontal, vertical, diagonal, written backwards, or even overlapping other words.

from pathlib import Path
import time

# get correct subfolder path
script_path = Path(__file__).resolve()
script_dir = script_path.parent
input_path = script_dir / "input.txt"
input_file = open(input_path)


def get_char_from_grid(grid, v):
    if (
        v["row"] >= 0
        and v["col"] >= 0
        and len(grid) > v["row"]
        and len(grid[v["row"]]) > v["col"]
    ):
        return grid[v["row"]][v["col"]]
    return False


def make_line(start_row, start_col, row_modifier, col_modifier, grid):
    line = ""
    for x in range(len(grid)):
        vector = {
            "row": start_row + x * row_modifier,
            "col": start_col + x * col_modifier,
        }

        char = get_char_from_grid(grid, vector)
        if char == False:
            return line

        line += char
    return line


def get_answer():
    answer = 0
    grid = []
    search_strings = {
        "horizontal": [],
        "vertical": [],
        "diagonal_top": [],
        "diagonal_bottom": [],
    }

    for line in input_file:
        string = line.strip()
        grid.append(string)
        search_strings["horizontal"].append(string)

    j = len(grid)
    for i in range(j):
        search_strings["vertical"].append(make_line(0, i, 1, 0, grid))
        search_strings["diagonal_top"].append(make_line(0, i, 1, 1, grid))
        search_strings["diagonal_top"].append(make_line(0, i, 1, -1, grid))

        # exclude main diagonals from being searched twice
        if i == 0 or i == j - 1:
            continue

        search_strings["diagonal_bottom"].append(make_line(j - 1, i, -1, -1, grid))
        search_strings["diagonal_bottom"].append(make_line(j - 1, i, -1, 1, grid))

    for search_type, string_list in search_strings.items():
        sub_answer = 0
        for string in string_list:
            sub_answer += string.count("XMAS")
            sub_answer += string.count("SAMX")
        answer += sub_answer
    return answer


# start timer and run main code
start_time = time.perf_counter()
answer = get_answer()
execution_time_ms = (time.perf_counter() - start_time) * 1000

# output results
print(f"{script_path.parent.name} - {script_path.name}")
print(f"Timing: {execution_time_ms:.3f} ms")
print(f"Answer: {answer}")
