def solution(my_string):
    #     l = []

    #     for c in my_string:
    #         if c not in l:
    #             l.append(c)

    #     answer = "".join(l)

    answer = "".join(dict.fromkeys(my_string).keys())

    return answer


if __name__ == "__main__":
    test_cases = ("people", "We are the world")
    for case in test_cases:
        print(solution(case))
