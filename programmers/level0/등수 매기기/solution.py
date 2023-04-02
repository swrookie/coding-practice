def solution(score):
    answer = [sorted([sum(s) / 2 for s in score], reverse=True).index(sum(s) / 2) + 1 for s in score]

    return answer


if __name__ == "__main__":
    test_cases = (
        [[80, 70], [90, 50], [40, 70], [50, 80]],
        [[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]],
    )
    for case in test_cases:
        print(solution(case))
