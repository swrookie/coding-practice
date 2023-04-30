def solution(balls, share):
    def factorial(x):
        res = 1
        for i in range(1, x + 1):
            res *= i
        return res

    answer = factorial(balls) // (factorial(balls - share) * factorial(share))  # 조합 공식
    return answer


if __name__ == "__main__":
    test_cases = ((3, 2), (5, 3))
    for case in test_cases:
        balls, share = case
        print(solution(balls, share))
