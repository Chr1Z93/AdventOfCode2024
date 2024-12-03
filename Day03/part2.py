# Problem description:
# Input is corrupted.
# It's supposed the be a lot of multiply statements
# Scan for those and sum up the resulting numbers
# Also find do() and don't() and enable / disable following statements

from pathlib import Path
import time
import re

# get correct subfolder path
scriptPath = Path(__file__).resolve()
scriptDir = scriptPath.parent
inputPath = scriptDir / "input.txt"
f = open(inputPath)


def getAnswer():
    answer = 0
    enabled = True

    for line in f:
        search_results = re.findall("mul\(\d+\,\d+\)|do\(\)|don't\(\)", line)

        for statement in search_results:
            if statement == "do()":
                enabled = True
                continue

            if statement == "don't()":
                enabled = False
                continue

            if enabled:
                numbers = re.findall("\d+", statement)
                answer += int(numbers[0]) * int(numbers[1])

    return answer


# start timer and run main code
start_time = time.perf_counter()
answer = getAnswer()
execution_time_ms = (time.perf_counter() - start_time) * 1000

# output results
print(f"{scriptPath.parent.name} - {scriptPath.name}")
print(f"Timing: {execution_time_ms:.3f} ms")
print(f"Answer: {answer}")
