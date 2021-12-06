
file_input = open("../inputs/day6input.txt", "r")
test_input = [3,4, 3, 1, 2]
test_case1 = 18
result_case, test_case2 = 80, 80

def test_making(test_input):
    fish = []
    for i in range(len(test_input)):
        fish.append(test_input[i])

    fish_test = [0 for i in range(9)]
    for j in range(len(fish)):
        fish_test[fish[j]] += 1

    return fish_test



def making_fish_array(file):
    fish_times = []
    table = file.readline().split(",")
    for i in range(len(table)):
        fish_times.append(int(table[i]))

    fish_days = [0 for i in range(9)]
    for j in range(len(fish_times)):
        fish_days[fish_times[j]] += 1

    return fish_days


def deep_copy(fish):
    temp_fish = []
    for i in range(len(fish)):
        temp_fish.append(fish[i])

    return temp_fish


def counting_lanternfish(fish):
    for i in range(256):
        temp_fish = deep_copy(fish)
        for i in range(8):
            fish[i] = temp_fish[i+1]
        fish[6] += temp_fish[0]
        fish[8] = temp_fish[0]

    result = 0
    for s in range(9):
        result += fish[s]

    return result

# print(making_fish_array(file_input))
# print(counting_lanternfish(test_making(test_input)))
print(counting_lanternfish(making_fish_array(file_input)))