def solution(my_string):
    answer = sorted(int(c) for c in my_string if c.isdigit())
    return answer


if __name__ == "__main__":
    test_cases = ("hi12392", "p2o4i8gj2", "abcde0")
    for case in test_cases:
        print(solution(case))
