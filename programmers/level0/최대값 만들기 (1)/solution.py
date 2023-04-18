def solution(numbers):
    answer = 0
    numbers.sort()
    answer = numbers[-1] * numbers[-2]

    return answer


if __name__ == "__main__":
    test_cases = ([1, 2, 3, 4, 5], [0, 31, 24, 10, 1, 9])
    for case in test_cases:
        print(solution(case))
