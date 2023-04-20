def solution(numbers, direction):
    answer = numbers[-1:] + numbers[0:-1] if direction == "right" else numbers[1:] + numbers[:1]

    return answer


if __name__ == "__main__":
    test_cases = (([1, 2, 3], "right"), ([4, 455, 6, 4, -1, 45, 6], "left"))
    for case in test_cases:
        numbers, direction = case
        print(solution(numbers, direction))
