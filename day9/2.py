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

        