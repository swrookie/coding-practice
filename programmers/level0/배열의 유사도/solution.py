def solution(s1, s2):
    answer = 0

    # for s in s1:
    #     if s in s2:
    #         answer += 1

    # &는 비트 AND 연산, 파이썬에서는 교차(intersection), set에 활용 가능
    answer = len(set(s1) & set(s2))

    return answer


if __name__ == "__main__":
    test_cases = ((["a", "b", "c"], ["com", "b", "d", "p", "c"]), (["n", "omg"], ["m", "dot"]))
    for test_case in test_cases:
        print(solution(test_case[0], test_case[1]))
