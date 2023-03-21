def solution(array):
    answer = 0

    for e in array:
        num_chars = list(str(e))
        answer += num_chars.count("7")

    return answer


if __name__ == "__main__":
    test_cases = [[7, 77, 17], [10, 29]]
    for test_case in test_cases:
        print(solution(test_case))
