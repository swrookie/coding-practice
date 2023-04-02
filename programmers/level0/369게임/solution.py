def solution(order):
    answer = 0
    str_order = str(order)
    answer = str_order.count("3") + str_order.count("6") + str_order.count("9")
    return answer


if __name__ == "__main__":
    test_cases = (3, 29423)
    for case in test_cases:
        print(solution(case))
