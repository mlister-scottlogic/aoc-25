from typing import List
from support.timers import timeit

from collections import defaultdict


def get_input(filename):
    text_file = open(filename, "r")
    all_lines = text_file.readlines()

    return [
        (int(r.strip().split(",")[0]), int(r.strip().split(",")[1])) for r in all_lines
    ]


def rect_size(p1, p2):
    return (max(p1[0], p2[0]) - min(p1[0], p2[0]) + 1) * (
        max(p1[1], p2[1]) - min(p1[1], p2[1]) + 1
    )


@timeit
def part1(input_file: str):
    total = 0
    inputs = get_input(input_file)

    areas = dict()

    for p1 in inputs:
        size = [((p1, p2), rect_size(p1, p2)) for p2 in inputs if p1 != p2]
        # print(p1, minimum)
        for points, d in size:
            areas[frozenset([*points])] = d

    return max(areas.values())


def points_in_bounds(p1, p2, inputs):
    min_x = min(p1[0], p2[0])
    min_y = min(p1[1], p2[1])

    max_x = max(p1[0], p2[0])
    max_y = max(p1[1], p2[1])

    in_bounds = [
        i
        for i in inputs
        if i[0] > min_x and i[0] < max_x and i[1] > min_y and i[1] < max_y
    ]

    # print(p1, p2, in_bounds)

    return len(in_bounds) > 0


def point_on_line(p, line):
    p1, p2 = line

    if p1[0] == p2[0]:
        return p[0] == p1[0] and p[1] >= min(p1[1], p2[1]) and p[1] <= max(p1[1], p2[1])
    else:
        return p[1] == p1[1] and p[0] >= min(p1[0], p2[0]) and p[0] <= max(p1[0], p2[0])


def corners_in_bound(p1, p2, inputs):
    corner2 = (p1[0], p2[1])
    corner3 = (p2[0], p1[1])

    corners_to_check = set([corner2, corner3])

    for c in corners_to_check:
        crossings = 0

        for i in range(len(inputs)):
            x1 = inputs[i][0]
            y1 = inputs[i][1]

            j = inputs[(i + 1) % len(inputs)]
            x2 = j[0]
            y2 = j[1]

            # print(c, i, j, x1, y1, x2, y2)

            if y1 < c[1] < y2 and (c[0] - x1) * (y2 - y1) < (x2 - x1) * (c[1] - y1):
                crossings += 1

        if crossings % 2 != 1:
            return False

    # print("corners in bounds")
    return True


def print_input(inputs):
    for y in range(10):
        line = ""
        for x in range(15):
            line += "X" if (x + 1, y + 1) in inputs else "."
        print(line)


def create_greenlines(inputs):
    pairs = []
    for index, element in enumerate(inputs):
        if index + 1 < len(inputs):
            pairs.append((element, inputs[index + 1]))
        else:
            # Cope with wrap around
            pairs.append((element, inputs[0]))
    return pairs


@timeit
def part2(input_file: str):
    inputs = get_input(input_file)

    print_input(inputs)

    inputs_set = set(inputs)
    greenlines = create_greenlines(inputs)

    areas = dict()

    for p1 in inputs:
        size = [
            ((p1, p2), rect_size(p1, p2))
            for p2 in inputs
            if p1 != p2
            and not points_in_bounds(p1, p2, inputs)
            and corners_in_bound(p1, p2, inputs)
        ]
        # print(p1, minimum)
        for points, d in size:
            areas[frozenset([*points])] = d

    m = max(areas.values())
    res = [k for k, v in areas.items() if v == m][0]
    print(res)
    return m


print("Part 1")
# print(part1("day9/example.txt"))
# print(part1("day9/input.txt"))

print("Part 2")
print(part2("day9/example2.txt"))
# print(part2("day9/input.txt"))
