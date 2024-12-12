# Problem description:
# You find that the stones have a consistent behavior.
# Every time you blink, the stones each simultaneously change according to the first applicable rule in this list:
# If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
# If the stone is engraved with a number that has an even number of digits, it is replaced by two stones.
# The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone.
# (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
# If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
# How many stones will you have after blinking 75 times?

from pathlib import Path
import time
import re
from functools import cache

# get correct subfolder path
script_path = Path(__file__).resolve()
script_dir = script_path.parent
input_path = script_dir / "input.txt"
input_file = open(input_path)


@cache
def get_new_stones(stone):
    if stone == 0:
        return [1]

    num_digits = len(str(abs(stone)))
    if num_digits % 2 == 0:
        half_digits = num_digits // 2
        divisor = 10**half_digits
        left_half = stone // divisor
        right_half = stone % divisor

        return [left_half, right_half]

    return [stone * 2024]


@cache
def get_stones_after_blinking(stone, blinks):
    if blinks == 0:
        return [stone]

    previous_blink = get_stones_after_blinking(stone, blinks - 1)
    current_blink = [
        new_stone
        for previous_stone in previous_blink
        for new_stone in get_new_stones(previous_stone)
    ]
    return current_blink


def get_answer():
    answer = 0
    stones = []
    for line in input_file:
        for m in re.finditer("\\d+", line):
            stones.append(int(m.group()))

    for stone in stones:
        stones_blinked = get_stones_after_blinking(stone, 45)
        answer += len(stones_blinked)

    return answer


# start timer and run main code
start_time = time.perf_counter()
answer = get_answer()
execution_time_ms = (time.perf_counter() - start_time) * 1000

# output results
print(f"{script_path.parent.name} - {script_path.name}")
print(f"Timing: {execution_time_ms:.3f} ms")
print(f"Answer: {answer}")
