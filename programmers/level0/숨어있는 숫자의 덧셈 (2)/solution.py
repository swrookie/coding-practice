# import re


def solution(my_string):
    # answer = sum(int(c) for c in re.sub(r"[a-z|A-z]", " ", my_string).split(" ") if c.isdigit())
    answer = sum(
        map(int, (filter(lambda c: c.isdigit(), "".join(c if c.isdigit() else " " for c in my_string).split(" "))))
    )  # 정규식 없이

    return answer


if __name__ == "__main__":
    test_cases = ("aAb1B2cC34oOp", "1a2b3c4d123Z")

    for case in test_cases:
        print(solution(case))
