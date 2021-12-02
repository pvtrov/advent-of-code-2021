f = open("../inputs/day2input.txt", "r")

array = [i[:-1] for i in f]
input_array = []

for i in range(len(array)):
    input_array.append(array[i].split())


def diving(input_array):
    depth = 0
    horizontal_position = 0

    for i in range(len(input_array)):
        if input_array[i][0] == "forward":
            horizontal_position += int(input_array[i][1])

        elif input_array[i][0] == "up":
            depth -= int(input_array[i][1])

        elif input_array[i][0] == "down":
            depth += int(input_array[i][1])


    result = horizontal_position*depth
    return result


print(diving(input_array))