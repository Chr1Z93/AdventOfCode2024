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


def calculate_checksum(number_map):
    result = 0
    for i, e in enumerate(number_map):
        if e != ".":
            result += i * e
    return result


def get_answer():
    expanded_map = []
    dot_ids = []
    empty_space_size = {}
    file_size = {}

    is_file = True
    for line in input_file:
        string = line.strip()
        file_id = 0
        map_id = 0
        for char in string:
            num = int(char)
            for i in range(num):
                if is_file:
                    expanded_map.append(file_id)
                    file_size[file_id] = num
                else:
                    expanded_map.append(".")
                    dot_ids.append(map_id)
                    empty_space_size[map_id] = num
                map_id += 1
            if is_file:
                file_id += 1
            is_file = not is_file

    reordered_map = expanded_map.copy()

    # loop through files
    for i, e in reversed(list(enumerate(expanded_map))):
        if e == ".":
            continue

        # loop through empty spaces
        for replace_id, dot_id in enumerate(dot_ids):
            # only move files if they can fit entirely in the empty space
            if empty_space_size[dot_id] < file_size[e]:
                continue

            # don't move files to the right
            if dot_id >= i:
                break

            # move the file block
            reordered_map[dot_id] = e
            reordered_map[i] = "."

            # maybe update adjacent empty_space_size (if this is the last block of the file)
            if expanded_map[i - 1] != e:
                for j in range(1, len(dot_ids)):
                    if replace_id + j >= len(dot_ids):
                        break

                    next_dot_id = dot_ids[replace_id + j]

                    # if this space is not directly adjacent, stop updating
                    if next_dot_id != dot_id + j:
                        break

                    empty_space_size[next_dot_id] -= file_size[e]

                    # remove from index if no space
                    if empty_space_size[next_dot_id] == 0:
                        dot_ids.pop(replace_id + j)

            # file block was written, so this block is now full
            dot_ids.pop(replace_id)
            break

    return calculate_checksum(reordered_map)


# start timer and run main code
start_time = time.perf_counter()
answer = get_answer()
execution_time_ms = (time.perf_counter() - start_time) * 1000

# output results
print(f"{script_path.parent.name} - {script_path.name}")
print(f"Timing: {execution_time_ms:.3f} ms")
print(f"Answer: {answer}")
