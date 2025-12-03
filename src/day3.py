from support.timers import timeit


def get_input(filename):
    text_file = open(filename, "r")
    return text_file.readlines()


@timeit
def part1(input_file: str):
    inputs = get_input(input_file)


@timeit
def part2(input_file: str):
    inputs = get_input(input_file)
    # print(inputs)
    count = 0


print("Part 1")
# print(part1("day3/example.txt"))
# print(part1("day3/input.txt"))

print("Part 2")
# print(part2("day3/example.txt"))
# print(part2("day3/input.txt"))
