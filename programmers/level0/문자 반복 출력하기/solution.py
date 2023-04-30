def solution(my_string, n):
    answer = "".join([c * n for c in my_string])
    return answer


if __name__ == "__main__":
    test_cases = ("hello", 3)
    for case in test_cases:
        my_string, n = case
        print(solution(my_string, n))
