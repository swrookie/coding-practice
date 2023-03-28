def solution(array):
    answer = []

    answer.append(max(array))
    answer.append(array.index(answer[0]))

    return answer


if __name__ == "__main__":
    test_cases = ([1, 8, 3], [9, 10, 11, 8])
    for test_case in test_cases:
        print(solution(test_case))
