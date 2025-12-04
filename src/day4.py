from typing import List
from support.timers import timeit


def get_input(filename) -> dict[tuple[int, int], int]:
    text_file = open(filename, "r")
    all_lines = text_file.readlines()
    all_lines = [l.strip() for l in all_lines]

    roll_map = {}
    for y, line in enumerate(all_lines):
        for x, field in enumerate(line):
            roll_map[(x, y)] = 1 if field == "@" else 0

    return roll_map


@timeit
def part1(input_file: str):
    inputs = get_input(input_file)

    total, new_map = calculate_rolls_removed(inputs)

    return total


def calculate_rolls_removed(
    input_map: dict[tuple[int, int], int],
) -> tuple[int, dict[tuple[int, int], int]]:
    rolls_points = {}

    for point in input_map:
        # For all rolls
        if input_map[point]:
            nearby_rolls = 0
            (x, y) = point
            for x_delta in range(-1, 2):
                for y_delta in range(-1, 2):
                    # ignore 0,0
                    if not (x_delta == 0 and y_delta == 0):
                        point_to_check = (x + x_delta, y + y_delta)

                        roll_to_check = input_map.get(point_to_check, 0)

                        nearby_rolls += roll_to_check
            rolls_points[point] = nearby_rolls

    total = 0

    for point in rolls_points:
        if rolls_points[point] < 4:
            total += 1
            input_map[point] = 0

    return total, input_map


@timeit
def part2(input_file: str):
    total = 0
    inputs = get_input(input_file)

    rolls_removed = None

    while rolls_removed != 0:
        rolls_removed, inputs = calculate_rolls_removed(inputs)
        total += rolls_removed

    return total


print("Part 1")
# print(part1("day4/example.txt"))
print(part1("day4/input.txt"))

print("Part 2")
# print(part2("day4/example.txt"))
print(part2("day4/input.txt"))
