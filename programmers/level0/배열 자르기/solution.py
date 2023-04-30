def solution(numbers, num1, num2):
    answer = numbers[num1 : num2 + 1]
    return answer


if __name__ == "__main__":
    test_cases = (([1, 2, 3, 4, 5], 1, 3), ([1, 3, 5], 1, 2))
    for case in test_cases:
        numbers, num1, num2 = case
        print(solution(numbers, num1, num2))
