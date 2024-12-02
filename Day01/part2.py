# Problem description:
# Two lists (two numbers with a space)
# Calculate a similarity score
# Each number on the left is counted in the right list and then multiplied by itself

from pathlib import Path

# get correct subfolder path
scriptPath = Path(__file__).resolve()
scriptDir = scriptPath.parent
inputPath = scriptDir / "input.txt"
f = open(inputPath)

# calculate answer
answer = 0
listLeft = []
dictRight = {}

# parse input
for line in f:
    numberList = line.split()
    listLeft.append(numberList[0])
    
    if numberList[1] in dictRight:
        dictRight[numberList[1]] += 1
    else:
        dictRight[numberList[1]] = 1

# get similarity score
for i in range(len(listLeft)):
    if listLeft[i] in dictRight:
        answer += int(listLeft[i])*int(dictRight[listLeft[i]])

# output the answer
print(answer)
