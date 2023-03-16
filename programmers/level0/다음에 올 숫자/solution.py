# 등차수열: 첫째항에 일정한 수를 더해서 얻은 항으로 이루어진 수열
# 등비수열: 첫째항에 일정한 수를 곱해서 얻은 항으로 이루어진 수열
def solution(common):
    answer = 0

    num1 = common[0]
    num2 = common[1]

    if num2 + num2 - num1 in common:
        # 등차수열
        answer = common[-1] + num2 - num1
    else:
        # 등비수열
        answer = common[-1] * (num2 / num1)

    return answer

if __name__ == "__main__":
    test_cases = [[1, 2, 3, 4], [2, 4, 8]]
    for test_case in test_cases:
        print(solution(test_case))
