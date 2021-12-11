input_file = open("../inputs/day10input.txt", "r")

input_array = []
f = list(input_file.readline())

while f:
    f.remove("\n")
    input_array.append(f)
    f = list(input_file.readline())

print(input_array)

pairs = {
    "(" : ")",
    "[" : "]",
    "{" : "}",
    "<" : ">"
}


def counting_chunks(array, pairs):
    points = {
        ")" : 3,
        "]" : 57,
        ">" : 25137,
        "}" : 1197
    }
    result = 0

    for i in range(len(array)):
        stack = []
        for j in range(len(array[i])):
            elem = array[i][j]
            if elem in ["(", "[", "<", "{"]:
                stack.append(elem)
            else:
                taken = stack.pop()
                if pairs[taken] != elem:
                    result += points[elem]
                    break

    return result


print(counting_chunks(input_array, pairs))