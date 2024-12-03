# Problem description:
# Input is corrupted.
# It's supposed the be a lot of multiply statements
# Scan for those and sum up the resulting numbers

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

    for line in input_file:

        for statement in re.findall("mul\(\d+\,\d+\)", line):
            numbers = re.findall("\d+", statement)
            answer += int(numbers[0]) * int(numbers[1])

    return answer


# start timer and run main code
start_time = time.perf_counter()
answer = get_answer()
execution_time_ms = (time.perf_counter() - start_time) * 1000

# output results
print(f"{script_path.parent.name} - {script_path.name}")
print(f"Timing: {execution_time_ms:.3f} ms")
print(f"Answer: {answer}")
