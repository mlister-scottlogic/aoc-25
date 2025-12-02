from support.timers import timeit
import math


def get_input(filename):
    text_file = open(filename, "r")
    line = text_file.readline().strip()

    ranges = line.split(",")
    return [r.split("-") for r in ranges]


@timeit
def part1(input_file: str):
    inputs = get_input(input_file)
    print(inputs)
    count = 0

    for input in inputs:
        # print(input)

        lower = int(input[0])
        higher = int(input[1])

        for j in range(lower, higher + 1):
            value_to_check = str(j)
            ## If odd number it can't be 2 repeating patterns
            if len(value_to_check) % 2 == 0:
                half_point = math.floor(len(value_to_check) / 2)
                # print(value_to_check)
                # print(half_point)

                first_part = value_to_check[0:half_point]
                second_part = value_to_check[half_point:]

                # print(first_part)
                # print(second_part)

                if first_part == second_part:
                    # print(first_part)
                    # print(second_part)
                    # print(value_to_check)
                    count += j

    return count


@timeit
def part2(input_file: str):
    count = 0
    return count


print("Part 1")
# print(part1("day2/example.txt"))
print(part1("day2/input.txt"))

# print("Part 2")
# print(part2("day2/example.txt"))
# print(part2("day2/input.txt"))
