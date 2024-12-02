# Problem description:
# The puzzle input consists of many reports, one report per line.
# Each report is a list of numbers called levels that are separated by spaces.
# Figure out which line is safe:
# - The levels are either all increasing or all decreasing.
# - Any two adjacent levels differ by at least one and at most three.
# Problem Dampener: one bad level is allowed

from pathlib import Path

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
        
        # check previous level
        current = int(level)
        before = int(report[i-1])
        
        # unsafe if identical
        if before == current:
            return False
        
        # get mode
        diff = current - before
        if mode == 0:
            mode = diff/abs(diff)
            
        # unsafe if not increasing / descreasing the same way and more than 3
        if abs(diff) > 3:
            return False

        if mode != diff/abs(diff):
            return False
        
        # not at the end of the report
        if i != (reportCount - 1):
            continue
        
        # must be safe
        return True
    
# calculate answer
answer = 0
reports = []

for line in f:
    report = line.split()
    reports.append(report)
    
for report in reports:
    if isReportSafe(report):
        answer += 1
        continue

    for i, level in enumerate(report):
        newReport = report.copy()
        newReport.pop(i)
        
        if not isReportSafe(newReport):
            continue
        
        # it was safe, so add to answer and continue
        answer += 1
        break  

# output the answer
print(answer)
