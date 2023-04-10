def solution(numbers):
    answer = 0
    numbers.sort()

    if abs(numbers[0]) >= abs(numbers[-1]) and numbers[1] < 0:
        answer = numbers[0] * numbers[1]
    else:
        answer = numbers[-1] * numbers[-2]

    return answer


if __name__ == "__main__":
    test_cases = ([1, 2, -3, 4, -5], [0, -31, 24, 10, 1, 9], [10, 20, 30, 5, 5, 20, 5])

    for case in test_cases:
        print(solution(case))
