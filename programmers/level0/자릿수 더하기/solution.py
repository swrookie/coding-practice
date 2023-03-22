def solution(n):
    answer = 0

    answer = sum(list(map(int, list(str(n)))))

    return answer


if __name__ == "__main__":
    test_cases = [1234, 930211]
    for test_case in test_cases:
        print(solution(test_case))
