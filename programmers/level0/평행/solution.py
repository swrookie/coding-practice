def solution(dots):
    answer = 0
    # Euclidean Distance
    # f = lambda d1,d2: pow(pow(d1[0] - d1[1], 2) + pow(d2[0] - d2[1], 2), 0.5)

    # parallel = (lset1[0] == lset2[1] and lset1[1] == lset2[0]) or (lset1[0] == lset3[1] and lset1[1] == lset3[0]) or (lset2[0] == lset3[1] and lset2[1] == lset3[0])

    # Slope Formula
    f = lambda d1, d2: (d2[1] - d1[1]) / (d2[0] - d1[0])

    dot1, dot2, dot3, dot4 = dots
    lset1, lset2, lset3 = (f(dot1, dot2), f(dot3, dot4)), (f(dot1, dot3), f(dot2, dot4)), (f(dot2, dot3), f(dot1, dot4))

    parallel = (lset1[0] == lset1[1]) or (lset2[0] == lset2[1]) or (lset3[0] == lset3[1])

    answer = 1 if parallel else 0

    return answer


if __name__ == "__main__":
    test_cases = ([[1, 4], [9, 2], [3, 8], [11, 6]], [[3, 5], [4, 1], [2, 4], [5, 10]])
    for case in test_cases:
        print(solution(case))
