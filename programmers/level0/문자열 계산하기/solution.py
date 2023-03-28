def solution(my_string):
    answer = 0

    # my_string = my_string.split(" ")
    # answer = int(my_string[0])

    # for i in range(2, len(my_string), 2):
    #     if my_string[i - 1] == "+":
    #         answer += int(my_string[i])
    #     else:
    #         answer -= int(my_string[i])

    # 프로그래머스 답 참고, 굳이 list comprehension으로 새로운 리스트 생성 없이 가능하다
    answer = sum(int(x) for x in my_string.replace(" - ", " + -").split(" + "))

    return answer


if __name__ == "__main__":
    test_cases = "3 + 4"
    for test_case in test_cases:
        print(solution(test_case))
