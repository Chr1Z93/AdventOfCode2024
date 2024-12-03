# Problem description:
# The puzzle input consists of many reports, one report per line.
# Each report is a list of numbers called levels that are separated by spaces.
# Figure out which line is safe:
# - The levels are either all increasing or all decreasing.
# - Any two adjacent levels differ by at least one and at most three.

from pathlib import Path
import timeit

# get correct subfolder path
script_path = Path(__file__).resolve()
script_dir = script_path.parent
input_path = script_dir / "input.txt"
f = open(input_path)


# calculate answer
def get_answer():
    answer = 0

    for line in f:
        levels = line.split()
        report_count = len(levels)
        mode = 0

        for i, level in enumerate(levels):
            if i == 0:
                continue

            # check previous level
            current = int(level)
            before = int(levels[i - 1])

            # unsafe if identical
            if before == current:
                break

            # get mode
            diff = current - before
            if mode == 0:
                mode = diff / abs(diff)

            # unsafe if not increasing / descreasing the same way and less than 4
            if abs(diff) > 3:
                break

            if mode != diff / abs(diff):
                break

            # not at the end of the report
            if i != (report_count - 1):
                continue

            # must be safe, add to answer
            answer += 1

    # output the answer
    print(f"Answer: {answer}")


print(f"{script_path.parent.name} - {script_path.name}")
execution_time = timeit.timeit(get_answer, number=1)
execution_time_ms = execution_time * 1000
print(f"Timing: {execution_time_ms:.3f} ms")
