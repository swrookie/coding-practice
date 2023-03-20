def solution(M, N):
    answer = 0

    answer = M * N - 1

    return answer


if __name__ == "__main__":
    test_cases = [(2, 2), (2, 5), (1, 1)]
    for test_case in test_cases:
        print(solution(test_case[0], test_case[1]))
