from functools import cache
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


@cache
def point_on_line(p, line):
    p1, p2 = line

    if p1[0] == p2[0]:
        return p[0] == p1[0] and p[1] >= min(p1[1], p2[1]) and p[1] <= max(p1[1], p2[1])
    else:
        return p[1] == p1[1] and p[0] >= min(p1[0], p2[0]) and p[0] <= max(p1[0], p2[0])


@cache
def does_intersect(p, line):
    x, y = p
    p1, p2 = line
    x1, y1 = p1
    x2, y2 = p2

    # Ignore lines that fully intersect
    if y == y1 == y2:
        # print(x, y, x1, x2, y1, y2)
        return False

    return x <= min(x1, x2) and y >= min(y1, y2) and y <= max(y1, y2)


@cache
def on_line(p, line):
    x, y = p
    p1, p2 = line
    x1, y1 = p1
    x2, y2 = p2

    # Vertical line
    if x == x1 and x1 == x2 and y >= min(y1, y2) and y <= max(y1, y2):
        return True

    if y == y1 and y1 == y2 and x >= min(x1, x2) and x <= max(x1, x2):
        return True

    return False


def all_points_in_bounds(p1, p2, greenlines, inputs):
    min_x = min(p1[0], p2[0])
    min_y = min(p1[1], p2[1])

    max_x = max(p1[0], p2[0])
    max_y = max(p1[1], p2[1])

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            crossings = 0

            # if its a corner then we don't need to check anything
            if (x, y) not in inputs:
                if not any([on_line((x, y), l) for l in greenlines]):
                    c_lines = [does_intersect((x, y), l) for l in greenlines]
                    crossings = sum([1 if l else 0 for l in c_lines])

                    if crossings % 2 == 0:
                        print(x, y)
                        return False

    return True


def corners_in_bound(p1, p2, greenlines, inputs):
    middle = ((p1[0] + p2[0]) // 2, (p1[1] + p2[1]) // 2)

    corner2 = (p1[0], p2[1])
    corner3 = (p2[0], p1[1])

    corners_to_check = set([corner2, corner3])

    # if p1 == (2, 3) and p2 == (9, 7):
    #     print(corners_to_check)

    for c in corners_to_check:
        crossings = 0

        # if its a corner then we don't need to check anything
        if c not in inputs:
            if not any([on_line(c, l) for l in greenlines]):

                c_lines = [does_intersect(c, l) for l in greenlines]
                crossings = sum([1 if l else 0 for l in c_lines])

                # if p1 == (2, 3) and p2 == (9, 7):
                #     print(c, crossings)

                # print(crossings)

                if crossings % 2 == 0:
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
            # and not points_in_bounds(p1, p2, inputs)
            and corners_in_bound(p1, p2, greenlines, inputs_set)
        ]
        # print(p1, minimum)
        for points, d in size:
            areas[frozenset([*points])] = d

    all_green = False
    m = None

    while not all_green and len(areas) > 0:

        m = max(areas.values())
        res = [k for k, v in areas.items() if v == m][0]

        list_res = list(res)

        all_green = all_points_in_bounds(
            list_res[0], list_res[1], greenlines, inputs_set
        )

        print(res, m, all_green, len(areas))

        areas.pop(res)

    return m


print("Part 1")
# print(part1("day9/example.txt"))
# print(part1("day9/input.txt"))

print("Part 2")
print(part2("day9/example.txt"))
print(part2("day9/example2.txt"))
print(part2("day9/input.txt"))
