def solution(strlist):
    answer = [len(s) for s in strlist]

    return answer


if __name__ == "__main__":
    test_cases = (["We", "are", "the", "world!"], ["I", "Love", "Programmers."])

    for case in test_cases:
        print(solution(case))
