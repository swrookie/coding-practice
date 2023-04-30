def solution(n, k):
    answer = n * 12000 + k * 2000 - n // 10 * 2000
    return answer


if __name__ == "__main__":
    test_cases = ((10, 3), (64, 6))
    for case in test_cases:
        n, k = case
        print(solution(n, k))
