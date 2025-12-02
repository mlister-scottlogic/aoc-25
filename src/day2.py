from support.timers import timeit


def get_input(filename):
    text_file = open(filename, "r")
    line = text_file.readline().strip()

    ranges = line.split(",")
    return [r.split("-") for r in ranges]


@timeit
def part1(input_file: str):
    input = get_input(input_file)
    print(input)

    count = 0

    return count


@timeit
def part2(input_file: str):
    count = 0
    return count


print("Part 1")
print(part1("day2/example.txt"))
print(part1("day2/input.txt"))

# print("Part 2")
# print(part2("day2/example.txt"))
# print(part2("day2/input.txt"))
