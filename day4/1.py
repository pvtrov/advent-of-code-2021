# 1 i 2 w jednym bo zapomnialam ze to ten sam plik XD

numbers_array = [74, 79, 46, 2, 19, 27, 31, 90, 21, 83, 94, 77, 0, 29, 38, 72, 42, 23, 6, 62, 45, 95, 41, 55, 93, 69,
                 39, 17, 12, 1, 20, 53, 49, 71, 61, 13,
                 88, 25, 87, 26, 50, 58, 28, 51, 89, 64, 3, 80, 36, 65, 57, 92, 52, 86, 98, 78, 9, 33, 44, 63, 16, 34,
                 97, 60, 40, 66, 75, 4, 7, 84, 22, 43,
                 11, 85, 91, 32, 48, 14, 18, 76, 8, 47, 24, 81, 35, 30, 82, 67, 37, 70, 15, 5, 73, 59, 54, 68, 56, 96,
                 99, 10]

file = open("../inputs/day4input.txt", "r")

boards = []

boards_test = [[[22, 13, 17, 11, 0],
                [8, 2, 23, 4, 24],
                [21, 9, 14, 16, 7],
                [6, 10, 3, 18, 5],
                [1, 12, 20, 15, 19]],
               [[3, 15, 0, 2, 22],
                [9, 18, 13, 17, 5],
                [19, 8, 7, 25, 23],
                [20, 11, 10, 24, 4],
                [14, 21, 16, 12, 6]],
               [[14, 21, 17, 24, 4],
                [10, 16, 15, 9, 19],
                [18, 8, 23, 26, 20],
                [22, 11, 13, 6, 5],
                [2, 0, 12, 3, 7]]]

test_numbers = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1]


def making_boards(boards, file):
    check = True

    while check:
        single_board = []
        for i in range(5):
            board_line = [] * 5
            line = file.readline()
            if not line:
                check = False
                break
            board_line = line.split()
            for index in range(5):
                board_line[index] = int(board_line[index])
            single_board.append(board_line)
        xd = file.readline()
        if not check:
            break
        boards.append(single_board)

    return boards
    # boards[i][x][y] = board number, row, column


def check_bingo(single_board):
    bingo = True
    for i in range(5):
        bingo_sum = 0
        for j in range(5):
            if single_board[i][j] == -1:
                bingo_sum += 1
                if bingo_sum == 5:
                    return bingo

    for i in range(5):
        bingo_sum = 0
        j = 0
        while j < 5:
            if single_board[j][i] == -1:
                bingo_sum += 1
            j += 1
        if bingo_sum == 5:
            return bingo

    return not bingo


def suming(single_board):
    sum = 0
    for i in range(5):
        for j in range(5):
            if single_board[i][j] != -1:
                sum += single_board[i][j]

    return sum


def bingo(boards, numbers_array):
    board_check = [False for _ in range(len(boards))]
    counter = len(boards)
    for number in numbers_array:
        for i in range(len(boards)):
            if board_check[i] is False and counter != 0:
                for x in range(5):
                    for y in range(5):
                        if boards[i][x][y] == number:
                            boards[i][x][y] = -1
                            if check_bingo(boards[i]) == True:
                                board_check[i] = True
                                counter -= 1
                                if counter == 0:
                                    sum_of_marked = suming(boards[i])
                                    return (sum_of_marked) * number


print(bingo(making_boards(boards, file), numbers_array))
# print(bingo(boards_test, test_numbers))
