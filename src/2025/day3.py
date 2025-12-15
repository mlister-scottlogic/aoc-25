from typing import List
from support.timers import timeit


def get_input(filename):
    text_file = open(filename, "r")
    all_lines = text_file.readlines()
    all_lines = [l.strip() for l in all_lines]

    return [[int(c) for c in l] for l in all_lines]


def joltage1(batteries: List[int]):
    if len(batteries) == 2:
        return (batteries[0], batteries[1])

    current_best = joltage1(batteries[1:])
    if batteries[0] >= current_best[0]:
        if current_best[0] > current_best[1]:
            return (batteries[0], current_best[0])
        else:
            return (batteries[0], current_best[1])

    return current_best


def joltage2(batteries: List[int], battery_size: int):
    if len(batteries) == battery_size:
        # print(batteries[:battery_size])
        return batteries

    current_best = joltage2(batteries[1:], battery_size)

    ## Turn off first thats less than batteries 0

    # print(f"--- {batteries[0]} --- {current_best} --- {batteries}")

    if batteries[0] >= current_best[0]:
        # First element where one on right is bigger or failing that the smallest

        best_element_to_remove = None
        # Needs to be bigger than something (should probably use none or something)
        last_element = 99

        for index, value in enumerate(current_best):
            if value > last_element:
                # last element is the one we want to remove
                best_element_to_remove = index - 1
                # print(
                #     best_element_to_remove,
                #     current_best,
                #     current_best[best_element_to_remove],
                # )
                break
            last_element = value
        else:
            if best_element_to_remove == None:
                # print("overriding last value")
                best_element_to_remove = current_best.index(min(current_best))
                # print(best_element_to_remove)

        current_best.pop(best_element_to_remove)
        # print("New value")
        # print(batteries[0], *current_best)
        return [batteries[0], *current_best]

    return current_best


def joltage3(batteries: List[int], battery_size):
    ## Find higest number with battery_size - 1 digits after it
    ## Repeat
    # print(batteries, battery_size)

    if battery_size == 1:
        return [max(batteries)]

    # Find highest digit with enough values after it
    new_battery_size = battery_size - 1
    best_digit = max(batteries[0 : (len(batteries) - new_battery_size)])

    index_of_best = batteries.index(best_digit)

    # print(best_digit, index_of_best)

    return [best_digit, *joltage3(batteries[index_of_best + 1 :], new_battery_size)]


@timeit
def part1(input_file: str):
    total = 0
    inputs = get_input(input_file)

    # print(inputs)

    for i in inputs:
        best_value = joltage3(i, 2)
        best_value_strings = [str(i) for i in best_value]
        jolt = int("".join(best_value_strings))
        # print(f"------ {i} --- {best_value} --- {jolt} ------")
        total += jolt

    return total


@timeit
def part2(input_file: str):
    # print(inputs)
    total = 0
    inputs = get_input(input_file)

    # print(inputs)

    for i in inputs:
        best_value = joltage3(i, 12)
        # print(best_value)
        best_value_strings = [str(i) for i in best_value]
        jolt = int("".join(best_value_strings))
        # print(f"------ {i} --- {best_value} --- {jolt} ------")
        total += jolt

        best_value2 = joltage2(i, 12)
        # print(best_value)
        best_value_strings2 = [str(i) for i in best_value2]
        jolt2 = int("".join(best_value_strings2))

        if jolt != jolt2:
            print(i, jolt, jolt2)

    return total


print("Part 1")
# print(part1("day3/example.txt"))
# print(part1("day3/input.txt"))

print("Part 2")
# print(part2("day3/example.txt"))
print(part2("day3/input.txt"))
