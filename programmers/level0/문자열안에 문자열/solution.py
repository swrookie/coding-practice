def solution(str1, str2):
    answer = 0

    answer = 1 if str2 in str1 else 2

    return answer


if __name__ == "__main__":
    test_cases = [("ab6CDE443fgh22iJKlmn1o", "6CD"), ("ppprrrogrammers", "pppp"), ("AbcAbcA", "AAA")]
    for test_case in test_cases:
        print(solution(test_case[0], test_case[1]))
