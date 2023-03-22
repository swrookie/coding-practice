def solution(n, numlist):
    answer = []

    answer.extend(filter(lambda x: x % n == 0, numlist))

    return answer


if __name__ == "__main__":
    test_cases = [(3, [4, 5, 6, 7, 8, 9, 10, 11, 12]), (5, [1, 9, 3, 10, 13, 5]), (12, [2, 100, 120, 600, 12, 12])]
    for test_case in test_cases:
        print(solution(test_case[0], test_case[1]))
