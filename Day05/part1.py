# Problem description:
# The Elf has for you both the page ordering rules and the pages to produce in each update (your puzzle input),
# but can't figure out whether each update has the pages in the right order.
# Determine which updates are already in the correct order.
# What do you get if you add up the middle page number from those correctly-ordered updates?

from pathlib import Path
import time
import re
from functools import cmp_to_key

# get correct subfolder path
script_path = Path(__file__).resolve()
script_dir = script_path.parent
input_path = script_dir / "input.txt"
input_file = open(input_path)


def cmp_items(a, b):
    if is_p1_after_p2(a, b):
        return 1
    elif is_p1_after_p2(b, a):
        return -1
    else:
        return 0


def is_p1_after_p2(p1, p2):
    global ordering_rules

    if p2 in ordering_rules:
        for page in ordering_rules[p2]:
            if page == p1:
                return True

    return False


def get_correct_order(list):
    new_list = list.copy()
    cmp_items_py3 = cmp_to_key(cmp_items)
    new_list.sort(key=cmp_items_py3)
    return new_list


def get_answer():
    answer = 0

    # dictionary of ordering rules (1st page: pages that must come after)
    global ordering_rules
    ordering_rules = {}

    # keep track of section
    section = 1

    for line in input_file:
        if line == "\n":
            section += 1
            continue

        number_strings = re.findall(r"\d+", line)

        if section == 1:
            # add to ordering rules
            if number_strings[0] in ordering_rules:
                ordering_rules[number_strings[0]].append(number_strings[1])
            else:
                ordering_rules[number_strings[0]] = [number_strings[1]]
        else:
            # check if this update is correctly ordered
            correct_list = get_correct_order(number_strings)

            # if it's correctly ordered, add the middle number
            if correct_list == number_strings:
                answer += int(number_strings[len(number_strings) // 2])

    return answer


# start timer and run main code
start_time = time.perf_counter()
answer = get_answer()
execution_time_ms = (time.perf_counter() - start_time) * 1000

# output results
print(f"{script_path.parent.name} - {script_path.name}")
print(f"Timing: {execution_time_ms:.3f} ms")
print(f"Answer: {answer}")
