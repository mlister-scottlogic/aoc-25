from support.timers import timeit
import string


def get_input(filename):
    text_file = open(filename, "r")
    all_lines = [l.strip() for l in text_file.readlines()]
    return [(l[0:-3], l[-3:]) for l in all_lines]


def calculate_seat_id(i):
    row = i[0]
    seat = i[1]

    binary_row = ["1" if c == "B" else "0" for c in row]
    binary_row_string = "".join(binary_row)
    row_number = int(binary_row_string, 2)

    binary_seat = ["1" if c == "R" else "0" for c in seat]
    binary_seat_string = "".join(binary_seat)
    seat_number = int(binary_seat_string, 2)

    seat_id = row_number * 8 + seat_number

    # print(i, row_number, seat_number, seat_id)
    return seat_id


@timeit
def part1(input_file):
    input = get_input(input_file)

    # print(input)

    seat_ids = [calculate_seat_id(i) for i in input]

    return max(seat_ids)


@timeit
def part2(input_file):
    input = get_input(input_file)

    seat_ids = [calculate_seat_id(i) for i in input]

    sorted_seat_ids = sorted(seat_ids)

    last = sorted_seat_ids[0]

    for i in sorted_seat_ids[1:]:
        if i - last > 1:
            print(i, last)
            return i - 1

        last = i

    return -1


print("Part 1")
# print(part1("day5/example.txt"))
# print(part1("day5/input.txt"))

# print("Part 2")
# print(part2("day5/example.txt"))
print(part2("day5/input.txt"))
