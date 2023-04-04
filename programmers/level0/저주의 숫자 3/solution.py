def solution(n):
    answer = 0

    for i in range(1, n + 1):
        answer += 1
        while "3" in str(answer) or (answer > 2 and answer % 3 == 0):
            answer += 1

    return answer


if __name__ == "__main__":
    test_cases = (15, 40)
    for case in test_cases:
        print(solution(case))
