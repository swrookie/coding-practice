def solution(before, after):
    answer = 1 if sorted(before) == sorted(after) else 0
    return answer


if __name__ == "__main__":
    test_cases = (("olleh", "hello"), ("allpe", "apple"))
    for case in test_cases:
        print(solution(case[0], case[1]))
