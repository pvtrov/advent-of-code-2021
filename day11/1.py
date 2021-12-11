input_file = open("../inputs/day11input.txt", "r")

input_array = []
f = list(input_file.readline())

while f:
    f.remove("\n")
    input_array.append(f)
    f = list(input_file.readline())

for i in range(len(input_array)):
    for j in range(len(input_array[i])):
        input_array[i][j] = int(input_array[i][j])

# print(input_array)


def short_adding(array, i, j):
    array[i][j] = adding_to_nine(array[i][j])
    if array[i][j] == 0:
        return adding_in_array(array, i, j)
    else:
        return array


def adding_to_nine(number):
    if number+1 == 10:
        return 0
    return number+1        # xwykle dodawanie tylko do 9 (10 zamienia sie na 0)


def adding_in_array(array, x, y):
    if x-1 != -1 and x != len(array)-1 and y != -1 and y != len(array)-1:
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if array[i][j] != 0:
                    short_adding(array, i, j)

    else:
        if x == 0 and y == 0:
            for i in range(x, x+2):
                for j in range(y, y+2):
                    if array[i][j] != 0:
                        short_adding(array, i, j)

        elif x == len(array)-1 and y == len(array)-1:
            for i in range(x-1, x+1):
                for j in range(y-1, y+1):
                    if array[i][j] != 0:
                        short_adding(array, i, j)

        elif x == 0 and y == len(array)-1:
            for i in range(x, x+2):
                for j in range(y-1, y+1):
                    if array[i][j] != 0:
                        short_adding(array, i, j)

        elif x == len(array)-1 and y == 0:
            for i in range(x-1, x+1):
                for j in range(y, y+2):
                    if array[i][j] != 0:
                        short_adding(array, i, j)

        elif x == 0:
            for i in range(x, x+2):
                for j in range(y-1, y+2):
                    if array[i][j] != 0:
                        short_adding(array, i, j)

        elif x == len(array)-1:
            for i in range(x-1, x+1):
                for j in range(y-1, y+2):
                    if array[i][j] != 0:
                        short_adding(array, i, j)

        elif y == 0:
            for i in range(x-1, x+2):
                for j in range(y, y+2):
                    if array[i][j] != 0:
                        short_adding(array, i, j)

        elif y == len(array)-1:
            for i in range(x-1, x+2):
                for j in range(y-1, y+1):
                    if array[i][j] != 0:
                        short_adding(array, i, j)

    return array


def checking_for_zeroes(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == 0:
                array = adding_in_array(array, i, j)
    return array


def octopus_flashes(array):
    flashes = [0 for _ in range(100)]

    for step in range(100):
        flash = 0
        for i in range(len(array)):
            for j in range(len(array[i])):
                array[i][j] = adding_to_nine(array[i][j])

        array = checking_for_zeroes(array)
        for i in range(len(array)):
            for j in range(len(array[i])):
                if array[i][j] == 0:
                    flash += 1

        flashes[step] = flash

    return sum(flashes)


print(octopus_flashes(input_array))

