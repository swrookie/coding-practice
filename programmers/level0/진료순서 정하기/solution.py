def solution(emergency):
    emergency_sorted = sorted(emergency, reverse=True)
    answer = [emergency_sorted.index(e) + 1 for e in emergency]

    return answer


if __name__ == "__main__":
    test_cases = ([3, 76, 24], [1, 2, 3, 4, 5, 6, 7], [30, 10, 23, 6, 100])
    for case in test_cases:
        print(solution(case))
