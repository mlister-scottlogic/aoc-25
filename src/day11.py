from typing import List
from support.timers import timeit
from functools import cache

from collections import defaultdict

from itertools import combinations
from functools import reduce


class hashabledict(dict):
    def __key(self):
        return tuple((k, self[k]) for k in sorted(self))

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        return self.__key() == other.__key()


def get_input(filename) -> dict[str, List[str]]:
    text_file = open(filename, "r")
    all_lines = text_file.readlines()

    new_lines = {}

    for line in all_lines:
        split_line = line.strip().split(":")

        start = split_line[0]

        outputs = split_line[1].strip().split(" ")

        new_lines[start] = frozenset(outputs)

    return new_lines


def number_of_paths(node: str, all_nodes):
    if node == "out":
        return 1

    return sum([number_of_paths(n, all_nodes) for n in all_nodes[node]])


@timeit
def part1(input_file: str):
    input = get_input(input_file)

    return number_of_paths2("you", "out", hashabledict(input))


@cache
def number_of_paths2(node: str, target_node: str, all_nodes):
    if node == target_node:
        return 1

    if node == "out":
        return 0

    return sum([number_of_paths2(n, target_node, all_nodes) for n in all_nodes[node]])


@timeit
def part2(input_file: str):
    input = get_input(input_file)

    hashable_inputs = hashabledict(input)

    svr_fft = number_of_paths2("svr", "fft", hashable_inputs)
    svr_dac = number_of_paths2("svr", "dac", hashable_inputs)

    fft_dac = number_of_paths2("fft", "dac", hashable_inputs)
    dac_fft = number_of_paths2("dac", "fft", hashable_inputs)

    fft_out = number_of_paths2("fft", "out", hashable_inputs)
    dac_out = number_of_paths2("dac", "out", hashable_inputs)

    print("outputs")
    svr_fft_dac_out = svr_fft * fft_dac * dac_out
    print("svr_fft_dac_out", svr_fft_dac_out)

    svr_dac_fft_out = svr_dac * dac_fft * fft_out
    print("svr_dac_fft_out", svr_dac_fft_out)

    return svr_fft_dac_out + svr_dac_fft_out


print("Part 1")
# print(part1("day11/example.txt"))
# print(part1("day11/input.txt"))

print("Part 2")
print(part2("day11/example2.txt"))
print(part2("day11/input.txt"))
