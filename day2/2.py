f = open("../inputs/day2input.txt", "r")

array = [i[:-1] for i in f]
input_array = []

for i in range(len(array)):
    input_array.append(array[i].split())


def diving_again(input_array):
    depth = 0
    horizontal_position = 0
    aim = 0

    for i in input_array:
        if i[0] == "down":
            aim += int(i[1])
        elif i[0] == "up":
            aim -= int(i[1])
        elif i[0] == "forward":
            horizontal_position += int(i[1])
            depth += aim*int(i[1])

    return depth*horizontal_position


print(diving_again(input_array))
