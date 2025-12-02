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
    # print(inputs)
    count = 0

    for input in inputs:
        # print(input)

        lower = int(input[0])
        higher = int(input[1])

        for current_value in range(lower, higher + 1):
            value_to_check = str(current_value)
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
                    count += current_value

    return count


@timeit
def part2(input_file: str):
    count = 0

    inputs = get_input(input_file)
    # print(inputs)
    count = 0

    for input in inputs:
        # print(input)

        lower = int(input[0])
        higher = int(input[1])

        for current_value in range(lower, higher + 1):
            value_to_check = str(current_value)

            if len(value_to_check) > 1:
                for slice_size in range(1, len(value_to_check)):
                    # Only need to check if values neatly divide
                    if len(value_to_check) % slice_size == 0:
                        # print(f"------------{value_to_check}  {k}--------------")
                        values = [
                            value_to_check[l : l + slice_size]
                            for l in range(0, len(value_to_check), slice_size)
                        ]
                        unique_values = set(values)

                        # print(values)
                        # print(unique_values)

                        if len(unique_values) == 1:
                            # print(values)
                            # print(unique_values)
                            # print(current_value)
                            count += current_value
                            break
    return count


print("Part 1")
# print(part1("day2/example.txt"))
print(part1("day2/input.txt"))

print("Part 2")
# print(part2("day2/example.txt"))
print(part2("day2/input.txt"))
