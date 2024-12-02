# Problem description:
# Two lists (two numbers with a space)
# Sort them
# Get differences (absolute)
# Sum up the differences

from pathlib import Path

# get correct subfolder path
scriptPath = Path(__file__).resolve()
scriptDir = scriptPath.parent
inputPath = scriptDir / "input.txt"
f = open(inputPath)

# calculate answer
answer = 0
list1 = []
list2 = []

# parse input
for line in f:
    numberList = line.split()
    
    list1.append(numberList[0])
    list2.append(numberList[1])

# sort lists
list1.sort()
list2.sort()

# get differences
for i in range(len(list1)):
    # add to answer
    answer += abs(int(list1[i])-int(list2[i]))

# output the answer
print(answer)
