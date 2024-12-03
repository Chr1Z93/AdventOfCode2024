# Problem description:
# The puzzle input consists of many reports, one report per line.
# Each report is a list of numbers called levels that are separated by spaces.
# Figure out which line is safe:
# - The levels are either all increasing or all decreasing.
# - Any two adjacent levels differ by at least one and at most three.
# Problem Dampener: one bad level is allowed

from pathlib import Path
import time

# get correct subfolder path
script_path = Path(__file__).resolve()
script_dir = script_path.parent
input_path = script_dir / "input.txt"
f = open(input_path)


def is_report_safe(report):
    report_count = len(report)
    mode = 0

    for i, level in enumerate(report):
        if i == 0:
            continue

        diff = level - report[i - 1]
        abs_diff = abs(diff)

        # unsafe if not increasing / descreasing the same way and more than 3
        if abs_diff > 3 or abs_diff == 0:
            return False

        if mode == 0:
            mode = diff / abs_diff

        if mode != diff / abs_diff:
            return False

        # not at the end of the report
        if i != (report_count - 1):
            continue

        # must be safe, if the code got to this point
        return True


def get_answer():
    answer = 0

    for line in f:
        splits = line.split()
        report = []

        # store report with levels as numbers
        for split in splits:
            report.append(int(split))

        # check safety
        if is_report_safe(report):
            answer += 1
            continue

        # check variations with one level removed
        for i, level in enumerate(report):
            new_report = report.copy()
            new_report.pop(i)

            if is_report_safe(new_report):
                answer += 1
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
