def solution(keyinput, board):
    answer = [0, 0]

    d = {"up": (0, 1), "down": (0, -1), "left": (-1, 0), "right": (1, 0)}
    max_x, max_y = board
    max_x_move, max_y_move = max_x // 2, max_y // 2

    for input in keyinput:
        cur_x, cur_y = answer
        new_x, new_y = d.get(input)
        if abs(new_x + cur_x) <= max_x_move and abs(new_y + cur_y) <= max_y_move:
            answer[0], answer[1] = new_x + cur_x, new_y + cur_y

    return answer


if __name__ == "__main__":
    test_cases = (
        (["left", "right", "up", "right", "right"], [11, 11]),
        (["down", "down", "down", "down", "down"], [7, 9]),
    )

    for case in test_cases:
        keyinput, board = case
        print(solution(keyinput, board))
