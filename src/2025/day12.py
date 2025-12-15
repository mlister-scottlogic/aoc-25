from typing import List
from support.timers import timeit
from functools import cache

from collections import defaultdict

from itertools import combinations
from functools import reduce
import numpy as np


def get_input(filename):
    text_file = open(filename, "r")
    all_lines = text_file.readlines()

    shapes = []

    current_shape = []

    for i, line in enumerate(all_lines[:30]):
        if i % 5 != 0 and i % 5 != 4:
            row = [1 if c == "#" else 0 for c in line.strip()]
            current_shape.append(row)

        if i % 5 == 4:
            shapes.append(np.array(current_shape, dtype=np.int8))
            current_shape = []

    space_sizes = []

    for i, line in enumerate(all_lines[30:]):
        present_counter = defaultdict(int)

        parts = line.split(":")

        space_size = tuple([int(s) for s in parts[0].split("x")])

        counts = [int(s) for s in parts[1].strip().split(" ")]

        for i, c in enumerate(counts):
            present_counter[i] = c

        space_sizes.append((space_size, present_counter))

    return shapes, space_sizes


# Source - https://stackoverflow.com/a
# Posted by MSeifert, modified by community. See post 'Timeline' for change history
# Retrieved 2025-12-12, License - CC BY-SA 3.0
def pad(array, reference, offsets):
    """
    array: Array to be padded
    reference: Reference array with the desired shape
    offsets: list of offsets (number of elements must be equal to the dimension of the array)
    """
    # Create an array of zeros with the reference shape
    result = np.zeros(reference.shape)
    # Create a list of slices from offset to offset + shape in each dimension
    insertHere = [
        slice(offsets[dim], offsets[dim] + array.shape[dim])
        for dim in range(array.ndim)
    ]
    # Insert the array in the result at the specified offsets
    result[insertHere] = array
    return result


@timeit
def part1(input_file: str):
    total = 0
    input = get_input(input_file)

    shapes, present_areas = input

    # print(shapes)

    rotated_shapes = {}

    for index, s in enumerate(shapes):
        rotated = [s]

        for i in range(1, 4):
            new_copy = np.copy(s)
            rotated_array = np.rot90(new_copy, k=i)
            matched_rotation = any([np.array_equal(e, rotated_array) for e in rotated])
            if not matched_rotation:
                rotated.append(rotated_array)

        rotated_shapes[index] = rotated

    max_shape_size = [np.sum(rotated_shapes[k][0]) for k in rotated_shapes.keys()]
    max_shape_size[5] += 1  # No way to fill this shape

    for present_area in present_areas:
        # print(present_area)
        size = present_area[0]
        required_presents = present_area[1]

        total_area = size[0] * size[1]

        present_size = sum(
            [max_shape_size[k] * required_presents[k] for k in required_presents.keys()]
        )

        # print(total_area, present_size)

        if present_size < total_area:
            total += 1

        # print(total_area, present_size)
    return total


@timeit
def part2(input_file: str):
    input = get_input(input_file)
    print(input)

    return 0


print("Part 1")
# print(part1("day12/example.txt"))
print(part1("day12/input.txt"))

print("Part 2")
# print(part2("day12/example2.txt"))
# print(part2("day12/input.txt"))
