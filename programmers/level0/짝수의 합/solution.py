def solution(n):
    answer = 0
    for i in range(2, n + 1):
        if i % 2 == 0:
            answer += i
    return answer


if __name__ == "__main__":
    test_cases = (10, 4)
    for case in test_cases:
        print(solution(case))
