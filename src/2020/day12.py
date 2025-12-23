import copy
from functools import cache
from math import prod
from support.timers import timeit
import string
from itertools import combinations
from collections import defaultdict


def get_input(filename):
    text_file = open(filename, "r")
    all_lines = [l.strip() for l in text_file.readlines()]
    return [(l[0], int(l[1:])) for l in all_lines]


@timeit
def part1(input_file):
    inputs = get_input(input_file)

    current_direction = 90
    position = (0, 0)

    for direction, value in inputs:
        # print(
        #     "Current:", position, current_direction, " edit to make", direction, value
        # )

        normalised_direction = direction
        if direction == "F":
            match current_direction:
                case 0:
                    normalised_direction = "N"
                case 90:
                    normalised_direction = "E"
                case 180:
                    normalised_direction = "S"
                case 270:
                    normalised_direction = "W"

        match normalised_direction:
            case "N":
                position = (position[0], position[1] + value)
            case "S":
                position = (position[0], position[1] - value)
            case "E":
                position = (position[0] + value, position[1])
            case "W":
                position = (position[0] - value, position[1])
            case "R":
                current_direction = (current_direction + value) % 360
            case "L":
                current_direction = (current_direction - value) % 360

    print(position)

    return abs(position[0]) + abs(position[1])


@timeit
def part2(input_file):
    inputs = get_input(input_file)

    position = (0, 0)
    waypoint = (10, 1)

    for direction, value in inputs:
        # print("Current:", position, waypoint, " edit to make", direction, value)

        match direction:
            case "N":
                waypoint = (waypoint[0], waypoint[1] + value)
            case "S":
                waypoint = (waypoint[0], waypoint[1] - value)
            case "E":
                waypoint = (waypoint[0] + value, waypoint[1])
            case "W":
                waypoint = (waypoint[0] - value, waypoint[1])

            case "R":
                waypoint_degrees = value % 360
                waypoint = rotate_waypoint(waypoint, waypoint_degrees)
            case "L":
                waypoint_degrees = -value % 360
                waypoint = rotate_waypoint(waypoint, waypoint_degrees)

            case "F":
                delta = (waypoint[0] * value, waypoint[1] * value)
                position = (position[0] + delta[0], position[1] + delta[1])

    print(position)

    return abs(position[0]) + abs(position[1])


def rotate_waypoint(waypoint, degrees):
    match degrees:
        case 0:
            print("Shouldn't happen!", degrees)
            return waypoint
        case 90:
            return (waypoint[1], -waypoint[0])
        case 180:
            return (-waypoint[0], -waypoint[1])
        case 270:
            return (-waypoint[1], waypoint[0])
        case 360:
            print("Shouldn't happen!", degrees)
            return waypoint
        case _:
            print("Shouldn't happen!", degrees)
            return waypoint


print("Part 1")
# print(part1("day12/example.txt"))
# print(part1("day12/input.txt"))

print("Part 2")
print(part2("day12/example.txt"))
print(part2("day12/input.txt"))
