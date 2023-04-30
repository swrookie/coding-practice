def solution(my_string, letter):
    answer = my_string.replace(letter, "")
    return answer


if __name__ == "__main__":
    test_cases = (("abcdef", "f"), ("BCBdbe", "B"))
    for case in test_cases:
        my_string, letter = case
        print(solution(my_string, letter))
