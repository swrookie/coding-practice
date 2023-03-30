def solution(my_string, num1, num2):
    answer = ""
    l = []

    #     for idx, c in enumerate(my_string):
    #         if idx == num1:
    #             l.append(my_string[num2])
    #         elif idx == num2:
    #             l.append(my_string[num1])
    #         else:
    #             l.append(c)

    #     answer = "".join(l)

    l = list(my_string)
    l[num1], l[num2] = l[num2], l[num1]

    answer = "".join(l)

    return answer


if __name__ == "__main__":
    test_cases = (("hello", 1, 2), ("I love you", 3, 6))
    for case in test_cases:
        print(solution(case[0], case[1], case[2]))
