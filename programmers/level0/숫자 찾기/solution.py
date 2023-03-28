def solution(num, k):
    answer = 0
    num, k = str(num), str(k)
    answer = num.index(k) + 1 if k in num else -1

    return answer


if __name__ == "__main__":
    test_cases = ((29183, 1), (232443, 4), (123456, 7))
    for test_case in test_cases:
        print(solution(test_case[0], test_case[1]))
