def solution(board, moves):
    answer = 0
    count = 0
    stack = []

    row_len = len(board)
    for move in moves:
        for r in range(0, row_len):
            new_doll = board[r][move - 1]
            if new_doll > 0:
                if stack:
                    top_doll = stack[-1]
                    if new_doll == top_doll:
                        stack.pop()
                        count += 2
                    else:
                        stack.append(new_doll)
                else:
                    stack.append(new_doll)
                board[r][move - 1] = 0
                break

    answer = count

    return answer


if __name__ == "__main__":
    board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
    moves = [1, 5, 3, 5, 1, 2, 1, 4]
    print(solution(board, moves))
