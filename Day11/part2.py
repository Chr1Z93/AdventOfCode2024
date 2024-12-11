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
import math

# get correct subfolder path
script_path = Path(__file__).resolve()
script_dir = script_path.parent
input_path = script_dir / "input.txt"
input_file = open(input_path)


def get_stones_after_blinking(stones, blinks):
    stone_cache = {0: [1]}

    previous_blink = stones
    for i in range(blinks):
        current_blink = []

        for stone in previous_blink:
            if stone in stone_cache:
                for new_stone in stone_cache[stone]:
                    current_blink.append(new_stone)
                continue

            num_digits = math.floor(math.log10(abs(stone))) + 1
            if num_digits % 2 == 0:
                half_digits = num_digits // 2
                divisor = 10**half_digits
                left_half = stone // divisor
                right_half = stone % divisor

                current_blink.append(left_half)
                current_blink.append(right_half)
                stone_cache[stone] = [left_half, right_half]
                continue

            current_blink.append(stone * 2024)

        previous_blink = current_blink

    return current_blink


def get_answer():
    stones = []
    for line in input_file:
        for m in re.finditer("\\d+", line):
            stones.append(int(m.group()))

    stones_blinked = get_stones_after_blinking(stones, 45)
    return len(stones_blinked)


# start timer and run main code
start_time = time.perf_counter()
answer = get_answer()
execution_time_ms = (time.perf_counter() - start_time) * 1000

# output results
print(f"{script_path.parent.name} - {script_path.name}")
print(f"Timing: {execution_time_ms:.3f} ms")
print(f"Answer: {answer}")
