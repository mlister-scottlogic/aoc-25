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
    return int(all_lines[0]), [c for c in all_lines[1].split(",")]


@timeit
def part1(input_file):
    start_time, busses = get_input(input_file)

    active_busses = [int(c) for c in busses if c != "x"]

    time_after = [(b, b - (start_time % b)) for b in active_busses]

    minimum = min(time_after, key=lambda t: t[1])
    print(minimum)
    return minimum[0] * minimum[1]


@timeit
def part2(input_file):
    _, busses = get_input(input_file)

    target = [(busses.index(c), int(c)) for c in busses if c != "x"]
    target_times = [0 for c in target]

    # print(target)

    step_size = max([t for t in target if t], key=lambda t: t[1])
    current_t = step_size[1] - step_size[0]

    # print([b[1] - b[0] for b in target])

    # print(step_size)

    # found = False

    # current_t = 168
    # steps = 0

    # while not found:
    #     times = [(current_t + b[0]) % b[1] if b else None for b in target]
    #     print(current_t, step_size, times)
    #     if times == target_times:
    #         print("FOUND!")
    #         print(times, target_times)
    #         found = True
    #         print(current_t)
    #         break

    #     current_t += step_size[1]
    #     steps += 1

    #     if steps % 100_000 == 0:
    #         print(current_t)

    # ordered_targets = sorted(target, key=lambda t: t[1])
    step_size = target[0]
    # print("ordered_targets", ordered_targets)
    print("step size", step_size)
    current_t = 0
    current_t = step_size[1] - step_size[0]

    current_step_size = step_size[1]

    for i, (offset, bus_id) in enumerate(target[1:], 1):
        # print(offset, bus_id)
        # time = (current_t - offset) % bus_id
        # print(
        #     "current_t:",
        #     current_t,
        #     " offset:",
        #     offset,
        #     " bus_id:",
        #     bus_id,
        #     " step_size:",
        #     current_step_size,
        #     # " time:",
        #     # time,
        # )

        found = False

        while not found:
            times = [(current_t + b[0]) % b[1] if b else None for b in target[: i + 1]]
            # print("while loop", current_t, times)

            if all(v == 0 for v in times):
                found = True
                break

            current_t += current_step_size

        times = [(current_t + b[0]) % b[1] if b else None for b in target]
        # print("times after while", times)
        # current_t += current_step_size * time
        current_step_size = current_step_size * bus_id

    # print(
    #     "current_t:",
    #     current_t,
    #     " offset:",
    #     offset,
    #     " bus_id:",
    #     bus_id,
    #     " step_size:",
    #     current_step_size,
    #     # " time:",
    #     # time,
    # )

    times = [(current_t + b[0]) % b[1] if b else None for b in target]
    print(times)

    return current_t


# print("Part 1")
# print(part1("day13/example.txt"))
# print(part1("day13/input.txt"))

print("Part 2")
# print(part2("day13/example.txt"))
print(part2("day13/input.txt"))
