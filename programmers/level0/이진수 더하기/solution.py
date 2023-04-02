def solution(bin1, bin2):
    # f = lambda my_str: sum(pow(2, len(my_str) - idx - 1) for idx, c in enumerate(my_str) if c != "0")
    # answer = str(format(f(bin1) + f(bin2), 'b'))
    # answer = str(format(int(bin1, 2) + int(bin2, 2), 'b'))
    answer = bin(int(bin1, 2) + int(bin2, 2))[2:]
    return answer


if __name__ == "__main__":
    test_cases = (("10", "11"), ("1001", "1111"))
    for case in test_cases:
        print(solution(case[0], case[1]))
