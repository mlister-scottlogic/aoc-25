import copy
from functools import cache
from math import prod
from support.timers import timeit
import string
from itertools import combinations
from collections import defaultdict


def get_input(filename):
    text_file = open(filename, "r")
    line = text_file.readline().strip().split(",")
    return [int(c) for c in line]


@timeit
def part1(input_file, target_turn):
    input = get_input(input_file)

    spoken = {}

    # print(input)

    # last_spoken = input[-1]

    to_speak = input[-1]

    for i in range(1, target_turn + 1):
        if i % 10_000 == 0:
            print("turn", i)

        if i - 1 < len(input):
            to_speak = input[i - 1]
            spoken[to_speak] = [i]
        else:
            when_last_spoken = spoken[to_speak]
            # print(i, spoken, to_speak, when_last_spoken)

            if len(when_last_spoken) < 2:
                to_speak = 0

                already_spoken = spoken.get(to_speak, None)

                if already_spoken:
                    already_spoken.append(i)
                    spoken[to_speak] = already_spoken[-3:]
                else:
                    spoken[to_speak] = [i]
            else:
                to_speak = (i - 1) - when_last_spoken[-2]
                # print(i, "to speak", to_speak)
                already_spoken = spoken.get(to_speak, None)

                if already_spoken:
                    already_spoken.append(i)
                    spoken[to_speak] = already_spoken[-3:]
                else:
                    spoken[to_speak] = [i]

                # if already_spoken:
                # else:
                #     spoken[to_speak] = already_spoken.apend(i)

        # print("turn:", i, to_speak)

    return to_speak


@timeit
def part2(input_file):
    input = get_input(input_file)

    return -1


# print("Part 1")
# print(part1("day15/example.txt", 2020))
# print(part1("day15/input.txt", 2020))

print("Part 2")
# print(part1("day15/example.txt", 30000000))
print(part1("day15/input.txt", 30000000))
