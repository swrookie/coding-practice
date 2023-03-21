def solution(my_string):
    answer = ""

    answer = "".join(sorted(list(my_string.lower())))

    return answer


if __name__ == "__main__":
    test_cases = ["Bcad", "heLLo", "Python"]
    for test_case in test_cases:
        print(solution(test_case))
