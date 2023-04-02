def solution(array, n):
    answer = 0
    # array = sorted(array)
    # l = [abs(n - i) for i in array]
    # closest = min(l)
    # answer = array[l.index(closest)]

    # answer = sorted(sorted(array), key=lambda i: abs(n - i))[0]
    answer = sorted(array, key=lambda i: (abs(n - i), i))[0]

    return answer


if __name__ == "__main__":
    test_cases = (([3, 10, 28], 20), ([10, 11, 12], 13))
    for case in test_cases:
        print(solution(case[0], case[1]))
