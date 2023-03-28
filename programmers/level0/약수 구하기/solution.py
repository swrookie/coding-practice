def solution(n):
    answer = [x for x in range(1, n + 1) if n % x == 0]
    return answer

if __name__ == "__main__":
    test_cases = (24, 29)
    for test_case in test_cases:
        print(solution(test_case))