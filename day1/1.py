

def depth_measurement(input_array):
    counter = 0
    for i in range(0, len(input_array)-1):
        if input_array[i] < input_array[i+1]:
            counter += 1

    return counter


f = open("../inputs/day1input.txt", "r")
input_array = [int(i) for i in f]


print(depth_measurement(input_array))