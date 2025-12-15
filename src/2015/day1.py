from support.timers import timeit
from collections import Counter


def get_input(filename):
    text_file = open(filename, "r")
    return text_file.readline().strip()


@timeit
def part1(input_file):
    input = get_input(input_file)

    counter = Counter(input)

    up = counter["("]
    down = counter[")"]

    return up - down


@timeit
def part2(input_file):
    input = get_input(input_file)

    currrent_position = 0

    for i, c in enumerate(input):
        match c:
            case "(":
                currrent_position += 1
            case ")":
                currrent_position -= 1

        if currrent_position == -1:
            return i + 1


print("Part 1")
print(part1("day1/input.txt"))

print("Part 2")
print(part2("day1/input.txt"))
