# Problem description:
# The reindeer brings you a blank topographic map of the surrounding area.
# Hiking trails never include diagonal steps - only up, down, left, or right (from the perspective of the map).
# A trailhead is any position that starts one or more hiking trails - here, these positions will always have height 0.
# Sum of the scores of all trailheads

from pathlib import Path
import time
import copy
import re

# get correct subfolder path
script_path = Path(__file__).resolve()
script_dir = script_path.parent
input_path = script_dir / "example.txt"
input_file = open(input_path)


def get_char_from_grid(grid, input_v, offset_row=0, offset_col=0):
    v = {"row": input_v["row"] + offset_row, "col": input_v["col"] + offset_col}
    if (
        v["row"] >= 0
        and v["col"] >= 0
        and len(grid) > v["row"]
        and len(grid[v["row"]]) > v["col"]
    ):
        return int(grid[v["row"]][v["col"]])
    return False


def is_position_an_increase(grid, input_v, offset):
    start_char = get_char_from_grid(grid, input_v)
    next_char = get_char_from_grid(grid, input_v, offset["row"], offset["col"])

    if next_char == False or next_char != start_char + 1:
        return False
    else:
        return True


def get_trailheads(grid, size):
    trailheads = []
    for row in range(size):
        for m in re.finditer("0", grid[row]):
            trailheads.append({"row": row, "col": m.start()})
    return trailheads


def get_trailhead_scores(grid, trailheads):
    trailhead_scores = trailheads.copy()
    for i, v in enumerate(trailhead_scores):
        v["score"] = get_score(grid, v)
    return trailhead_scores


def get_score(grid, v):
    reachable_nines = []
    offsets = {
        "above": {"row": -1, "col": 0},
        "right": {"row": 0, "col": 1},
        "below": {"row": 1, "col": 0},
        "left": {"row": 0, "col": -1},
    }

    for i in range(10):
        vec = copy.deepcopy(v)
        for direction, offset in offsets.items():
            if is_position_an_increase(grid, v, offset):
                vec["row"] += offset["row"]
                vec["col"] += offset["col"]
                if i == 9:
                    reachable_nines.append(vec["row"] * 100 + vec["col"])

    return len(set(reachable_nines))


def get_answer():
    answer = 0

    grid = []
    for line in input_file:
        grid.append(line.strip())

    size = len(grid)
    trailheads = get_trailheads(grid, size)
    trailhead_scores = get_trailhead_scores(grid, trailheads)

    print(trailhead_scores)
    return answer


# start timer and run main code
start_time = time.perf_counter()
answer = get_answer()
execution_time_ms = (time.perf_counter() - start_time) * 1000

# output results
print(f"{script_path.parent.name} - {script_path.name}")
print(f"Timing: {execution_time_ms:.3f} ms")
print(f"Answer: {answer}")
