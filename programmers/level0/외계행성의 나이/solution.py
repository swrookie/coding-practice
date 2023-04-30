def solution(age):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    answer = "".join(alphabets[int(i)] for i in str(age))

    return answer


if __name__ == "__main__":
    test_cases = (23, 51, 100)
    for case in test_cases:
        print(solution(case))
