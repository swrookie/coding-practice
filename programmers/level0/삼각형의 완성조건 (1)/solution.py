def solution(sides):
    answer = 1 if max(sides) < sum(sorted(sides)[:2]) else 2
    return answer

if __name__ == "__main__":
    test_cases = ([1, 2, 3], [3, 6, 2], [199, 72, 222])
    for case in test_cases:
        print(solution(case))