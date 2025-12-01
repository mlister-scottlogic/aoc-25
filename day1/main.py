def get_input(filename):
    text_file = open(filename, "r")
    return text_file.readlines()

dial_history = []

dial = 50

dial_max = 100

dial_0s = 0

dial_history.append(dial)

# input = get_input("example.txt")
input = get_input("input.txt")

for i in input: 
    if (i[0] == "L"):
        old_dial = dial
        dial -= int(i[1:])

        absv = abs(dial // dial_max)
        dial = dial % dial_max

        if (dial == 0):
            dial_0s += 1

        if (old_dial == 0 and absv > 0):
            dial_0s += absv -1
        else:
            dial_0s += absv
            
    if (i[0] == "R"):
        dial += int(i[1:])
        dial_0s += abs(dial // dial_max)
        dial = dial % dial_max

    print(i.strip())
    print("dial ", dial)
    print("times 0 ", dial_0s)
    dial_history.append(dial)

print("Answer:")
print(dial_0s)


