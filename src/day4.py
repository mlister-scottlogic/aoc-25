from typing import List
from support.timers import timeit


def get_input(filename) -> dict[tuple[int, int], bool]:
    text_file = open(filename, "r")
    all_lines = text_file.readlines()
    all_lines = [l.strip() for l in all_lines]

    roll_map = {}
    for y, line in enumerate(all_lines):
        for x, field in enumerate(line):
            roll_map[(x, y)] = field == "@"

    return roll_map


@timeit
def part1(input_file: str):
    total = 0
    inputs = get_input(input_file)

    rolls_points = {}

    for point in inputs:
        # For all rolls
        if inputs[point]:
            nearby_rolls = 0
            for x in range(-1, 2):
                for y in range(-1, 2):
                    # ignore 0,0
                    if not (x == 0 and y == 0):
                        point_to_check = (point[0] + y, point[1] + x)

                        roll_to_check = inputs.get(point_to_check, None)

                        if roll_to_check is not None and roll_to_check:
                            nearby_rolls += 1
            rolls_points[point] = nearby_rolls

    # print(rolls_points)

    for point in rolls_points:
        if rolls_points[point] < 4:
            total += 1

    return total


@timeit
def part2(input_file: str):
    total = 0
    inputs = get_input(input_file)

    return total


print("Part 1")
print(part1("day4/example.txt"))
print(part1("day4/input.txt"))

print("Part 2")
# print(part2("day4/example.txt"))
# print(part2("day4/input.txt"))
