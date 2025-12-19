from support.timers import timeit
import string


def get_input(filename):
    text_file = open(filename, "r")
    all_lines = [l.strip() for l in text_file.readlines()]

    no_other_bags = []
    contains = {}

    for line in all_lines:
        if "bags contain no other bags." in line:
            no_other_bags.append(line.split("bags contain no other bags")[0].strip())
        else:
            splits = line.split("contain")
            key = splits[0][:-5].strip()

            values = splits[1][:-1].split(",")
            values = [v[:-4].strip() for v in values]

            values = [
                (v.split(" ")[0], v.split(" ")[1] + " " + v.split(" ")[2])
                for v in values
            ]

            contains[key] = values

    return no_other_bags, contains


@timeit
def part1(input_file):
    no_other_bags, contains = get_input(input_file)

    # print(no_other_bags, contains)

    total = 0

    for bag in contains.keys():
        if bag != "shiny gold":
            if traverse(bag, contains, no_other_bags):
                # print(bag)
                total += 1

    return total


def traverse(current_bag, contains, no_other_bags):
    if current_bag in no_other_bags:
        return False

    if current_bag == "shiny gold":
        return True

    # print(contains[current_bag])

    return any([traverse(b[1], contains, no_other_bags) for b in contains[current_bag]])


def traverse2(current_bag, contains, no_other_bags, num_bags):
    if current_bag in no_other_bags:
        # print(current_bag, num_bags)
        return 1 * num_bags

    # if current_bag == "shiny gold":
    #     return 0

    # bags_size = int(contains[current_bag])

    intermediate_sum = (
        sum(
            [
                num_bags * traverse2(b[1], contains, no_other_bags, int(b[0]))
                for b in contains[current_bag]
            ]
        )
        + num_bags
    )

    # print(current_bag, num_bags, contains[current_bag], intermediate_sum)

    return intermediate_sum


@timeit
def part2(input_file):
    no_other_bags, contains = get_input(input_file)

    # remove 1 for the shiny gold bag
    return traverse2("shiny gold", contains, no_other_bags, 1) - 1


print("Part 1")
# print(part1("day7/example.txt"))
# print(part1("day7/input.txt"))

print("Part 2")
print(part2("day7/example.txt"))
print(part2("day7/input.txt"))
