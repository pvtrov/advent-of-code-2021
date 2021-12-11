input_file = open("../inputs/day8input.txt", "r")

input_array = []
f = input_file.readline().split()

while f:
    input_array.append(f)
    f = input_file.readline().split()

print(input_array)


def easy_didgits(array):
    result = 0
    for i in range(len(array)):
        for j in range(11, 15):
            length = len(array[i][j])
            if length == 2 or length == 4 or length == 3 or length == 7:
                result += 1

    return result


print(easy_didgits(input_array))