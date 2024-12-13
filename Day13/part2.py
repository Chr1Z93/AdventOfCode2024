# Problem description:
# Claw machines with two buttons: A and B
# Need to hit prize with lowest cost (A costs 3, B costs 1)
# Prize + 10000000000000

from pathlib import Path
import time
import re

# get correct subfolder path
script_path = Path(__file__).resolve()
script_dir = script_path.parent
input_path = script_dir / "input.txt"
input_file = open(input_path)


def get_answer():
    answer = 0
    games = []
    current_game = {}
    for line in input_file:
        data = re.findall("\\d+", line)

        if "Button A" in line:
            current_game["a1"] = int(data[0])
            current_game["a2"] = int(data[1])
        elif "Button B" in line:
            current_game["b1"] = int(data[0])
            current_game["b2"] = int(data[1])
        elif "Prize" in line:
            current_game["c1"] = int(data[0]) + 10000000000000
            current_game["c2"] = int(data[1]) + 10000000000000
            games.append(current_game)
            current_game = {}

    for game in games:
        for i in range(10000000000000):
            x1 = (game["c1"] - i * game["b1"]) / game["a1"]
            if x1 > 100:
                continue

            x2 = (game["c2"] - i * game["b2"]) / game["a2"]
            if x1 != x2:
                continue

            int_x1 = int(x1)
            if int_x1 == x1:
                answer += int_x1 * 3 + i
                break

    return answer


# start timer and run main code
start_time = time.perf_counter()
answer = get_answer()
execution_time_ms = (time.perf_counter() - start_time) * 1000

# output results
print(f"{script_path.parent.name} - {script_path.name}")
print(f"Timing: {execution_time_ms:.3f} ms")
print(f"Answer: {answer}")
