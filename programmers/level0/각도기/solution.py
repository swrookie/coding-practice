def solution(angle):
    answer = 0
    if angle < 90:
        answer = 1
    elif angle == 90:
        answer = 2
    elif angle < 180:
        answer = 3
    elif angle == 180:
        answer = 4

    # answer = (angle // 90) * 2 + (angle % 90 > 0) * 1 # 추후 분석 예정

    return answer


if __name__ == "__main__":
    test_cases = (70, 91, 180)
    for case in test_cases:
        print(solution(case))
