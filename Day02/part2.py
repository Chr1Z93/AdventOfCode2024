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
scriptPath = Path(__file__).resolve()
scriptDir = scriptPath.parent
inputPath = scriptDir / "input.txt"
f = open(inputPath)

def isReportSafe(report):
    reportCount = len(report)
    mode = 0

    for i, level in enumerate(report):
        if i == 0:
            continue

        diff = level - report[i - 1]
        absDiff = abs(diff)

        # unsafe if not increasing / descreasing the same way and more than 3
        if absDiff > 3 or absDiff == 0:
            return False

        if mode == 0:
            mode = diff / absDiff

        if mode != diff / absDiff:
            return False

        # not at the end of the report
        if i != (reportCount - 1):
            continue

        # must be safe, if the code got to this point
        return True


def getAnswer():
    answer = 0

    for line in f:
        splits = line.split()
        report = []

        # store report with levels as numbers
        for split in splits:
            report.append(int(split))

        # check safety
        if isReportSafe(report):
            answer += 1
            continue

        # check variations with one level removed
        for i, level in enumerate(report):
            newReport = report.copy()
            newReport.pop(i)

            if isReportSafe(newReport):
                answer += 1
                break

    return answer

# start timer and run main code
start_time = time.perf_counter()
answer = getAnswer()
execution_time_ms = (time.perf_counter() - start_time) * 1000

# output results
print(f"{scriptPath.parent.name} - {scriptPath.name}")
print(f"Timing: {execution_time_ms:.3f} ms")
print(f"Answer: {answer}")
