input_file = open("../inputs/day9input.txt", "r")

input_array = []
f = list(input_file.readline())

while f:
    f.remove("\n")
    input_array.append(f)
    f = list(input_file.readline())

for x in range(len(input_array)):
    for y in range(len(input_array)):
        input_array[x][y] = int(input_array[x][y])


def adding_on_boundary(array, i, j):
    x = array[i][j]
    if i == 0 and j != 0:
        if x < array[i + 1][j] and x < array[i][j - 1] and x < array[i][j + 1]:
            return x + 1
        else:
            return 0
    elif i == 0 and j == 0:
        if x < array[i][j + 1] and x < array[i + 1][j]:
            return x + 1
        else:
            return 0
    elif j == 0 and i != 0:
        if x < array[i][j + 1] and x < array[i-1][j] and x < array[i + 1][j]:
            return x + 1
        else:
            return 0
    elif i == len(array) - 1 and j == 0:
        if x < array[i - 1][j] and x < array[i][j + 1]:
            return x + 1
        else:
            return 0
    elif i == len(array) - 1 and j != len(array[i]) - 1:
        if x < array[i - 1][j] and x < array[i][j - 1] and x < array[i][j + 1]:
            return x + 1
        else:
            return 0
    elif i == len(array) - 1 and j == len(array[i]) - 1:
        if x < array[i - 1][j] and x < array[i][j - 1]:
            return x + 1
        else:
            return 0
    elif i != len(array) - 1 and j == len(array[i]) - 1:
        if x < array[i][j - 1] and x < array[i - 1][j] and x < array[i + 1][j]:
            return x + 1
        else:
            return 0
    elif i == 0 and j == len(array[i]) - 1:
        if x < array[i][j - 1] and x < array[i + 1][j]:
            return x + 1
        else:
            return 0
    else:
        return 0


def smoke_basin(array):
    result = 0
    neighbour_table = [[0, 1], [1, 0], [-1, 0], [0, -1]] #gora, lewo, dol, prawo

    for i in range(len(array)):
        for j in range(len(array[i])):
            if i == 0 or i == len(array)-1 or j == 0 or j == len(array[i])-1:
                result += adding_on_boundary(array, i, j)

            else:
                if array[i][j] < array[i][j+1] and array[i][j] < array[i+1][j] and array[i][j] < array[i-1][j] and \
                    array[i][j] < array[i][j-1]:
                    result += array[i][j]+1

    return result


print(smoke_basin(input_array))
