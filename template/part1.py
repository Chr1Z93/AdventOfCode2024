# Problem description:
#
#
#
#

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
    print(f"Answer: {answer}")


print(f"{script_path.parent.name} - {script_path.name}")
execution_time = timeit.timeit(get_answer, number=1)
execution_time_ms = execution_time * 1000
print(f"Timing: {execution_time_ms:.3f} ms")
