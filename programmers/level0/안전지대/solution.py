def solution(board):
    answer = 0
    n = len(board)
    # 위, 아래, 좌, 우, 위좌, 위우, 아래좌, 아래우
    coords = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1))

    def fill_danger(board, r_idx, c_idx):
        for coord in coords:
            new_r, new_c = r_idx + coord[0], c_idx + coord[1]
            if (new_r > -1 and new_r < n) and (new_c > -1 and new_c < n):
                board[new_r][new_c] = -1 if board[new_r][new_c] != 1 else 1

    for r_idx, r in enumerate(board):
        for c_idx, c in enumerate(r):
            if c == 1:
                fill_danger(board, r_idx, c_idx)

    for r in board:
        answer += r.count(0)

    return answer


if __name__ == "__main__":
    test_cases = (
        [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]],
        [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]],
        [
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
        ],
    )

    for case in test_cases:
        print(solution(case))
