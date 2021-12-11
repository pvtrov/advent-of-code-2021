input_file = open("../inputs/day10input.txt", "r")

input_array = []
f = list(input_file.readline())

while f:
    f.remove("\n")
    input_array.append(f)
    f = list(input_file.readline())

# print(input_array)

pairs = {
    "(" : ")",
    "[" : "]",
    "{" : "}",
    "<" : ">"
}


def counting_chunks(array, pairs):
    results = [0 for _ in range(len(array))]
    points = {
        ")" : 1,
        "]" : 2,
        ">" : 4,
        "}" : 3
    }
    broken_rows = []
    for i in range(len(array)):
        stack = []
        for j in range(len(array[i])):
            elem = array[i][j]
            if elem in ["(", "[", "<", "{"]:
                stack.append(elem)
            else:
                taken = stack.pop()
                if pairs[taken] != elem:
                    broken_rows.append(i)

    result = 0

    for i in range(len(array)):
        if i not in broken_rows:
            result = 0
            stack = []
            for j in range(len(array[i])):
                elem = array[i][j]
                if elem in ["(", "[", "<", "{"]:
                    stack.append(elem)
                else:
                    taken = stack.pop()

            while len(stack) > 0:
                element = stack.pop()
                result = result*5 + points[pairs[element]]

            results[i] = result

    actual_results = []
    for j in range(len(results)):
        if results[j] != 0:
            actual_results.append(results[j])

    actual_results.sort()
    res = actual_results[len(actual_results)//2]

    return res


print(counting_chunks(input_array, pairs))