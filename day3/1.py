file = open("../inputs/day3input.txt", "r")
input_array = [list(i[:-1]) for i in file]


def list_to_string(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1


def binary_diagnostic(input_array):
    gamma_rate = []
    epsilon_rate = []

    for i in range(12):
        one = 0
        zero = 0
        for element in input_array:
            if element[i] == "1":
                one += 1
            elif element[i] == "0":
                zero += 1
        if one > zero:
            gamma_rate.append("1")
            epsilon_rate.append("0")
        elif zero > one:
            gamma_rate.append("0")
            epsilon_rate.append("1")

    gamma_rate_bin = list_to_string(gamma_rate)
    epsilon_rate_bin = list_to_string(epsilon_rate)

    g = int(gamma_rate_bin, 2)
    e = int((epsilon_rate_bin), 2)

    return g*e


print(binary_diagnostic(input_array))
