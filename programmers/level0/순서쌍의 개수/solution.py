def solution(n):
    answer = 0
    for i in range(1, n // 2 + 1):  #  불필요한 iteration 방지를 위해 자연수의 반까지만 연산
        if n % i == 0:
            answer += 1
    return answer + 1


if __name__ == "__main__":
    test_cases = (20, 100)
    for case in test_cases:
        print(solution(case))
