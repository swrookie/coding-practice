def solution(cipher, code):
    # answer = "".join([cipher[i - 1] for i in range(code, len(cipher) + 1, code)])
    answer = cipher[code - 1 :: code]  # Python advanced string slicing feature
    return answer


if __name__ == "__main__":
    test_cases = (("dfjardstddetckdaccccdegk", 4), ("pfqallllabwaoclk", 2))
    for case in test_cases:
        print(solution(case[0], case[1]))
