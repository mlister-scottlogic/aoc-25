def get_input(filename):
    text_file = open(filename, "r")
    return text_file.readlines()

dial_history = []

dial = 50

dial_max = 100

dial_history.append(dial)

input = get_input("input1.txt")

for i in input: 
    if (i[0] == "L"):
        dial -= int(i[1:])
    if (i[0] == "R"):
        dial += int(i[1:])
    dial = dial % dial_max
    # print(i)
    # print(dial)
    dial_history.append(dial)

print("Answer:")
print(dial_history.count(0))


