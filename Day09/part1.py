# Problem description:
# He shows you the disk map (your puzzle input) he's already generated.
# The disk map uses a dense format to represent the layout of files and free space on the disk.
# The digits alternate between indicating the length of a file and the length of free space.
# The final step of this file-compacting process is to update the filesystem checksum.
# To calculate the checksum, add up the result of multiplying each of these blocks'
# position with the file ID number it contains. The leftmost block is in position 0.

from pathlib import Path
import time

# get correct subfolder path
script_path = Path(__file__).resolve()
script_dir = script_path.parent
input_path = script_dir / "input.txt"
input_file = open(input_path)


def get_answer():
    answer = 0

    expanded_map = []
    is_file = True
    for line in input_file:
        string = line.strip()
        id = 0
        for char in string:
            num = int(char)

            for i in range(num):
                if is_file:
                    expanded_map.append(id)
                else:
                    expanded_map.append(".")
            if is_file:
                id += 1
            is_file = not is_file

    number_map = []
    dot_ids = []
    for id, e in enumerate(expanded_map):
        if e == ".":
            number_map.append(".")
            dot_ids.append(id)
        else:
            number_map.append(e)

    replace_id = 0
    max_replace = len(dot_ids)
    reordered_map = number_map.copy()
    for i, e in reversed(list(enumerate(reordered_map))):
        if e == ".":
            continue

        dot_id = dot_ids[replace_id]
        if dot_id >= i:
            break

        reordered_map[dot_id] = e
        reordered_map[i] = "."
        replace_id += 1
        if replace_id >= max_replace:
            break

    for i, e in enumerate(reordered_map):
        if e != ".":
            answer += i * e

    return answer


# start timer and run main code
start_time = time.perf_counter()
answer = get_answer()
execution_time_ms = (time.perf_counter() - start_time) * 1000

# output results
print(f"{script_path.parent.name} - {script_path.name}")
print(f"Timing: {execution_time_ms:.3f} ms")
print(f"Answer: {answer}")
