# Problem description:
# The map shows the current position of the guard with ^ (to indicate the guard is currently facing up from the perspective of the map).
# Any obstructions - crates, desks, alchemical reactors, etc. - are shown as #.
# If there is something directly in front of you, turn right 90 degrees. Otherwise, take a step forward.
# Predict the path of the guard. Detect time paradoxes, how many are possible with one additional obstruction?

from pathlib import Path
import time
import copy

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
    next_position = {
        "row": position["row"] + direction_to_offset[direction]["row"],
        "col": position["col"] + direction_to_offset[direction]["col"],
    }
    next_character = get_char_from_grid(grid, next_position)

    if next_character == False:
        return False
    elif next_character == "#":
        return get_next_position(grid, position, turn_right_direction[direction])
    return {"next_position": next_position, "direction": direction}


def visit_position(visited, position, direction):
    id = position["col"] * 1000 + position["row"]
    if id in visited:
        if direction in visited[id]:
            return False
        else:
            visited[id][direction] = True
    else:
        visited[id] = {direction: True}


def is_paradox(grid, start_position):
    position = start_position
    direction = "up"
    visited = {}
    for i in range(10000):
        visit = visit_position(visited, position, direction)
        if visit == False:
            return True

        data = get_next_position(grid, position, direction)
        if data == False:
            return False

        position = data["next_position"]
        direction = data["direction"]


def get_original_visits(grid, start_position):
    position = start_position
    direction = "up"
    visited = {}
    for i in range(10000):
        visit = visit_position(visited, position, direction)
        if visit == False:
            return visited

        data = get_next_position(grid, position, direction)
        if data == False:
            return visited

        position = data["next_position"]
        direction = data["direction"]
    return visited


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

    # get original visited spots
    original_visits = get_original_visits(grid, start_position)

    # introduce a random obstacle
    size = len(grid)
    for row in range(size):
        for col in range(size):
            if col * 1000 + row not in original_visits:
                continue

            if get_char_from_grid(grid, {"row": row, "col": col}) == "#":
                continue

            grid_copy = copy.deepcopy(grid)
            grid_copy[row] = grid_copy[row][:col] + "#" + grid_copy[row][col + 1 :]
            if is_paradox(grid_copy, start_position):
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
