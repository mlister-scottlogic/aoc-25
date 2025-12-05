from typing import List
from support.timers import timeit


def get_input(filename) -> tuple[List[tuple[int, int]], List[int]]:
    text_file = open(filename, "r")
    all_lines = text_file.readlines()
    all_lines = [l.strip() for l in all_lines]

    space_index = all_lines.index("")

    ranges = [
        (int(r.split("-")[0]), int(r.split("-")[1])) for r in all_lines[0:space_index]
    ]

    ids = [int(id) for id in all_lines[space_index + 1 :]]

    return ranges, ids


@timeit
def part1(input_file: str):
    ranges, ids = get_input(input_file)

    total = 0

    for id in ids:
        for r in ranges:
            if id >= r[0] and id <= r[1]:
                total += 1
                # print(id)
                break

    return total


@timeit
def part2(input_file: str):
    ranges, _ = get_input(input_file)

    ranges2 = [dict(lower=r[0], upper=r[1]) for r in ranges]

    ranges2.sort(key=lambda r: r["lower"])

    # print(ranges2)

    changed = True

    while changed:
        # print("------ new iteration ------")
        changed = False

        for i in range(1, len(ranges2)):
            first_bound = ranges2[i - 1]
            second_bound = ranges2[i]

            if first_bound["upper"] >= second_bound["lower"]:
                if (
                    second_bound["upper"] < first_bound["upper"]
                    and first_bound != second_bound
                ):
                    second_bound["upper"] = first_bound["upper"]
                    second_bound["lower"] = first_bound["lower"]

                    changed = True
                elif first_bound != second_bound:
                    first_bound["upper"] = second_bound["upper"]
                    second_bound["lower"] = first_bound["lower"]

                    changed = True

        # Remove duplicates
        ranges_set = set([(r["lower"], r["upper"]) for r in ranges2])
        ranges2 = [dict(lower=r[0], upper=r[1]) for r in ranges_set]
        ranges2.sort(key=lambda r: r["lower"])

        # print(ranges2)

    total = 0
    ranges_set = set([(r["lower"], r["upper"]) for r in ranges2])

    # print(ranges_set)

    for r in ranges_set:
        total += (r[1] + 1) - r[0]

    return total


print("Part 1")
# print(part1("day5/example.txt"))
# print(part1("day5/input.txt"))

print("Part 2")
print(part2("day5/example.txt"))
print(part2("day5/input.txt"))
