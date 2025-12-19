from support.timers import timeit
import string


def get_input(filename):
    text_file = open(filename, "r")
    all_lines = [l.strip() for l in text_file.readlines()]

    groups = []
    current_group = []
    for l in all_lines:
        if l:
            current_group.append(set([c for c in l]))
        else:
            groups.append(current_group)
            current_group = []

    if current_group:
        groups.append(current_group)

    return groups


@timeit
def part1(input_file):
    input = get_input(input_file)

    totals = [len(set.union(*i)) for i in input]

    return sum(totals)


@timeit
def part2(input_file):
    input = get_input(input_file)

    totals = [len(set.intersection(*i)) for i in input]

    return sum(totals)


# print("Part 1")
# print(part1("day6/example.txt"))
# print(part1("day6/input.txt"))

print("Part 2")
print(part2("day6/example.txt"))
print(part2("day6/input.txt"))
