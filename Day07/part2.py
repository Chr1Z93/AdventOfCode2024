# Problem description:
# Determine which test values could possibly be produced
# by placing any combination of operators into their calibration equations (your puzzle input).
# Operators are always evaluated left-to-right, not according to precedence rules.
# Get the sum of the test values from just the equations that could possibly be true.
# New operation: concatenation

from pathlib import Path
import time
import re
from itertools import product

# get correct subfolder path
script_path = Path(__file__).resolve()
script_dir = script_path.parent
input_path = script_dir / "input.txt"
input_file = open(input_path)


def add_numbers(a, b):
    return a + b


def multiply_numbers(a, b):
    return a * b


def concatenate_numbers(a, b):
    return int(str(a) + str(b))


def get_result(str):
    search = re.findall(r"\d+\:", str)
    return int(search[0][:-1])


def get_numbers(str):
    numbers = []
    search = re.findall(r"\s\d+", str)
    for str in search:
        numbers.append(int(str[1:]))
    return numbers


def test_for_result(result, numbers):
    operations = [add_numbers, multiply_numbers, concatenate_numbers]
    op_ids = list(product(range(len(operations)), repeat=len(numbers) - 1))

    for op_list in op_ids:
        if calculate(operations, op_list, numbers) == result:
            return True
    return False


def calculate(operations, op_list, numbers):
    value = numbers[0]
    for i in range(len(numbers) - 1):
        value = operations[op_list[i]](value, numbers[i + 1])
    return value


def get_answer():
    answer = 0

    for line in input_file:
        result = get_result(line)
        numbers = get_numbers(line)

        if test_for_result(result, numbers):
            answer += result

    return answer


# start timer and run main code
start_time = time.perf_counter()
answer = get_answer()
execution_time_ms = (time.perf_counter() - start_time) * 1000

# output results
print(f"{script_path.parent.name} - {script_path.name}")
print(f"Timing: {execution_time_ms:.3f} ms")
print(f"Answer: {answer}")
