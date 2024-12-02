# Problem description:
# The puzzle input consists of many reports, one report per line.
# Each report is a list of numbers called levels that are separated by spaces.
# Figure out which line is safe:
# - The levels are either all increasing or all decreasing.
# - Any two adjacent levels differ by at least one and at most three.

from pathlib import Path

# get correct subfolder path
scriptPath = Path(__file__).resolve()
scriptDir = scriptPath.parent
inputPath = scriptDir / "input.txt"
f = open(inputPath)

# calculate answer
answer = 0

for line in f:
    levels = line.split()
    reportCount = len(levels)
    mode = 0
    
    for i, level in enumerate(levels):
        if i == 0:
            continue
        
        # check previous level
        current = int(level)
        before = int(levels[i-1])
        
        # unsafe if identical
        if before == current:
            break
        
        # get mode
        diff = current - before
        if mode == 0:
            mode = diff/abs(diff)
            
        # unsafe if not increasing / descreasing the same way and less than 4
        if abs(diff) > 3:
            break

        if mode != diff/abs(diff):
            break
        
        # not at the end of the report
        if i != (reportCount - 1):
            continue

        # must be safe, add to answer
        answer += 1

# output the answer
print(answer)
