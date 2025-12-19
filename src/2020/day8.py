import copy
from support.timers import timeit
import string


def get_input(filename):
    text_file = open(filename, "r")
    all_lines = [l.strip() for l in text_file.readlines()]

    instructions = [[*l.split(" ")] for l in all_lines]

    instructions = [
        [i[0], int(i[1][1:]) if i[1][0] == "+" else int(i[1])] for i in instructions
    ]

    return instructions


@timeit
def part1(input_file):
    input = get_input(input_file)

    executed_instructions = []
    accumulator = 0
    current_instruction_pointer = 0

    while current_instruction_pointer not in executed_instructions:
        executed_instructions.append(current_instruction_pointer)
        op, value = input[current_instruction_pointer]

        match op:
            case "nop":
                current_instruction_pointer += 1
            case "acc":
                accumulator += value
                current_instruction_pointer += 1
            case "jmp":
                current_instruction_pointer += value
    return accumulator


def has_infinite_loop(input):
    executed_instructions = []
    accumulator = 0
    current_instruction_pointer = 0

    while (
        current_instruction_pointer not in executed_instructions
        and current_instruction_pointer < len(input)
    ):
        executed_instructions.append(current_instruction_pointer)
        op, value = input[current_instruction_pointer]

        match op:
            case "nop":
                current_instruction_pointer += 1
            case "acc":
                accumulator += value
                current_instruction_pointer += 1
            case "jmp":
                current_instruction_pointer += value

    return current_instruction_pointer < len(input), accumulator


@timeit
def part2(input_file):
    input = get_input(input_file)

    for i, instruction in enumerate(input):
        # print(instruction)
        if instruction[0] != "acc":
            # print("swapping", instruction)
            new_list = copy.deepcopy(input)

            if instruction[0] == "nop":
                new_list[i][0] = "jmp"
            else:
                new_list[i][0] = "nop"

            has_loop, acc = has_infinite_loop(new_list)

            if not has_loop:
                return acc
    return -1


# print("Part 1")
# print(part1("day8/example.txt"))
# print(part1("day8/input.txt"))

print("Part 2")
# print(part2("day8/example.txt"))
print(part2("day8/input.txt"))
