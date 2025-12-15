from typing import List
from support.timers import timeit

from sortedcontainers import SortedSet


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


class IdRange:
    def __init__(self, lower, upper):
        if upper < lower:
            raise ValueError

        self.lower = lower
        self.upper = upper

    def __repr__(self) -> str:
        return f"({self.lower},{self.upper})"

    def __eq__(self, other):
        if not isinstance(other, IdRange):
            return NotImplemented
        return self.lower == other.lower and self.upper == other.upper

    def __hash__(self):
        return hash(self.__repr__())

    def __lt__(self, other):
        return self.lower < other.lower


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
def part2(ranges: List[tuple[int, int]]):
    ranges2 = SortedSet([IdRange(r[0], r[1]) for r in ranges])

    changed = True

    while changed:
        changed = False

        for i in range(1, len(ranges2)):
            first_bound = ranges2[i - 1]
            second_bound = ranges2[i]

            if first_bound.upper >= second_bound.lower:
                if (
                    second_bound.upper < first_bound.upper
                    and first_bound != second_bound
                ):
                    ranges2.pop(i)

                    changed = True

                    break
                elif first_bound != second_bound:
                    ranges2.remove(first_bound)
                    ranges2.remove(second_bound)
                    ranges2.add(IdRange(first_bound.lower, second_bound.upper))

                    changed = True
                    break

    total = 0

    for r in ranges2:
        total += (r.upper + 1) - r.lower

    return total


print("Part 1")
# print(part1("day5/example.txt"))
# print(part1("day5/input.txt"))

print("Part 2")
ranges, _ = get_input("day5/input.txt")

# print(part2("day5/example.txt"))
print(part2(ranges))
