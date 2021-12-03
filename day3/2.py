file = open("../inputs/day3input.txt", "r")
input_array = [list(i[:-1]) for i in file]


def suming_for_oxygen(array_to_sort, i):
    while len(array_to_sort) > 1:
        zeroes = []
        ones = []

        for element in array_to_sort:
            if element[i] == "1":
                ones.append(element)
            else:
                zeroes.append(element)

        if len(ones) >= len(zeroes):
            return suming_for_oxygen(ones, i+1)
        else:
            return suming_for_oxygen(zeroes, i+1)
    return array_to_sort


def suming_for_co(array_to_sort, i):
    while len(array_to_sort) > 1:
        zeroes = []
        ones = []

        for element in array_to_sort:
            if element[i] == "1":
                ones.append(element)
            else:
                zeroes.append(element)

        if len(ones) >= len(zeroes):
            return suming_for_co(zeroes, i+1)
        else:
            return suming_for_co(ones, i+1)
    return array_to_sort


def list_to_string(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1


def oxygen_and_co(input_array):
    oxygen = suming_for_oxygen(input_array, 0)
    co = suming_for_co(input_array, 0)

    oxygen_bin = list_to_string(oxygen[0])
    co_bin = list_to_string(co[0])

    return int(oxygen_bin, 2) * int(co_bin, 2)



print(oxygen_and_co(input_array))