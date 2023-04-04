def solution(sides):
    answer = 0

    min_s, max_s = min(sides), max(sides)
    answer += len(list(range(max_s - min_s + 1, max_s + 1))) + len(list(range(max_s + 1, min_s + max_s)))

    # 공식...?
    # sum(sides) - max(sides) + min(sides) - 1

    return answer


if __name__ == "__main__":
    test_cases = (
        [1, 2],
        [3, 6],
        [11, 7],
    )
    for case in test_cases:
        print(solution(case))
