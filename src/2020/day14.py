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

    all_lines = [l.split(" = ") for l in all_lines]

    # all_lines = [
    #     [["mem", p.split("[")[1].split("]")[0]] if "[" in p else p for p in l]
    #     for l in all_lines
    # ]

    new_list = []

    for l in all_lines:
        if "[" in l[0]:
            mem_val = l[0].split("[")[1].split("]")[0]
            new_list.append(("mem", int(mem_val), int(l[1])))
        else:
            ones_mask = int("".join(["1" if c == "1" else "0" for c in l[1]]), 2)
            zeroes_mask = int("".join(["0" if c == "0" else "1" for c in l[1]]), 2)
            new_list.append(("mask", ones_mask, zeroes_mask, l[1]))

    return new_list


@timeit
def part1(input_file):
    input = get_input(input_file)

    mem_addresses = {}
    current_mask = (0, 0)

    for i in input:
        op = i[0]
        match op:
            case "mask":
                current_mask = (i[1], i[2])
                print(current_mask)
            case "mem":
                mem_address = i[1]
                value = i[2]
                masked_value = (value | current_mask[0]) & current_mask[1]
                mem_addresses[mem_address] = masked_value

    print(mem_addresses)

    print(any([v for v in mem_addresses.values() if v > 68719476736]))

    return sum(mem_addresses.values())


@timeit
def part2(input_file):
    input = get_input(input_file)

    mem_addresses = {}

    # current_masks = []
    current_mask = (0, 0)
    current_mask_str = ""

    for i in input:
        op = i[0]
        match op:
            case "mask":
                # current_masks = create_masks([i[3]])
                current_mask = (i[1], i[2])
                current_mask_str = i[3]
                # print("current mask", current_mask, current_mask_str)
            case "mem":
                mem_address = i[1]
                value = i[2]

                masked_mem_address = mem_address | current_mask[0]

                mem_address_masked_str = "{0:036b}".format(masked_mem_address)
                # print(current_mask_str)
                # print(mem_address_masked_str)

                zipped = zip(current_mask_str, mem_address_masked_str)

                replace_x = "".join(["X" if c[0] == "X" else c[1] for c in zipped])
                # print(replace_x)
                addresses = create_floating([replace_x])

                for a in addresses:
                    mem_addresses[a] = value

                # print(masked_value_str)

                # mem_addresses[mem_address] = masked_values
                # masked_value = (value | current_mask[0]) & current_mask[1]
                # mem_addresses[mem_address] = masked_value

    # print(mem_addresses)
    return sum(mem_addresses.values())


def create_floating(masks):
    # print(masks)

    masks_with_xs = [mask for mask in masks if "X" in mask]

    if masks_with_xs:
        for mask in masks_with_xs:
            ones_version = mask.replace("X", "1", 1)
            zeros_version = mask.replace("X", "0", 1)
            masks.remove(mask)

            return create_floating([*masks, ones_version, zeros_version])

    # print("Created masks", masks)
    return [int(mask, 2) for mask in masks]


print("Part 1")
# print(part1("day14/example.txt"))
# print(part1("day14/input.txt"))

print("Part 2")
print(part2("day14/example.txt"))
print(part2("day14/input.txt"))
