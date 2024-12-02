# Problem description:
# 
# 
# 
# 

from pathlib import Path

# get correct subfolder path
scriptPath = Path(__file__).resolve()
scriptDir = scriptPath.parent
inputPath = scriptDir / "input.txt"
f = open(inputPath)

# calculate answer
answer = 0
firstChar = ""
secondChar = ""

# do something
for line in f:
    # get first digit
    for char in line:
        if char.isdigit():
            firstChar = char
            break

    # get last digit
    for char in reversed(line):
        if char.isdigit():
            secondChar = char
            break

    # combine both digits and add to answer
    answer += int(firstChar + secondChar)

# output the answer
print(answer)
