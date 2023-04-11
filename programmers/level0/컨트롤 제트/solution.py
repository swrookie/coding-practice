def solution(s):
    answer = 0

    s_list = s.split(" ")

    def ctrlz(e):
        if e == "Z":
            new_e = int(s_list[s_list.index(e) - 1]) * -1
            s_list[s_list.index(e)] = new_e
        else:
            new_e = int(e)

        return new_e

    answer = sum(map(ctrlz, s_list))

    return answer


if __name__ == "__main__":
    test_cases = ("1 2 Z 3", "10 20 30 40", "10 Z 20 Z 1", "10 Z 20 Z", "-1 -2 -3 Z")

    for case in test_cases:
        print(solution(case))
