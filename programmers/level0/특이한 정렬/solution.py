def solution(numlist, n):
    answer = sorted(numlist, key=lambda x: (abs(n - x), -x))
    return answer


if __name__ == "__main__":
    test_cases = (([1, 2, 3, 4, 5, 6], 4), ([10000, 20, 36, 47, 40, 6, 10, 7000], 30))
    for case in test_cases:
        print(solution(case[0], case[1]))
