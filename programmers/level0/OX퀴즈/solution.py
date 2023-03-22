def solution(quiz):
    answer = []

    def validate_result(operator: str, ops: list, res: int):
        num1, num2 = map(int, ops.split(operator))
        total = num1 + num2 if operator == " + " else num1 - num2

        return "O" if total == res else "X"

    for eq in quiz:
        arr = eq.split("=")
        ops, res = arr[0], int(arr[1])

        if " + " in ops:
            answer.append(validate_result(" + ", ops, res))
        else:
            answer.append(validate_result(" - ", ops, res))

    return answer


if __name__ == "__main__":
    test_cases = [["3 - 4 = -3", "5 + 6 = 11"], ["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]]
    for test_case in test_cases:
        print(solution(test_case))
