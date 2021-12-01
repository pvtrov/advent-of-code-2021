

def suming_measurements(depth_measurements):
    table_of_sums = []
    for i in range(len(depth_measurements)-2):
        table_of_sums.append(depth_measurements[i]+depth_measurements[i+1]+depth_measurements[i+2])

    counter = 0
    for j in range(len(table_of_sums)-1):
        if table_of_sums[j] < table_of_sums[j+1]:
            counter += 1

    return counter


f = open("../inputs/day1input.txt", "r")
input_array = [int(i) for i in f]

print(suming_measurements(input_array))