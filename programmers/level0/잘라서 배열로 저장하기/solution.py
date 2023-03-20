def solution(my_str, n):
    answer = []
    size = len(my_str)

    for i in range(0, size, n):
        answer.append(my_str[i : i + n])

    return answer


if __name__ == "__main__":
    test_cases = ["abc1Addfggg4556b", "abcdef123"]
    for test_case in test_cases:
        print(solution(test_case))
