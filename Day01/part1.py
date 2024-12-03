# Problem description:
# Two lists (two numbers with a space)
# Sort them
# Get differences (absolute)
# Sum up the differences

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
        answer += abs(int(list1[i]) - int(list2[i]))

    # output the answer
    print(f"Answer: {answer}")


print(f"{script_path.parent.name} - {script_path.name}")
execution_time = timeit.timeit(get_answer, number=1)
execution_time_ms = execution_time * 1000
print(f"Timing: {execution_time_ms:.3f} ms")
