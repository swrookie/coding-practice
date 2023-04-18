def solution(my_string):
    vowels = ("a", "e", "i", "o", "u")
    answer = "".join(c for c in my_string if c not in vowels)
    return answer


if __name__ == "__main__":
    test_cases = ("bus", "nice to meet you")
    for case in test_cases:
        print(solution(case))
