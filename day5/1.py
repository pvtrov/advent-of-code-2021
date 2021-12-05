
file_input = open("../inputs/day5input.txt", "r")

almost_points = []


def making_vents(file_input, almost_points):
    reading = file_input.readline()
    while reading:
        almost_points.append(reading.split())
        reading = file_input.readline()

    vents = []
    for i in range(len(almost_points)):
        vents.append([(almost_points[i][0].split(",")), almost_points[i][2].split(",")])

    for j in range(len(vents)):
        vents[j][0][1] = int(vents[j][0][1])
        vents[j][0][0] = int(vents[j][0][0])
        vents[j][1][1] = int(vents[j][1][1])
        vents[j][1][0] = int(vents[j][1][0])

    return vents


test_points = [[[0, 9], [5, 9]],
               [[9, 4], [3, 4]],
                [[2, 2], [2, 1]],
               [[7, 0], [7, 4]],
               [[0, 9], [2, 9]],
               [[3, 4], [1, 4]]]



def perpendicularly(vents_map, x, y2, y1):
    if y2 > y1:
        for i in range(y1, y2+1, 1):
            vents_map[x][i] += 1
    else:
        for i in range(y2, y1+1, 1):
            vents_map[x][i] += 1

    return vents_map


def horizontally(vents_map, y, x1, x2):
    if x1 > x2:
        for i in range(x2, x1+1, 1):
            vents_map[i][y] += 1
    else:
        for i in range(x1, x2+1, 1):
            vents_map[i][y] += 1

    return vents_map


def hydrothermal_vents(vents):
    first_vents = []
    largest_x = 0
    largest_y = 0
    for i in range(len(vents)):
        if vents[i][0][0] == vents[i][1][0] or vents[i][0][1] == vents[i][1][1]:
            first_vents.append(vents[i])
            if vents[i][0][0] > largest_x:
                largest_x = vents[i][0][0]
            if vents[i][1][0] > largest_x:
                largest_x = vents[i][1][0]
            if vents[i][0][1] > largest_y:
                largest_y = vents[i][0][1]
            if vents[i][1][1] > largest_y:
                largest_y = vents[i][1][1]

    vents_map = [[0] * (largest_x+1) for i in range(largest_y+1)]

    for i in range(len(first_vents)):
        if first_vents[i][0][0] == first_vents[i][1][0]:
            vents_map = perpendicularly(vents_map, first_vents[i][1][0], first_vents[i][1][1], first_vents[i][0][1])

        if first_vents[i][0][1] == first_vents[i][1][1]:
            vents_map = horizontally(vents_map, first_vents[i][1][1], first_vents[i][0][0], first_vents[i][1][0])

    counter = 0
    for i in range(largest_y+1):
        for j in range(largest_x+1):
            if vents_map[i][j] > 1:
                counter += 1


    return counter


print(hydrothermal_vents(making_vents(file_input, almost_points)))

# print(hydrothermal_vents(test_points))
