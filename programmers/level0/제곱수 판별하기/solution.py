import math


def solution(n):
    answer = 0

    answer = 1 if math.sqrt(n).is_integer() else 2
    # answer = 1 if pow(n, 0.5).is_integer() else 2 라이브러리 임포트 없이

    return answer


if __name__ == "__main__":
    test_cases = [144, 976]
    for test_case in test_cases:
        print(solution(test_case))
