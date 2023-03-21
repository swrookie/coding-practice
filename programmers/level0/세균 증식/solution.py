def solution(n, t):
    answer = 0

    answer = n * pow(2, t)

    return answer


if __name__ == "__main__":
    test_cases = [(2, 10), (7, 15)]
    for test_case in test_cases:
        print(solution(test_case[0], test_case[1]))
