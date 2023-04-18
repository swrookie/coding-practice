def solution(n):
    answer = 1
    total = 1

    for i in range(2, n + 1):
        total *= i
        if total > n:
            break
        answer = i

    return answer


if __name__ == "__main__":
    test_cases = (3628800, 7)
    for case in test_cases:
        print(solution(case))
