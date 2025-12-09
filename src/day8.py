from typing import List
from support.timers import timeit
import math


def get_input(filename):
    text_file = open(filename, "r")
    all_lines = text_file.readlines()

    parsed = [[int(x) for x in l.strip().split(",")] for l in all_lines]

    return [(c[0], c[1], c[2]) for c in parsed]


def distance(p1, p2):
    return math.sqrt(
        ((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2) + ((p1[2] - p2[2]) ** 2)
    )


@timeit
def part1(input_file: str, iterations):
    input = get_input(input_file)

    circuits = [set([i]) for i in input]

    minimums = dict()

    for p1 in input:
        minimum_for_point = [((p1, p2), distance(p1, p2)) for p2 in input if p1 != p2]
        # print(p1, minimum)
        for points, d in minimum_for_point:
            minimums[frozenset([*points])] = d

    for _ in range(iterations):
        overall_minimum = min(minimums.values())
        res = [k for k, v in minimums.items() if v == overall_minimum][0]

        # print(res)

        related_circuits = [s for s in circuits if len(s.intersection(res)) > 0]

        # If they aren't already connected merge the sets
        if len(related_circuits) > 1:
            # print(related_circuits)
            circuits.remove(related_circuits[0])
            related_circuits[1].update(related_circuits[0])

        # print(circuits, len(circuits))

        # remove element we just worked on
        minimums.pop(res)

    # print(circuits)
    circuit_lengths = [len(c) for c in circuits]
    circuit_lengths.sort(reverse=True)
    print(circuit_lengths)

    return circuit_lengths[0] * circuit_lengths[1] * circuit_lengths[2]


@timeit
def part2(input_file: str):
    input = get_input(input_file)

    circuits = [set([i]) for i in input]

    minimums = dict()

    for p1 in input:
        minimum_for_point = [((p1, p2), distance(p1, p2)) for p2 in input if p1 != p2]
        # print(p1, minimum)
        for points, d in minimum_for_point:
            minimums[frozenset([*points])] = d

    res = None

    while len(circuits) > 1:
        overall_minimum = min(minimums.values())
        res = [k for k, v in minimums.items() if v == overall_minimum][0]

        # print(res)

        related_circuits = [s for s in circuits if len(s.intersection(res)) > 0]

        # If they aren't already connected merge the sets
        if len(related_circuits) > 1:
            # print(related_circuits)
            circuits.remove(related_circuits[0])
            related_circuits[1].update(related_circuits[0])

        # print(circuits, len(circuits))

        # remove element we just worked on
        minimums.pop(res)

    print(res)
    total = 1

    for x in res:
        print(x)
        total = total * x[0]

    return total


print("Part 1")
# print(part1("day8/example.txt", 10))
# print(part1("day8/input.txt", 1000))

print("Part 2")
# print(part2("day8/example.txt"))
print(part2("day8/input.txt"))
