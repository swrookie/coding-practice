def solution(my_string):
    answer = sum(int(c) for c in my_string if c.isdigit())

    return answer


if __name__ == "__main__":
    test_cases = ("aAb1B2cC34oOp", "1a2b3c4d123")

    for case in test_cases:
        print(solution(case))
