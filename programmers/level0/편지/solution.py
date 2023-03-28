def solution(message):
    answer = len(message) * 2
    return answer


if __name__ == "__main__":
    test_cases = ("happy birthday!", "I love you~")
    for test_case in test_cases:
        print(solution(test_case))
