input_file = open("../inputs/day8input.txt", "r")

input_array = []
f = input_file.readline().split()

while f:
    input_array.append(f)
    f = input_file.readline().split()


patterns = [["c", "a", "g", "e", "d", "b"],
            ["a", "b"],
            ["g", "c", "d", "f", "a"],
            ["f", "b", "c", "a", "d"],
            ["e", "a", "f", "b"],
            ["c", "d", "f", "b", "e"],
            ["c", "d", "f", "g", "e", "b"],
            ["d", "a", "b"],
            ["a", "c", "e", "d", "g", "f", "b"],
            ["c", "e", "f", "a", "b", "d"]]

