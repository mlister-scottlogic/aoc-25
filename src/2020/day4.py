from support.timers import timeit
import string


def get_input(filename):
    text_file = open(filename, "r")
    all_lines = [l.strip() for l in text_file.readlines()]

    passports = []
    current_passport = {}
    for l in all_lines:
        if not l:
            passports.append(current_passport)
            current_passport = {}
        else:
            values = l.split(" ")

            for pair in values:
                kv = pair.split(":")
                # print(kv)
                k = kv[0]
                v = kv[1]

                current_passport[k] = v

    if current_passport != {}:
        passports.append(current_passport)

    return passports


@timeit
def part1(input_file):
    input = get_input(input_file)
    valid_passports = 0

    print("Input length", len(input))

    expected_keys = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])

    for passport in input:
        keys = set(passport.keys())

        if expected_keys.issubset(keys):

            valid_passports += 1

    return valid_passports


@timeit
def part2(input_file):
    input = get_input(input_file)
    valid_passports = 0

    print("Input length", len(input))

    expected_keys = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
    valid_eye_colour = set(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])

    for passport in input:
        keys = set(passport.keys())

        if expected_keys.issubset(keys):
            byr = int(passport["byr"])
            if byr < 1920 or byr > 2002:
                continue

            iyr = int(passport["iyr"])
            if iyr < 2010 or iyr > 2020:
                continue

            eyr = int(passport["eyr"])
            if eyr < 2020 or eyr > 2030:
                continue

            hgt = passport["hgt"]
            unit = hgt[-2:]

            match unit:
                case "cm":
                    hgt_value = int(hgt[0:-2])
                    if hgt_value < 150 or hgt_value > 193:
                        continue
                case "in":
                    hgt_value = int(hgt[0:-2])

                    if hgt_value < 59 or hgt_value > 76:
                        continue
                case _:
                    # print("***PANIC***", unit, hgt)
                    continue

            hcl = passport["hcl"]
            if hcl[0] != "#":
                continue
            all_hex = all([c in string.hexdigits for c in hcl[1:]])
            if not all_hex:
                continue

            ecl = passport["ecl"]
            if not ecl in valid_eye_colour:
                continue

            pid = passport["pid"]
            if len(pid) != 9:
                continue
            all_digits = all([c in string.digits for c in pid])
            if not all_digits:
                continue

            valid_passports += 1

    return valid_passports


# print("Part 1")
# print(part1("day4/example.txt"))
# print(part1("day4/input.txt"))

print("Part 2")
print(part2("day4/example.txt"))
print(part2("day4/input.txt"))
