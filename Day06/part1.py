# Problem description:
# The map shows the current position of the guard with ^ (to indicate the guard is currently facing up from the perspective of the map).
# Any obstructions - crates, desks, alchemical reactors, etc. - are shown as #.
# If there is something directly in front of you, turn right 90 degrees. Otherwise, take a step forward.
# Predict the path of the guard. How many distinct positions will the guard visit before leaving the mapped area?

from pathlib import Path
import time

# get correct subfolder path
script_path = Path(__file__).resolve()
script_dir = script_path.parent
input_path = script_dir / "input.txt"
input_file = open(input_path)

direction_to_offset = {
    "up": {"row": -1, "col": 0},
    "right": {"row": 0, "col": 1},
    "down": {"row": 1, "col": 0},
    "left": {"row": 0, "col": -1},
}

turn_right_direction = {
    "up": "right",
    "right": "down",
    "down": "left",
    "left": "up",
}


def get_char_from_grid(grid, input, offset={"row": 0, "col": 0}):
    v = {"row": input["row"] + offset["row"], "col": input["col"] + offset["col"]}
    if (
        v["row"] >= 0
        and v["col"] >= 0
        and len(grid) > v["row"]
        and len(grid[v["row"]]) > v["col"]
    ):
        return grid[v["row"]][v["col"]]
    return False


def get_next_position(grid, position, direction):
    offset = direction_to_offset[direction]
    next_position = {
        "row": position["row"] + offset["row"],
        "col": position["col"] + offset["col"],
    }
    next_character = get_char_from_grid(grid, next_position)

    if next_character == False:
        return False
    elif next_character == "#":
        # print(f"Pos: {position} | {direction}")
        new_direction = turn_right_direction[direction]
        return get_next_position(grid, position, new_direction)
    return {"next_position": next_position, "direction": direction}


def get_answer():
    answer = 0
    grid = []
    start_position = {}
    row = 0

    for line in input_file:
        grid.append(line.strip())
        find_start = line.find("^")
        if find_start >= 0:
            start_position["row"] = row
            start_position["col"] = find_start

        row += 1

    position = start_position
    direction = "up"
    visited_positions = {}
    visited_positions[position["col"] * 1000 + position["row"]] = True
    for i in range(10000):
        data = get_next_position(grid, position, direction)
        if data == False:
            print(f"Number of steps: {i}")
            break

        position = data["next_position"]
        direction = data["direction"]
        visited_positions[position["col"] * 1000 + position["row"]] = True

    answer = len(visited_positions)
    return answer


# start timer and run main code
start_time = time.perf_counter()
answer = get_answer()
execution_time_ms = (time.perf_counter() - start_time) * 1000

# output results
print(f"{script_path.parent.name} - {script_path.name}")
print(f"Timing: {execution_time_ms:.3f} ms")
print(f"Answer: {answer}")
