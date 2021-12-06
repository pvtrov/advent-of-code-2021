
file_input = open("../inputs/day6input.txt", "r")

test_input = [3,4]
test_case1 = 18
result_case, test_case2 = 80, 80


def test_making(test_input):
    fish = [[] for _ in range(257)]
    for i in range(len(test_input)):
        fish[0].append(test_input[i])

    return fish


def making_fish_array(file):
    fish_times = [[] for _ in range(257)]
    table = file.readline().split(",")
    for i in range(len(table)):
        fish_times[0].append(int(table[i]))

    return fish_times


def lanternfish(fish_times):
    for i in range(0, len(fish_times)-1):
        for fish in fish_times[i]:
            if fish-1 == -1:
                fish_times[i+1].append(6)
                fish_times[i+1].append(8)
            else:
                fish_times[i+1].append(fish-1)

    result = len(fish_times[len(fish_times)-1])
    return result


print(lanternfish(making_fish_array(file_input)))
# print(lanternfish(test_making(test_input)))